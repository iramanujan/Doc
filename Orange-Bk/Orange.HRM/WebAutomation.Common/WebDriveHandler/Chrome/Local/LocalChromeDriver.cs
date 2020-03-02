using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System;
using WebAutomation.Common.GenericHelper.Utils;
using WebAutomation.Common.WebDriveHandler.Base;
using WebDriverHelper.DriverFactory.Chrome.Options;

namespace WebAutomation.Common.WebDriveHandler.Chrome.Local
{
    public class LocalChromeDriver : BaseLocalDriverFactory, IWebDriverFactory
    {
        private IWebDriver webDriver = null;
        private ChromeOptions chromeOptions = null;
        private ChromeDriverService chromeDriverService = null;

        private void BeforeWebDriverSetupSetps()
        {
            this.chromeOptions = ChromeDriverOptions.CreateDefaultChromeOptions();
            this.chromeDriverService = ChromeDriverService.CreateDefaultService(FileUtils.GetCurrentlyExecutingDirectory());
        }

        public IWebDriver InitializeWebDriver()
        {
            BeforeWebDriverSetupSetps();
            webDriver = new ChromeDriver(chromeDriverService, chromeOptions, TimeSpan.FromSeconds(toolConfigMember.CommandTimeout));
            return this.webDriver;
        }
    }
}
