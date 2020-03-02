using AutomationCommonDevelopmentKit.Configuration;
using OpenQA.Selenium;
using SeleniumFrameworkDevelopmentKit.Model.Extensions;
using SeleniumFrameworkDevelopmentKit.Model.WebDriver;

namespace Orange.HRM.TestHarness.Core
{
    public static class TestHarnessContextHelper
    {

        public static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        public static IWebDriver webDriver = null;
        public static TestHarnessContext CreateDefault()
        {
            TestHarnessContext testHarnessContext = new TestHarnessContext();
            webDriver = testHarnessContext.webDriver;
            return testHarnessContext;
        }

        public static TestHarnessContext CreateLocalDriverContext()
        {
            var webDriver = WebDriverFactory.GetWebDriverType(appConfigMember.Browser, appConfigMember.ExecutionType).webDriver;
            return new TestHarnessContext(webDriver);
        }

        public static void StopDriver()
        {
            webDriver.QuitWebDriver();
        }
    }
}
