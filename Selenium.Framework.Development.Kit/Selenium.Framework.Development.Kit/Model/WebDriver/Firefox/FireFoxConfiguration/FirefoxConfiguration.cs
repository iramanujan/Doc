using OpenQA.Selenium.Firefox;
using Selenium.Framework.Development.Kit.Configuration;
using Selenium.Framework.Development.Kit.Helper.Utils;
using System;

namespace Selenium.Framework.Development.Kit.Model.WebDriver.Firefox.FireFoxConfiguration
{
    public class FirefoxConfiguration
    {
        private static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        internal static FirefoxProfile GetFirefoxProfile()
        {
            FirefoxProfile profile;
            try
            {
                profile = appConfigMember.ProfileName == null ? new FirefoxProfile() : new FirefoxProfile(appConfigMember.ProfileName);
                profile.SetPreference("browser.download.folderList", 2);
                profile.SetPreference("browser.download.dir", appConfigMember.RootDownloadLocation);
                profile.SetPreference("browser.download.manager.alertOnEXEOpen", false);
                profile.SetPreference("browser.helperApps.neverAsk.saveToDisk", "text/plain, application/octet-stream");
                if (appConfigMember.NoCache)
                {
                    profile.SetPreference("browser.cache.disk.enable", false);
                    profile.SetPreference("browser.cache.memory.enable", false);
                    profile.SetPreference("browser.cache.offline.enable", false);
                }
                profile.SetPreference("intl.accept_languages", appConfigMember.Localization.ToString());
            }
            catch (Exception)
            {
                profile = new FirefoxProfile();
            }
            return profile;
        }

        internal static FirefoxDriverService GetFirefoxDriverService()
        {
            return FirefoxDriverService.CreateDefaultService(FileUtils.GetCurrentlyExecutingDirectory());
        }

        internal static FirefoxOptions GetFirefoxOptions()
        {
            FirefoxOptions firefoxOptions = new FirefoxOptions();
            firefoxOptions.SetPreference(FirefoxDriver.ProfileCapabilityName, FirefoxConfiguration.GetFirefoxProfile().ToBase64String());
            firefoxOptions.ToCapabilities();
            firefoxOptions.LogLevel = FirefoxDriverLogLevel.Trace;
            return firefoxOptions;
        }
    }
}
