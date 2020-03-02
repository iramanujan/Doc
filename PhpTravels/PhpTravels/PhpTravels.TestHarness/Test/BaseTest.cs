using NUnit.Framework;
using NUnit.Framework.Interfaces;
using OpenQA.Selenium;
using PhpTravels.Steps.Base;
using PhpTravels.Steps.Login;
using Selenium.Framework.Development.Kit.Configuration;
using Selenium.Framework.Development.Kit.Helper.Report;

namespace PhpTravels.TestHarness.Test
{
    public class BaseTest
    {
        public LoginStep loginStep = null;
        public static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        public Report ObjReport => Report.ReportInstance;
        public IWebDriver webDriver => myContext.webDriver;
        protected TestHarnessContext myContext { get; set; }
        [SetUp]
        public void BaseTestSetUp()
        {
            ObjReport.CreateTest(TestContext.CurrentContext.Test.Name);
            myContext = TestHarnessContextHelper.CreateDefault();
            this.loginStep = new LoginStep(webDriver);
            loginStep.LoginPhpTravels(appConfigMember.UserName, appConfigMember.Password);
        }


        [TearDown]
        public void BaseTestTearDown()
        {
            if (TestContext.CurrentContext.Result.Outcome.Status == TestStatus.Failed)
            {
                ObjReport.Error(TestContext.CurrentContext.Test.MethodName);
            }
            if (TestContext.CurrentContext.Result.Outcome.Status == TestStatus.Warning)
            {
                ObjReport.Warning(TestContext.CurrentContext.Test.MethodName);
            }
            myContext.webDriver.Quit();
        }
    }
}
