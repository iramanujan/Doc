using NUnit.Framework;
using Selenium.Framework.Development.Kit.Helper.Report;
using System;

namespace OrangeHrm.TestHarness
{
    [SetUpFixture]
    class OneTimeAssemblySetUp
    {
        public Report ObjReport => Report.ReportInstance;

        [OneTimeSetUp]
        public void OneTimeSetup()
        {
            ObjReport.ExtentReportsSetup();
        }

        [OneTimeTearDown]
        public void OneTimeTearDown()
        {
            ObjReport.ExtentReportsTearDown();
        }

    }
}
