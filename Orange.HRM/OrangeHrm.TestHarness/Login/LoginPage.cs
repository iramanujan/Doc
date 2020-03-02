using NUnit.Framework;
using Selenium.Framework.Development.Kit.Helper.Report;
using System;

namespace OrangeHrm.TestHarness.Login
{
    [TestFixture]
    public class LoginPage
    {
        private Report ObjReport => Report.ReportInstance;
        [SetUp]
        public void SetUp()
        {
            ObjReport.CreateTest("Test1","dude");
        }


        [Test]
        public void Test1()
        {
            ObjReport.Pass("Pass");
        }

        [Test]
        public void Test2()
        {
            ObjReport.Error("Fail");
        }

        [TearDown]
        public void TearDown()
        {

        }

    }
}
