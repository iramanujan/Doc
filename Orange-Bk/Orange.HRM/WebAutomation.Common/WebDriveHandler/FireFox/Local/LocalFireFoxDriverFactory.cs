using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;
using System;
using WebAutomation.Common.GenericHelper.Utils;
using WebAutomation.Common.WebDriveHandler.Base;
using WebAutomation.Common.WebDriveHandler.FireFox.Profile;

namespace WebAutomation.Common.WebDriveHandler.FireFox.Local
{
    public class LocalFireFoxDriverFactory : BaseLocalDriverFactory, IWebDriverFactory
    {

        private FirefoxOptions firefoxOptions = null;
        private FirefoxDriverService firefoxDriverService = null;
        private FirefoxProfile firefoxProfile = null;

        protected void BeforeWebDriverSetupSetps()
        {
            firefoxProfile = FireFoxDriverProfile.CreateProfile();
            firefoxDriverService = FirefoxDriverService.CreateDefaultService(FileUtils.GetCurrentlyExecutingDirectory());
            firefoxOptions = new FirefoxOptions();
            firefoxOptions.Profile = firefoxProfile;
            firefoxOptions.LogLevel = FirefoxDriverLogLevel.Info;
        }

        public IWebDriver InitializeWebDriver()
        {
            BeforeWebDriverSetupSetps();
            var firefoxDriver = new FirefoxDriver(firefoxDriverService, firefoxOptions, TimeSpan.FromSeconds(30));
            return firefoxDriver;
        }
    }
}
