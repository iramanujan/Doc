using NUnit.Framework;
using OpenQA.Selenium;
using Selenium.Framework.Development.Kit.Configuration;
using Selenium.Framework.Development.Kit.Helper.Report;
using TestHarness.Steps.Context;

namespace Test
{
    public class BaseTest
    {
        public static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        public Report ObjReport => Report.ReportInstance;
        public IWebDriver webDriver => myContext.webDriver;
        protected TestHarnessContext myContext { get; set; }
    }
}
