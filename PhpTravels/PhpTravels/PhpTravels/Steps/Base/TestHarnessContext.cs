using OpenQA.Selenium;
using Selenium.Framework.Development.Kit.Configuration;
using Selenium.Framework.Development.Kit.Model.WebDriver;
using Selenium.Framework.Development.Kit.Model.Extensions;

namespace PhpTravels.Steps.Base
{
    public class TestHarnessContext
    {
        public static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        public IWebDriver webDriver { get; }
        public TestHarnessContext(IWebDriver webDriver)
        {
            this.webDriver = webDriver;
            this.webDriver.InitializeApplication();
        }

        public TestHarnessContext() : this(WebDriverFactory.GetWebDriverType(appConfigMember.Browser, appConfigMember.ExecutionType).webDriver)
        {
        }

    }
}
