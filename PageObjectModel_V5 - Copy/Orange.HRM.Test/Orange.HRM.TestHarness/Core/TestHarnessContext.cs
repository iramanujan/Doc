using AutomationCommonDevelopmentKit.Configuration;
using AutomationCommonDevelopmentKit.Report;
using OpenQA.Selenium;
using SeleniumFrameworkDevelopmentKit.Model.Extensions;
using SeleniumFrameworkDevelopmentKit.Model.WebDriver;

namespace Orange.HRM.TestHarness.Core
{
    public class TestHarnessContext
    {
        public static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        private Report ObjReport => Report.ReportInstance;
        public IWebDriver webDriver { get; }
        public TestHarnessContext(IWebDriver webDriver)
        {
            this.webDriver = webDriver;
            ObjReport.Info("Initialize Application. " + appConfigMember.Url);
            this.webDriver.InitializeApplication();
        }

        public TestHarnessContext() : this(WebDriverFactory.GetWebDriverType(appConfigMember.Browser, appConfigMember.ExecutionType).webDriver)
        {
        }

    }
}
