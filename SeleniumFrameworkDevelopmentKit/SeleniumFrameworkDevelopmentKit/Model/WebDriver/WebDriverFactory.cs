using AutomationCommonDevelopmentKit.Headspring;
using NUnit.Framework;
using OpenQA.Selenium;
using SeleniumFrameworkDevelopmentKit.Model.WebDriver.Chrome.Local;
using SeleniumFrameworkDevelopmentKit.Model.WebDriver.Firefox.Local;
using SeleniumFrameworkDevelopmentKit.Model.WebDriver.InternetExplorer.Local;
using System.Linq;
using static AutomationCommonDevelopmentKit.Configuration.AppConfigMember;

namespace SeleniumFrameworkDevelopmentKit.Model.WebDriver
{
    public abstract class WebDriverFactory : Enumeration<WebDriverFactory>
    {
        public abstract IWebDriver webDriver { get; }
        public static readonly WebDriverFactory LocalChromeDriver = new ChromeLocalType();
        public static readonly WebDriverFactory LocalInternetExplorerDriver = new IELocalType();
        public static readonly WebDriverFactory LocalFireFoxDriver = new FirefoxLocalType();
        public BrowserType BrowserType { get; set; }
        public WebDriverExecutionType ExecutionType { get; set; }

        protected WebDriverFactory(int value, BrowserType browserType, WebDriverExecutionType executionType) : base(value: value, displayName: browserType + executionType.ToString())
        {
            BrowserType = browserType;
            ExecutionType = executionType;
        }

        public static WebDriverFactory GetWebDriverType(BrowserType browserType, WebDriverExecutionType executionType)
        {
            var targetWebDriverType =GetAll().FirstOrDefault(wd => wd.BrowserType == browserType && wd.ExecutionType == executionType);
            Assert.IsNotNull(targetWebDriverType, $"WebDriverType with properties BrowserType='{browserType}' ExecutionType={executionType} not found");
            return targetWebDriverType;
        }
        private class ChromeLocalType : WebDriverFactory
        {
            public ChromeLocalType() : base(1, BrowserType.Chrome, WebDriverExecutionType.Local)
            {
            }
            public override IWebDriver webDriver => new LocalChromeDriver().InitializeWebDriver();
        }
        private class IELocalType : WebDriverFactory
        {
            public IELocalType() : base(2, BrowserType.IE, WebDriverExecutionType.Local)
            {
            }
            public override IWebDriver webDriver => new LocalInternetExplorerDriver().InitializeWebDriver();
        }
        private class FirefoxLocalType : WebDriverFactory
        {
            public FirefoxLocalType() : base(3, BrowserType.Firefox, WebDriverExecutionType.Local)
            {
            }
            public override IWebDriver webDriver => new LocalFireFoxDriver().InitializeWebDriver();
        }
    }
}
