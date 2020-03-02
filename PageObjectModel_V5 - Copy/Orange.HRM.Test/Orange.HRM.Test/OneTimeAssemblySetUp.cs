using AutomationCommonDevelopmentKit.Configuration;
using AutomationCommonDevelopmentKit.Report;
using AutomationCommonDevelopmentKit.Utils;
using NUnit.Framework;

namespace Orange.HRM.Test
{
    [SetUpFixture]
    class OneTimeAssemblySetUp
    {
        public static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        public Report ObjReport => Report.ReportInstance;

        [OneTimeSetUp]
        public void OneTimeSetup()
        {
            ProcessUtils.KillAllBrowser();
            ObjReport.ExtentReportsSetup();
        }


        [OneTimeTearDown]
        public void OneTimeTearDown()
        {
            ProcessUtils.KillAllBrowser();
            ObjReport.ExtentReportsTearDown();
        }

    }
}
