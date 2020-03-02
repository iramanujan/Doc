using AutomationCommonDevelopmentKit.Attributes.EnumAttribute;
using OpenQA.Selenium;
using Orange.HRM.TestHarness.Core;
using Orange.HRM.TestHarness.Data;
using SeleniumFrameworkDevelopmentKit.Model.Extensions;
using System.Collections.ObjectModel;

namespace Orange.HRM.TestHarness.Page.Admin.UserManagement.Users
{
    public class SystemUsersPageMap : BasePageElementMap
    {
        public enum ColumnNames
        {
            [System.ComponentModel.Description("Username")]
            USERNAME = 0,

            [System.ComponentModel.Description("User Role")]
            USERROLE = 1,

            [System.ComponentModel.Description("Employee Name")]
            EMPLOYEENAME = 2,

            [System.ComponentModel.Description("Status")]
            STATUS = 3,
        }
        public IWebElement Admin => webDriver.GetWebElement(By.CssSelector("#menu_admin_viewAdminModule"));
        public IWebElement UserManagement => webDriver.GetWebElement(By.CssSelector("#menu_admin_UserManagement"));
        public IWebElement User => webDriver.GetWebElement(By.CssSelector("#menu_admin_viewSystemUsers"));
        public IWebElement UserName => webDriver.FindElement(By.CssSelector("#searchSystemUser_userName"));
        public IWebElement UserRole => webDriver.FindElement(By.CssSelector("#searchSystemUser_userType"));
        public IWebElement EmployeeName => webDriver.FindElement(By.CssSelector("#searchSystemUser_employeeName_empName"));
        public IWebElement Status => webDriver.FindElement(By.CssSelector("#searchSystemUser_status"));
        public IWebElement Search => webDriver.FindElement(By.CssSelector("#searchBtn"));
        public IWebElement ReSet => webDriver.FindElement(By.CssSelector("#resetBtn"));
        public IWebElement Add => webDriver.FindElement(By.CssSelector("#btnAdd"));
        public IWebElement Delete => webDriver.FindElement(By.CssSelector("#btnDelete"));

        public ReadOnlyCollection<IWebElement> RowsUserRole => webDriver.FindElements(By.CssSelector("#resultTable > tbody > tr > td:nth-child(3)"));
        public ReadOnlyCollection<IWebElement> RowsStatus => webDriver.FindElements(By.CssSelector("#resultTable > tbody > tr > td:nth-child(5)"));
        public ReadOnlyCollection<IWebElement> TableHeader => this.webDriver.FindElements(By.CssSelector("#resultTable > thead > tr > th > a"));
        public IWebElement Cell(ColumnNames columnNames, CellPosition cellPosition = CellPosition.VALUE_BASE, string value = "", bool IsHyperLink = false)
        {
            IWebElement cell = null;
            int ColumnIndex = TableHeader.GetColumnIndex(columnNames.GetDescription(), ColumnIndex: 2);
            string ColumnCssSelector = "#resultTable > tbody > trCHILD > td:nth-child(" + ColumnIndex + ")";


            if (IsHyperLink)
                ColumnCssSelector = ColumnCssSelector + " > a";

            if (cellPosition.Equals(CellPosition.VALUE_BASE))
            {
                ColumnCssSelector = ColumnCssSelector.Replace("CHILD", "");
                ReadOnlyCollection<IWebElement> cells = this.webDriver.FindElements(By.CssSelector(ColumnCssSelector));
                foreach (var item in cells)
                {
                    if (item.GetTextValue().Trim().ToLower() == value.Trim().ToLower())
                    {
                        cell = item;
                        break;
                    }
                }
            }
            if (cellPosition.Equals(CellPosition.LAST))
            {
                ColumnCssSelector = ColumnCssSelector.Replace("CHILD", ":last-child");
                cell = webDriver.FindElement(By.CssSelector(ColumnCssSelector));
            }
            if (cellPosition.Equals(CellPosition.FIRST))
            {
                ColumnCssSelector = ColumnCssSelector.Replace("CHILD", ":first-child");
                cell = webDriver.FindElement(By.CssSelector(ColumnCssSelector));
            }
            return cell;
        }
    }
}
