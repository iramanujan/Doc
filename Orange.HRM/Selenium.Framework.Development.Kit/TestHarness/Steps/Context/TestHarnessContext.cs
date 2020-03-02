using OpenQA.Selenium;
using Selenium.Framework.Development.Kit.Configuration;
using Selenium.Framework.Development.Kit.Model.WebDriver;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestHarness.Steps.Context
{
    public class TestHarnessContext
    {
        public static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        public IWebDriver webDriver { get; }
        public TestHarnessContext(IWebDriver webDriver)
        {
            this.webDriver = webDriver;
        }

        public TestHarnessContext() : this(WebDriverFactory.GetWebDriverType(appConfigMember.Browser, appConfigMember.ExecutionType).webDriver)
        {
        }

    }
}
