using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using Selenium.Framework.Development.Kit.Helper.Log;
using Selenium.Framework.Development.Kit.Model.Extensions;
using System.Text.RegularExpressions;
using System;
namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {

            //string qry = "SELECT Col1,Col2 FROM Person WHERE Col3 == 'ABC'";

            //var tablename = Regex.Match(qry, @"(?<=(?:FROM|JOIN)[\s(]+)(?>\w+)(?=[\s)]*(?:\s+(?:AS\s+)?\w+)?(?:$|\s+(?:WHERE|ON|(?:LEFT|RIGHT)?\s+(?:(?:OUTER|INNER)\s+)?JOIN)))", RegexOptions.IgnoreCase);
            //var where = Regex.Match(qry, @"(?<=(?:WHERE)[\s(]+)(?>\w+)", RegexOptions.IgnoreCase);

            //var input = "C# (pronounced see sharp, like the musical note C♯, but written with the number sign)[b] is a general-purpose, multi-paradigm programming language encompassing strong typing, lexically scoped, imperative, declarative, functional, generic, object-oriented (class-based), and component-oriented programming disciplines.[16] It was developed around 2000 by Microsoft as part of its .NET initiative, and later approved as an international standard by Ecma (ECMA-334) and ISO (ISO/IEC 23270:2018). Mono is the name of the free and open-source project to develop a compiler and runtime for the language. C# is one of the programming languages designed for the Common Language Infrastructure (CLI).";
            //var searchText = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            //foreach(char c in searchText.ToCharArray())
            //{
            //    var s = Regex.Matches(input, c.ToString(),RegexOptions.IgnoreCase).Count;
            //    Console.WriteLine(c+":"+s);
            //}
            IWebDriver webDriver = null;
            try
            {
                var service = ChromeDriverService.CreateDefaultService();
                service.LogPath = "D:\\chromedriver.log";
                service.EnableVerboseLogging = true;
                webDriver = new ChromeDriver(service, CreateDefaultChromeOptions());
                webDriver.GoToUrl(@"https://www.sqlservercentral.com/");
                webDriver.WaitForPage(300);
                webDriver.WaitForAjax(300);
                webDriver.Maximize();
                var Disclaimer = webDriver.FindElement(By.XPath("//*[@id='page']//a[text()='Staying Safe when Traveling']"));
                Disclaimer.ScrollPageVertically();
                var aa = Disclaimer.HasAttribute("hrefa");
            }
            catch(Exception e)
            {
                Logger.Error(e.Message);
            }
            finally
            {
                webDriver.QuitWindows();
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
