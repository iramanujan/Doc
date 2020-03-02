using AutomationCommonDevelopmentKit.Configuration;
using OpenQA.Selenium;
using OpenQA.Selenium.Support.UI;
using System;

namespace SeleniumFrameworkDevelopmentKit.WebDriverUtils.WebDriverWaits
{
    public class WebDriverWaiter
    {
        private static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();

        public static WebDriverWait Wait(IWebDriver webDriver, int numberOfSeconds)
        {
            return new WebDriverWait(webDriver, TimeSpan.FromSeconds(numberOfSeconds));
        }
        public static WebDriverWait Wait(IWebDriver webDriver, TimeSpan time)
        {
            return new WebDriverWait(webDriver, time);
        }

        public static WebDriverWait Wait(IWebDriver webDriver)
        {
            return new WebDriverWait(webDriver, TimeSpan.FromSeconds(appConfigMember.PageTimeout));
        }
    }
}
