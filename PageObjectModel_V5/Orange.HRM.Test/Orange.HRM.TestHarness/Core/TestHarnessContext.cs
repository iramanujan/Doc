using OpenQA.Selenium;
using Selenium.Framework.Development.Kit.Configuration;
using Selenium.Framework.Development.Kit.Model.WebDriver;
using Selenium.Framework.Development.Kit.Model.Extensions;
using Selenium.Framework.Development.Kit.Helper.Report;

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
