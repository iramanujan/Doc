using AutomationCommonDevelopmentKit.Configuration;
using AutomationCommonDevelopmentKit.Utils;
using OpenQA.Selenium.IE;
using OpenQA.Selenium.Remote;
using System;

namespace SeleniumFrameworkDevelopmentKit.Model.WebDriver.InternetExplorer.IEConfiguration
{
    class InternetExplorerConfiguration
    {
        private static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        internal static InternetExplorerDriverService GetInternetExplorerDriverService()
        {
            var path = FileUtils.GetCurrentlyExecutingDirectory();
            var internetExplorerDriverService = InternetExplorerDriverService.CreateDefaultService(path, "IEDriverServer.exe");
            internetExplorerDriverService.HideCommandPromptWindow = false;
            internetExplorerDriverService.LoggingLevel = InternetExplorerDriverLogLevel.Trace;
            internetExplorerDriverService.LogFile = appConfigMember.IELogFileLocation;
            return internetExplorerDriverService;
        }

        internal static InternetExplorerOptions GetInternetExplorerOptions()
        {
            InternetExplorerOptions options = new InternetExplorerOptions();
            options.AddAdditionalCapability(CapabilityType.AcceptSslCertificates, true);
            options.AddAdditionalCapability(CapabilityType.IsJavaScriptEnabled, true);
            options.IntroduceInstabilityByIgnoringProtectedModeSettings = true;
            options.ElementScrollBehavior = InternetExplorerElementScrollBehavior.Bottom;
            options.IgnoreZoomLevel = true;
            options.RequireWindowFocus = true;
            options.EnsureCleanSession = true;
            options.EnableNativeEvents = false;
            options.PageLoadStrategy = (OpenQA.Selenium.PageLoadStrategy)Enum.Parse(typeof(OpenQA.Selenium.PageLoadStrategy), appConfigMember.PageLoadStrategy);
            options.AddAdditionalCapability("InternetExplorerDriver.FORCE_CREATE_PROCESS", true);
            return options;
        }
    }
}
