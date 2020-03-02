using NUnit.Framework;
using Selenium.Framework.Development.Kit.Configuration;
using Selenium.Framework.Development.Kit.Helper.Report;
using Selenium.Framework.Development.Kit.Helper.Utils;


namespace Test
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
