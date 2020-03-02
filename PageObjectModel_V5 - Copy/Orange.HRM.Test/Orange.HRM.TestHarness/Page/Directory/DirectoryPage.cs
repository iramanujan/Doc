using AutomationCommonDevelopmentKit.Extensions;
using AutomationCommonDevelopmentKit.Utils;
using AutomationCommonDevelopmentKit.Wait;
using Orange.HRM.TestHarness.Core;
using SeleniumFrameworkDevelopmentKit.Model.Extensions;
using System;
using System.Linq;

namespace Orange.HRM.TestHarness.Page.Directory
{
    public class DirectoryPage : BasePageSingleton<DirectoryPage, DirectoryPageMap, DirectoryPageValidator>
    {
        public readonly string pageSource = "Leave Entitlements and Usage Report";
        public readonly string pageUrl = "/directory/viewDirectory";
        public string JobTitle = null;
        public string Location = null;
        public string EmpName = null;
        public int RowCount;

        public DirectoryPage()
        {

        }

        public DirectoryPage NavigateToDirectoryPage()
        {
            Map.Directory.Click();
            return this;
        }

        public DirectoryPage SelectLocation()
        {
            this.Location = Map.Location.GetOptions().RandomElement();
            Map.Location.SelectByText(this.Location);
            ObjReport.Info("Select Location From Dropdown " + this.Location.Trim(), IsScreenshot: true);
            return this;
        }

        public DirectoryPage SelectJobTitle()
        {
            this.JobTitle = Map.JobTitle.GetOptions().RandomElement();
            Map.JobTitle.SelectByText(this.JobTitle);
            ObjReport.Info("Select Job Title From Dropdown " + this.JobTitle, IsScreenshot: true);
            return this;
        }

        public DirectoryPage ClickOnSearch()
        {
            ObjReport.Info("Click On Search Button");
            Map.Search.Click();
            return this;
        }

        public DirectoryPage ClickOnReSet()
        {
            ObjReport.Info("Click On Reset Button");
            Map.ReSet.Click();
            return this;
        }

        public DirectoryPage EnterEmplyeeName(string empName)
        {
            ObjReport.Info("Enter Emplyee Name " + empName);
            Map.EmployeeName.SendKeys(empName);
            return this;
        }

        public DirectoryPage SelectEmplyeeName()
        {
            var names = Map.NameTable.Select(item => item.GetTextValue()).ToList();
            this.EmpName = names.RandomElement();
            Map.EmployeeName.SendKeys(this.EmpName);
            Waiter.Wait(TimeSpan.FromSeconds(1));
            Map.EmployeeNameList(this.EmpName).Click(); ;
            ObjReport.Info("Select Emplyee Name from List " + this.EmpName, IsScreenshot: true);
            return this;
        }

        public DirectoryPage SelectEmplyeeNameJobTitleAndLocation()
        {
            int rowNumber = RandomUtils.RandomNumeric(2, Map.NameTable.Count + 1);

            this.EmpName = Map.NameRow(rowNumber).GetTextValue();
            this.JobTitle = Map.JobTitleRow(rowNumber).GetTextValue();
            this.Location = Map.LocationRow(rowNumber).GetTextValue();
            var location = Map.Location.GetOptions().Find(t => t.Contains(this.Location));
            Waiter.Wait(TimeSpan.FromSeconds(5));
            Map.EmployeeName.SendKeys(this.EmpName);
            Waiter.Wait(TimeSpan.FromSeconds(1));
            Map.EmployeeNameList(this.EmpName).Click(); ;
            ObjReport.Info("Select Emplyee Name from List " + this.EmpName, IsScreenshot: true);
            ///////////////////////////////////////////////////////////////////////
            Waiter.Wait(TimeSpan.FromSeconds(1));
            Map.Location.SelectByText(location);
            ObjReport.Info("Select Location From Dropdown " + this.Location.Trim(), IsScreenshot: true);
            ///////////////////////////////////////////////////////////////////////
            Waiter.Wait(TimeSpan.FromSeconds(1));
            Map.JobTitle.SelectByText(this.JobTitle);
            ObjReport.Info("Select Job Title From Dropdown " + this.JobTitle, IsScreenshot: true);
            return this;
        }

        public DirectoryPage WaitForPageLoad()
        {
            WaitTillPageLoad();
            return this;
        }

        public DirectoryPage GetRecordCount()
        {
            this.RowCount = Map.NameTable.Count;
            return this;
        }

    }
}