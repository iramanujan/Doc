using AutomationCommonDevelopmentKit.Configuration;
using AutomationCommonDevelopmentKit.Log;
using AutomationCommonDevelopmentKit.Utils;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using SeleniumFrameworkDevelopmentKit.Model.WebDriver.Chrome.ChromeConfiguration;
using SeleniumFrameworkDevelopmentKit.Model.WebDriver.Interface;
using System;
using System.IO;

namespace SeleniumFrameworkDevelopmentKit.Model.WebDriver.Chrome.Local
{
    public class LocalChromeDriver : IWebDriverFactory
    {
        private static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        private IWebDriver webDriver = null;
        private ChromeOptions chromeOptions = null;
        private ChromeDriverService chromeDriverService = null;

        public void BeforeWebDriverSetupSetps()
        {
            this.chromeOptions = ChromeDriverConfiguration.GetChromeOptions();
            this.chromeDriverService = ChromeDriverConfiguration.GetChromeDriverService();
        }

        public IWebDriver InitializeWebDriver()
        {
            try
            {
                BeforeWebDriverSetupSetps();
                this.webDriver = new ChromeDriver(chromeDriverService, chromeOptions, TimeSpan.FromSeconds(appConfigMember.CommandTimeout));
                AfterWebDriverSetupSetps();
            }
            catch (Exception ObjException)
            {
                Logger.Error("An Exception Occurred While Creating ChromeDriver Object." + ObjException.Message);
            }
            return this.webDriver;
        }

        public void AfterWebDriverSetupSetps()
        {
            if (!Directory.Exists(appConfigMember.RootDownloadLocation))
            {
                StepsExecutor.ExecuteSafely(() => Directory.CreateDirectory(appConfigMember.RootDownloadLocation));
            }
            if (!Directory.Exists(appConfigMember.RootUploadLocation))
            {
                StepsExecutor.ExecuteSafely(() => Directory.CreateDirectory(appConfigMember.RootUploadLocation));
            }
            if (!Directory.Exists(appConfigMember.ChromeLogFileLocation))
            {
                StepsExecutor.ExecuteSafely(() => Directory.CreateDirectory(Path.GetDirectoryName(appConfigMember.ChromeLogFileLocation)));
            }
        }

    }
}
