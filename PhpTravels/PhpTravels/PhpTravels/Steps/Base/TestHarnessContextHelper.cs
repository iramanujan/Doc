using Selenium.Framework.Development.Kit.Configuration;
using Selenium.Framework.Development.Kit.Model.WebDriver;

namespace PhpTravels.Steps.Base
{
    public static class TestHarnessContextHelper
    {

        public static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();

        public static TestHarnessContext CreateDefault()
        {
            return new TestHarnessContext();
        }

        public static TestHarnessContext CreateLocalDriverContext()
        {
            var webDriver = WebDriverFactory.GetWebDriverType(appConfigMember.Browser, appConfigMember.ExecutionType).webDriver;
            return new TestHarnessContext(webDriver);
        }
    }
}
