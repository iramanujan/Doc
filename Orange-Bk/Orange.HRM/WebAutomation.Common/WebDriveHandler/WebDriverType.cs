using NUnit.Framework;
using System.Linq;
using WebAutomation.Common.GenericHelper.Headspring;
using WebAutomation.Common.WebDriveHandler.Chrome.Local;
using WebAutomation.Common.WebDriveHandler.FireFox.Local;
using WebDriverHelper.DriverFactory.Chrome.Local;
using WebDriverHelper.DriverFactory.Chrome.Remote;
using WebDriverHelper.DriverFactory.FireFox.Local;
using WebDriverHelper.DriverFactory.FireFox.Remote;


using static WebAutomation.Common.AppConfigHandler.ToolConfigMember;

namespace WebAutomation.Common.WebDriveHandler
{
    public abstract class WebDriverType : Enumeration<WebDriverType>
    {
        public static readonly WebDriverType ChromeLocal = new ChromeLocalType();
        public static readonly WebDriverType FirefoxLocal = new FirefoxLocalType();

        protected WebDriverType(int value,BrowserType browserType, WebDriverExecutionType executionType) : base(value: value, displayName: browserType + executionType.ToString())
        {
            BrowserType = browserType;
            ExecutionType = executionType;
        }

        public BrowserType BrowserType { get; set; }

        public WebDriverExecutionType ExecutionType { get; set; }

        public BrowserLocalization Localization { get; set; }

        public static WebDriverType Get(BrowserType browserType, WebDriverExecutionType executionType)
        {
            var targetWebDriverType =
                GetAll().FirstOrDefault(wd => wd.BrowserType == browserType && wd.ExecutionType == executionType);
            Assert.IsNotNull(targetWebDriverType, $"WebDriverType with properties BrowserType='{browserType}' ExecutionType={executionType} not found");
            return targetWebDriverType;
        }

        public abstract IWebDriverFactory Factory { get; }

        private class ChromeLocalType : WebDriverType
        {
            public ChromeLocalType() : base(1, BrowserType.Chrome, WebDriverExecutionType.Local)
            {
            }
            public override IWebDriverFactory Factory => new LocalChromeDriver();
        }

        private class FirefoxLocalType : WebDriverType
        {
            public FirefoxLocalType() : base(5, BrowserType.Firefox, WebDriverExecutionType.Local)
            {
            }
            public override IWebDriverFactory Factory => new LocalFireFoxDriverFactory();
        }
    }
}
