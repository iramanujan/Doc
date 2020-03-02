using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using Selenium.Framework.Development.Kit.Configuration;
using Selenium.Framework.Development.Kit.Helper.Utils;

namespace Selenium.Framework.Development.Kit.Model.WebDriver.Chrome.ChromeConfiguration
{
    class ChromeDriverConfiguration
    {
        private static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        private static ChromeDriverService chromeDriverService = null;
        public static ChromeOptions GetChromeOptions()
        {
            var options = new ChromeOptions();

            options.AddUserProfilePreference("safebrowsing.enabled", true);
            options.AddUserProfilePreference("download.default_directory", appConfigMember.RootDownloadLocation);
            options.AddArguments("--test-type");
            options.AddArguments("--no-sandbox");
            options.AddArgument("--start-maximized");
            options.AddArgument("--ignore-certificate-errors");
            options.AddArgument("--disable-popup-blocking");
            options.AddArgument("--incognito");
            options.AddArgument("--enable-precise-memory-info");
            options.AddArgument("--disable-default-apps");
            options.AddArgument("test-type=browser");
            options.AddArgument("disable-infobars");
            options.AddArguments($"--lang={appConfigMember.Localization.ToString()}");
            options.AddExcludedArgument("enable-automation");
            options.AddAdditionalCapability("useAutomationExtension", false);

            options.AddArgument("verbose");
            options.AddArgument("log-path="+ appConfigMember.ChromeLogFileLocation);

            options.SetLoggingPreference(LogType.Browser, LogLevel.All);
            if (appConfigMember.NoCache)
                options.AddArguments("--incognito");
            return options;
        }

        public static ChromeDriverService GetChromeDriverService()
        {
            chromeDriverService = ChromeDriverService.CreateDefaultService(FileUtils.GetCurrentlyExecutingDirectory());
            if (chromeDriverService.IsRunning)
            {
                chromeDriverService.Dispose();
            }
            chromeDriverService.Start();
            chromeDriverService.LogPath = appConfigMember.ChromeLogFileLocation;
            chromeDriverService.EnableVerboseLogging = true;

            return chromeDriverService;
        }
    }
}
