using AutomationCommonDevelopmentKit.Configuration;
using AutomationCommonDevelopmentKit.Report;
using NUnit.Framework;
using NUnit.Framework.Interfaces;
using Orange.HRM.TestHarness.Core;

namespace Orange.HRM.Test.Core
{
    public class BaseTest
    {
        public static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        public Report ObjReport => Report.ReportInstance;
        protected TestHarnessContext myContext { get; set; }
        [SetUp]
        public void BaseTestSetUp()
        {
            ObjReport.CreateTest(TestContext.CurrentContext.Test.Name);
            myContext = TestHarnessContextHelper.CreateDefault();
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
            ObjReport.ExtentReportsTearDown();
            TestHarnessContextHelper.StopDriver();
        }
    }
}
