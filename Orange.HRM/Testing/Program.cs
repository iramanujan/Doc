using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using Selenium.Framework.Development.Kit.Helper.Log;
using Selenium.Framework.Development.Kit.Model.Extensions;
using System.Text.RegularExpressions;
using System;

namespace Testing
{
    class Program
    {
        static void Main(string[] args)
        {
            IWebDriver webDriver = null;
            try
            {
                var service = ChromeDriverService.CreateDefaultService();
                service.LogPath = "D:\\chromedriver.log";
                service.EnableVerboseLogging = true;
                webDriver = new ChromeDriver(service, CreateDefaultChromeOptions());
                webDriver.KillAllBrowser();
                webDriver.GoToUrl(@"https://www.sqlservercentral.com/");
                webDriver.WaitForPage(300);
                webDriver.WaitForAjax(300);
                webDriver.Maximize();
                var Disclaimer = webDriver.FindElement(By.XPath("//*[@id='page']//a[text()='Staying Safe when Traveling']"));
                Disclaimer.ScrollPageVertically();

            }
            catch (Exception e)
            {
                Logger.Error(e.Message);
            }
            finally
            {
                webDriver.QuitWebDriver();
            }
        }

        public static ChromeOptions CreateDefaultChromeOptions()
        {
            var options = new ChromeOptions();

            options.AddUserProfilePreference("safebrowsing.enabled", true);
            options.AddUserProfilePreference("download.default_directory", @"C:\Automation\Download\");

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
            options.AddArguments("--incognito");
            options.AddArguments("--lang=es");
            options.AddExcludedArgument("enable-automation");
            options.AddAdditionalCapability("useAutomationExtension", false);
            options.SetLoggingPreference(LogType.Browser, LogLevel.All);
            return options;
        }

        public static void getJavaScriptConsoleLogs(IWebDriver webDriver)
        {
            Selenium.Framework.Development.Kit.Helper.Log.Logger.Info("====================================================");
            Logger.Info("Browser Console logs Starts:-");
            var logEntries = webDriver.Manage().Logs.GetLog(LogType.Browser);
            foreach (var logEntry in logEntries)
            {
                Logger.Info(logEntry.Timestamp + " - " + logEntry.Message);
            }
            Logger.Info("Browser Console logs Ends:-");
            Logger.Info("====================================================");
        }
    }
}
