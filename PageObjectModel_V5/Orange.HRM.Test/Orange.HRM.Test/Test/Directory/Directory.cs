using NUnit.Framework;
using Orange.HRM.Test.Core;
using Orange.HRM.TestHarness.Page.Dashboard;
using Orange.HRM.TestHarness.Page.Directory;
using Orange.HRM.TestHarness.Page.Login;

namespace Orange.HRM.Test.Test.Directory
{
    [TestFixture]
    public class Directory : BaseTest
    {
        [SetUp]
        public void SetUp()
        {
            LoginPage.Instance.SetUserName(appConfigMember.UserName).SetPassword(appConfigMember.Password).ClickOnLogin();
            DashboardPage.Instance.Validate().VerifyLoginUserName();
            DirectoryPage.Instance.WaitForPageLoad().NavigateToDirectoryPage().WaitForPageLoad();
        }

        [TestCase(TestName = "Validate Job Title Filter", Author = "Anuj Jain", Category = "Smoke,Sanity,Regression")]
        public void VerifyeJobTitleFilter()
        {
            DirectoryPage.Instance.SelectJobTitle().ClickOnSearch().WaitForPageLoad().Validate().ValidateJobTitleFilter(DirectoryPage.Instance.JobTitle);
        }

        [TestCase(TestName = "Validate Location Filter", Author = "Anuj Jain", Category = "Smoke,Sanity,Regression")]
        public void VerifyeLocationFilter()
        {
            DirectoryPage.Instance.SelectLocation().ClickOnSearch().WaitForPageLoad().Validate().ValidateLocationFilter(DirectoryPage.Instance.Location);
        }

        [TestCase(TestName = "Validate Name Filter", Author = "Anuj Jain", Category = "Smoke,Sanity,Regression")]
        public void VerifyeNameFilter()
        {
            DirectoryPage.Instance.SelectEmplyeeName().ClickOnSearch().WaitForPageLoad().Validate().ValidateNameFilter(DirectoryPage.Instance.EmpName);
        }

        [TestCase(TestName = "Validate Name, Location and Job Title Filter", Author = "Anuj Jain", Category = "Smoke,Sanity,Regression")]
        public void VerifyeAllFilter()
        {
            DirectoryPage.Instance.SelectEmplyeeNameJobTitleAndLocation().ClickOnSearch().WaitForPageLoad();
            DirectoryPage.Instance.Validate().ValidateNameFilter(DirectoryPage.Instance.EmpName);
            DirectoryPage.Instance.Validate().ValidateLocationFilter(DirectoryPage.Instance.Location);
            DirectoryPage.Instance.Validate().ValidateJobTitleFilter(DirectoryPage.Instance.JobTitle);
        }

        [TestCase(TestName = "Validate Reset For Name", Author = "Anuj Jain", Category = "Smoke,Sanity,Regression")]
        public void VerifyeReSetNameFilter()
        {
            DirectoryPage.Instance.GetRecordCount().SelectEmplyeeName().ClickOnSearch().WaitForPageLoad().ClickOnReSet().WaitForPageLoad().Validate().ValidateReSet(DirectoryPage.Instance.RowCount);
        }

        [TestCase(TestName = "Validate Reset For Location", Author = "Anuj Jain", Category = "Smoke,Sanity,Regression")]
        public void VerifyeReSetLocationFilter()
        {
            DirectoryPage.Instance.GetRecordCount().SelectLocation().ClickOnSearch().WaitForPageLoad().ClickOnReSet().WaitForPageLoad().Validate().ValidateReSet(DirectoryPage.Instance.RowCount);
        }

        [TestCase(TestName = "Validate Reset For Job Title", Author = "Anuj Jain", Category = "Smoke,Sanity,Regression")]
        public void VerifyeReSetJobTitleFilter()
        {
            DirectoryPage.Instance.GetRecordCount().SelectJobTitle().ClickOnSearch().WaitForPageLoad().ClickOnReSet().WaitForPageLoad().Validate().ValidateReSet(DirectoryPage.Instance.RowCount);
        }

        [TestCase(TestName = "Validate Reset For Name, Location and Job Title Filter", Author = "Anuj Jain", Category = "Smoke,Sanity,Regression")]
        public void VerifyeReSetWithAllFilter()
        {
            DirectoryPage.Instance.GetRecordCount().SelectEmplyeeNameJobTitleAndLocation().ClickOnSearch().WaitForPageLoad().ClickOnReSet().WaitForPageLoad().Validate().ValidateReSet(DirectoryPage.Instance.RowCount);
        }

        [TearDown]
        public void TearDown()
        {
        }
    }
}