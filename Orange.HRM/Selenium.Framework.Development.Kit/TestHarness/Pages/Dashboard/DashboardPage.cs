using OpenQA.Selenium;

namespace TestHarness.Pages.Dashboard
{
    public class DashboardPage
    {
        public IWebDriver webDriver = null;
        public DashboardPage(IWebDriver webDriver)
        {
            this.webDriver = webDriver;
        }
        internal readonly string pageSource = "Leave Entitlements and Usage Report";

        internal readonly string pageUrl = "/index.php/dashboard";
    }
}
