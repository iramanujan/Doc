using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;
using Selenium.Framework.Development.Kit.Configuration;
using Selenium.Framework.Development.Kit.Helper.Log;
using Selenium.Framework.Development.Kit.Helper.Utils;
using Selenium.Framework.Development.Kit.Model.WebDriver.Firefox.FireFoxConfiguration;
using Selenium.Framework.Development.Kit.Model.WebDriver.Interface;
using System;
using System.IO;

namespace Selenium.Framework.Development.Kit.Model.WebDriver.Firefox.Local
{
    public class LocalFireFoxDriver : IWebDriverFactory
    {
        private static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        private IWebDriver webDriver = null;
        private FirefoxOptions firefoxOptions = null;
        private FirefoxDriverService firefoxDriverService = null;
        private FirefoxProfile firefoxProfile = null;

        public void BeforeWebDriverSetupSetps()
        {
            this.firefoxProfile = FirefoxConfiguration.GetFirefoxProfile();
            this.firefoxDriverService = FirefoxConfiguration.GetFirefoxDriverService();
            this.firefoxOptions = FirefoxConfiguration.GetFirefoxOptions();

        }

        public IWebDriver InitializeWebDriver()
        {
            try
            {
                BeforeWebDriverSetupSetps();
                this.webDriver = new FirefoxDriver(firefoxDriverService, firefoxOptions, TimeSpan.FromSeconds(appConfigMember.CommandTimeout));
                AfterWebDriverSetupSetps();
            }
            catch (Exception ObjException)
            {
                Logger.Error("An Exception Occurred While Creating FirefoxDriver Object." + ObjException.Message);
            }
            return this.webDriver;
        }

        public void AfterWebDriverSetupSetps()
        {
            if (Directory.Exists(appConfigMember.RootDownloadLocation))
            {
                StepsExecutor.ExecuteSafely(() => Directory.Delete(appConfigMember.RootDownloadLocation, true));
                StepsExecutor.ExecuteSafely(() => Directory.CreateDirectory(appConfigMember.RootDownloadLocation));
            }
            if (Directory.Exists(appConfigMember.RootUploadLocation))
            {
                StepsExecutor.ExecuteSafely(() => Directory.Delete(appConfigMember.RootUploadLocation, true));
                StepsExecutor.ExecuteSafely(() => Directory.CreateDirectory(appConfigMember.RootUploadLocation));
            }
        }
    }
}
