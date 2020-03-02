import argparse
import pandas as pd
import numpy as np
import os

def create_dir():
    if not os.path.exists(r"D:/DataComp"):
        os.makedirs(r"D:/DataComp")

def report_diff(x):
    return x[0] if x[0] == x[1] or pd.isna(x).all() else f'In Source ({x[1]}) -> In Target ({x[0]})'


def strip(x):
    return x.strip() if isinstance(x, str) else x


def diff_pd(old_df, new_df, idx_col):
    # setting the column name as index for fast operations
    old_df = old_df.set_index(idx_col)
    new_df = new_df.set_index(idx_col)
    # get the added and removed rows
    old_keys = old_df.index
    new_keys = new_df.index
    removed_keys = np.setdiff1d(old_keys, new_keys)
    added_keys = np.setdiff1d(new_keys, old_keys)
    out_data = {'AddedIntoTargetFromSource': old_df.loc[removed_keys]}#, 'AddedIntoSourceFromTarget': new_df.loc[added_keys]}
    # focusing on common data of both dataframes
    common_keys = np.intersect1d(old_keys, new_keys, assume_unique=True)
    common_columns = np.intersect1d(old_df.columns, new_df.columns, assume_unique=True)
    new_common = new_df.loc[common_keys, common_columns].applymap(strip)
    old_common = old_df.loc[common_keys, common_columns].applymap(strip)
    # get the changed rows keys by dropping identical rows
    # (indexes are ignored, so we'll reset them)
    common_data = pd.concat([old_common.reset_index(), new_common.reset_index()])
    changed_keys = common_data.drop_duplicates(keep=False)[idx_col].unique()
    # combining the changed rows via multi level columns
    df_all_changes = pd.concat([old_common.loc[changed_keys], new_common.loc[changed_keys]], axis='columns',
                               keys=['old', 'new'])
    df_all_changes = df_all_changes.swaplevel(axis='columns')[new_common.columns]
    # using report_diff to merge the changes in a single cell with "-->"
    df_changed = df_all_changes.groupby(level=0, axis=1).apply(lambda frame: frame.apply(report_diff, axis=1))
    out_data['DiffSourceToTarget'] = df_changed.style.applymap(lambda x: f"color: {'red'if isinstance(x, str) and 'In Source' in x and 'In Target' in x else 'black' }")
    #common_data2 = pd.concat([pd.DataFrame(eval(out_data['DiffSourceToTarget'])),pd.DataFrame(eval(out_data['AddedIntoTargetFromSource']))])
    return out_data

def read_merger_data(path):
    df1 = pd.read_excel(path, sheet_name="AddedIntoTargetFromSource", dtype='object')
    df2 = pd.read_excel(path, sheet_name="DiffSourceToTarget", dtype='object')
    df3 = pd.concat([df1,df2],sort=False)
    with pd.ExcelWriter(path) as writer:
            df3.to_excel(writer, sheet_name="sname")
    print(f"Differences saved in {path}")

def compare_excel(source, target,index_col_name=None):
    lstSheets = pd.read_excel(target, None).keys()
    lstSheets2 = pd.read_excel(source, None).keys()
    for sheet_name in lstSheets:
        if(sheet_name in lstSheets2 and sheet_name not in ['ListOfAllSheetNames','Screens','Merchandise_Hierarchy']):
            dataFrameSource = pd.read_excel(source, sheet_name=sheet_name,dtype = 'object')
            dataFrameTarget = pd.read_excel(target, sheet_name=sheet_name,dtype = 'object')
            dataFrameDiff = diff_pd(dataFrameSource, dataFrameTarget, index_col_name)
            out_path = r"D:/DataComp/"+sheet_name+".xlsx"
            with pd.ExcelWriter(out_path) as writer:
                for sname, data in dataFrameDiff.items():
                    data.to_excel(writer, sheet_name=sname)
            print(f"Differences saved in {out_path}")

strSourceFilePath = r"D:\Master\InputData.xlsx"
strTargetFilePath = r"D:\Anuj\InputData.xlsx"

create_dir();
#compare_excel(strTargetFilePath,strSourceFilePath, "UniqueID")

