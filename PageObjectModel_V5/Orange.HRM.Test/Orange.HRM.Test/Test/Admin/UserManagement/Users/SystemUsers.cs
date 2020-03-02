using NUnit.Framework;
using Orange.HRM.Test.Core;
using Orange.HRM.TestHarness.Page.Admin.UserManagement.Users;
using Orange.HRM.TestHarness.Page.Login;

namespace Orange.HRM.Test.Test.Admin.UserManagement.Users
{
    [TestFixture(Category = "SystemUsers")]
    public class SystemUsers : BaseTest
    {
        [SetUp]
        public void SetUp()
        {
            LoginPage.Instance.SetUserName(appConfigMember.UserName).SetPassword(appConfigMember.Password).ClickOnLogin();
            SystemUsersPage.Instance.WaitForSystemUsersPageLoad().NavigateToSystemUsersPage().WaitForSystemUsersPageLoad().CommonValidate().VerifyPageText(SystemUsersPage.Instance.pageLoadedText).VerifyPageUrl(SystemUsersPage.Instance.pageUrl);
        }

        [TestCase(TestName = "Validate User Role Filter", Author = "Anuj Jain", Category = "Smoke,Sanity,Regression")]
        public void VerifyeUserRoleFilter()
        {
            SystemUsersPage.Instance.SelectUserRole().ClickOnSearch().WaitForSystemUsersPageLoad().Validate().ValidateUserRoleFilter(SystemUsersPage.Instance.UserRole);
        }

        [TestCase(TestName = "Validate Status Filter", Author = "Anuj Jain", Category = "Smoke,Sanity,Regression")]
        public void VerifyeStatusFilter()
        {
            SystemUsersPage.Instance.SelectStatus().ClickOnSearch().WaitForSystemUsersPageLoad().Validate().ValidateStatusFilter(SystemUsersPage.Instance.Status);
        }

        [TearDown]
        public void TearDown()
        {
        }
    }
}
