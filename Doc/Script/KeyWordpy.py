from inspect import signature
from Action import Action
from PlatFormAdmin import PlatFormAdmin
from UDF import UDF
from MDB import MDB
from UpLoad import UpLoad
from Login import Login
from InSight import InSight
from WorkDesk import WorkDesk
from ECR import ECR
from ReportPackage import ReportPackage
from UpLoad import UpLoad
from FileIO import FileIO
from DBConnector import DBConnector
class KeyWord:
  case={}
  def __init__(self):
    self.Case = {
                "OPENAPP"						 	      : Login.IMSLogin,
                "OPENINSIGHTAPP"						: Login.InSightLogin,
                "OPENECRAPP"						 	  : Login.EcrLogin,
								"OPENAPP1" 									:	Action.OpenApplication,
								"KEYIN"											:	Action.KeyIn,
								"TYPESTR"										:	Action.TypeString,
								"TYPEEMAIL"                 : Action.TypeEmail,
								"TYPEDATE"                  : Action.TypeDate,
								"CLICK"											: Action.Click,
								"CLICKWOSCROLL"							: Action.ClickWithOutScroll,
								"CLICKBUTTON"								: Action.ClickButton,
								"CHECKED"										: Action.Checked,
								"CLICKCHECKED"							: Action.ClickChecked,
								"CLICKITEM"									:	Action.SelectByVisibleText,
								"CLICKITEMBYINDEX"					:	Action.SelectByIndex,
								"CLICKITEMBYOPTVALUE"				:	Action.SelectByValue,
								"CLEANUP"										:	Action.CleanUp,
								"SETENV"										: Action.SetEnv,
								"CLICKCHECK"								: Action.ClickCheck,
								"CLICKIFFOUND"							: Action.ClickIfFound,
								"CLICKNGO"									: Action.ClickGo,
								"CLICKUNCHECK"							: Action.ClickUnCheck,
								"CLICKXY"										: Action.ClickOnXY,
								"CLOSE"											: Action.Close,
								"COMBOBOXIN"								: Action.ComboBoxIn,
								"COMP_TEXT"									: Action.CompareByTextContent,
								"DRAG"											: Action.DragAndDrop,
								"EXPORT"										: Action.ExportFile,
								"GETOBJ"										: Action.GetObject,
								"GETTEXT"										:	Action.GetText,
								"ISDISABLE" 							  : Action.IsDisable,
								"KEYINRANDEMAIL" 						: Action.KeyInRandomEmail,
								"KEYINRANDNUM" 							: Action.KeyInRandomInt,
								"KEYINRANDTEXT" 						: Action.KeyInRandomText,
								"KEYINTEXT"									: Action.KeyInText,
								"KEYINWOCLEAN"							: Action.KeyInWithOutClean,
								"LISTITEM"									: Action.ListItem,
								"OBJLISTITEM"						    : Action.ObjectListItem,
								"OBJKEYIN"									: Action.ObjectKeyIn,
								"SELECTITEM"								: Action.SelectItemByIndex,
								"SELECTRANDITEM"						: Action.SelectItemByRandomIndex,
								"SETVAL"										: Action.SetValue,
								"TERMINATEBROWSER"					: Action.TerminateBrowser,
								"VALCOMP"										: Action.CompareByValue,
								"STORE"											: Action.SetTempVal,
								"REPORT"										: Action.Report,
								"WAITSPIN"									: Action.WaitTillSpinnerActive,
								"WAIT"											: Action.Wait,
								"READQUEST"								  : Action.ReadQuest,
								"ANSSECQUEST"								: Action.AnsSecQuest,
								"SYNC"											: Action.Sync,
								"TABKEYS"                   : Action.TabKeys,
								"VRF_CLICKCHECK"						: Action.ValidateCheckbox,
								"VRF_DROPDOWNTEXT"					: Action.ValidateDropDownText,   
								"PROCTOXL"									: Action.ExportToExcel,
								"PAUSE"                     : Action.Pause, 
								
								
#PlatForm Admin KeyWords
								"INVSUBMIT"									: PlatFormAdmin.SubmitInvestierRequest,
								"PLATADMCHKSTAT"						: PlatFormAdmin.VarifyJobStatus,
								"VERGENSTAT"								:	PlatFormAdmin.VerifyGenevaRSLString,
								"PLATADMWAITFORJCOMP"				:	PlatFormAdmin.WaitTillGenevaRequestComplete,
								"GENSUBMIT"									:	PlatFormAdmin.SetGenevaRequestTime,
								
								
#UDF KeyWords
								"OPENUDFSCREEN"							:	UDF.OpenScreen,
								"OPENACCOUNT"								:	UDF.OpenAccount,
								"UDFUIEDIT"									:	UDF.UIEdit,
								"UDFETLUPLOAD"							:	UDF.UdfEtlFileUpload,
								"VER_ETL_UPD"								:	UDF.VerifyETLUpdate,
								"UPLOADPATH"								:	UpLoad.UpLoad,
								
								
#MDB KeyWords
								"OPENMDBREPORT"							: MDB.OpenReport,
								"VERIFYFIELDS"							: MDB.ValidateAddRemoveColumn,
								"VER_GRN_TOT"								: MDB.ValidateGrandTotalSum,
								"MDB_FILTER"								: MDB.ValidateFilter,
								"MDB_DYNFILTER"							: MDB.ValidateDynamicFilter,
								"MDB_SORT"									: MDB.ValidateSorting,
								"MAKEBYNDCMPREADY"					: FileIO.CopyFileAndFolder,
								
								
# InSight
								"CLICKVISLASTREC"						: InSight.ClickOnLastRecord,
								"ENTERULTIBENSTOREDVAL"			: InSight.GetUltimateBeneficiaryAccountNumber1,
								"ENTERFUNDMNEMONICSTOREDVAL": InSight.GetFundMnemonic,
								"ENTERFUNDMNEMONICSTOREDVAL2":InSight.GetFundMnemonic2,
								"ENTERULTBENACCOUNT"        : InSight.GetUltimateBeneficiaryAccountNumber2,
								"ENTERINVESTORLEGALNAME"		: InSight.GetInvestorLegalName,
								"GETEXTERNALINVESTORID"			: InSight.GetExternalInvestorID,
								"SETSEARCHTEXT"							: InSight.SetSearchText,
								"INGKEYINRANDTEXT"					: InSight.SetUltimateBeneficiaryAccountNumber2,
								"INGLGINVKEYINRANDTEXT"     : InSight.SetExternalInvestorID,
								"INVRELMASTER_VFY"					: InSight.InvMasterRelationShipVerify,
								"GETUPDATEINV"							:	InSight.GetColumnPositionByAttribute,
																

#ReportPackage
								"OPENRP"										: ReportPackage.OpenRp,
								"SELREPINQ"									: ReportPackage.SelectReportByINQ,
								"VERIFYAVLLISTSEARCH"				: ReportPackage.VerifySearchAvailableList,
								"VERIFYSELLISTSEARCH"				: ReportPackage.VerifySearchSelList,
								"SEARCHRP"									: ReportPackage.SearchForReportPackage,
								"VERIFYREPPACKSEARCHGRID"		: ReportPackage.VerifyRepPackGridSearch,
								"VERIFYREPPACKLEFTNAV"			: ReportPackage.VerifyRepPackLeftNavSearch,
								"VERIFYRPEXPORT"						: ReportPackage.VerifyRepPackExport,
								"VERIFYREPDELETE"						: ReportPackage.VerifyDeleteRepPack,
								"VERIFYSCHEDREPLABEL"				: ReportPackage.VerifySchedPackageLabel,
								"VERIFYSCHEDREPJOBNAME"			: ReportPackage.VerifySchedPackageJobName,
								"VERIFYUNCONSOLREPCOUNT"		: ReportPackage.verifyNumOfExpFiles,
								"VERIFYUNCONSOLREPNAME"			: ReportPackage.VerifyUnconsolExpFileNames,
								"VERIFYINCLPARAM"						: ReportPackage.VerifyExcelInclParamConsolidated,
								"VERIFYEXTERNALACCID"				: ReportPackage.VerifyExcelInclExternalIdConsolidated,
								"VERIFYEXCELTABS"           : ReportPackage.VerifyExpExcelTabs,
								"ENTERPARAM"                : ReportPackage.enterParam,
								"VERIFYEXCELNODATA"         : ReportPackage.VerifyExcelNoData,
								
								
#WorkDesk
								"NEWCLICKITEM"							: Action.SelectByVisibleText2,
								"WAITDIVOVERLAY"						: Action.WaitTillOvelayDivActive,
								"WAITSPIN"                  : Action.WaitTillSpinnerActive,
								"WORKDESKCLICK"							: WorkDesk.WorkDeskClick,
#								"VERIFY_MOVES"              : WorkDesk.VerifyMove,
								"VERIFY_WDSEARCH"           : WorkDesk.VerifyJIRASearchTicket,
								"WD_VRFTCK"                 : WorkDesk.JiraTicketVerifyFromDatabase,
								
#ECR
								"LISTITEMWOSCROLL"					: ECR.ListItem,
								"REPORTO"					          : Action.ReportTo,
								"STOREINTEXT"								: ECR.SaveBatchId
								}