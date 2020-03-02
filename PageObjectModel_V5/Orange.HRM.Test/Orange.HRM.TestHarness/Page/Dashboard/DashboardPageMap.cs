using OpenQA.Selenium;
using Orange.HRM.TestHarness.Core;

namespace Orange.HRM.TestHarness.Page.Dashboard
{
    public class DashboardPageMap : BasePageElementMap
    {
        public IWebElement Welcome => webDriver.FindElement(By.CssSelector("#welcome"));

    }
}
