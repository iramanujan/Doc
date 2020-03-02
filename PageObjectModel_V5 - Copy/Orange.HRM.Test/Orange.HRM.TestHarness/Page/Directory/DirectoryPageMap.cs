using OpenQA.Selenium;
using Orange.HRM.TestHarness.Core;
using System.Collections.ObjectModel;

namespace Orange.HRM.TestHarness.Page.Directory
{
    public class DirectoryPageMap : BasePageElementMap
    {
        public IWebElement Directory => webDriver.FindElement(By.CssSelector("#menu_directory_viewDirectory"));
        public IWebElement Search => webDriver.FindElement(By.CssSelector("#searchBtn"));
        public IWebElement ReSet => webDriver.FindElement(By.CssSelector("#resetBtn"));
        public IWebElement EmployeeName => webDriver.FindElement(By.CssSelector("#searchDirectory_emp_name_empName"));
        public IWebElement JobTitle => webDriver.FindElement(By.CssSelector("#searchDirectory_job_title"));
        public IWebElement Location => webDriver.FindElement(By.CssSelector("#searchDirectory_location"));

        public ReadOnlyCollection<IWebElement> JobTitleTable => webDriver.FindElements(By.CssSelector("#resultTable > tbody > tr  li:nth-child(2)"));

        public ReadOnlyCollection<IWebElement> LocationTable => webDriver.FindElements(By.CssSelector("#resultTable > tbody > tr  li:nth-child(4)"));

        public ReadOnlyCollection<IWebElement> NameTable => webDriver.FindElements(By.CssSelector("#resultTable  ul > li > b"));

        public IWebElement EmployeeNameList(string empName)
        {
            By ele = By.XPath("//strong[contains(text(),'" + empName + "')]/parent::li");
            return webDriver.FindElement(ele);
        }

        public IWebElement JobTitleRow(int row)
        {
            By by = By.CssSelector("#resultTable > tbody > tr:nth-child(" + row + ") ul > li:nth-child(2)");
            return webDriver.FindElement(by);
        }

        public IWebElement LocationRow(int row)
        {
            By by = By.CssSelector("#resultTable > tbody > tr:nth-child(" + row + ") ul > li:nth-child(4)");
            return webDriver.FindElement(by);
        }

        public IWebElement NameRow(int row)
        {
            By by = By.CssSelector("#resultTable > tbody > tr:nth-child(" + row + ") ul > li:nth-child(1) > b");
            return webDriver.FindElement(by);
        }
    }
}
