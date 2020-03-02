using NUnit.Framework;
using Orange.HRM.Test.Core;
using Orange.HRM.TestHarness.Page.Dashboard;
using Orange.HRM.TestHarness.Page.Login;
using Selenium.Framework.Development.Kit.Helper.NUnit.Attributtes;

namespace Orange.HRM.Test.Test.Login
{
    [TestFixture(Category = "Login")]
    public class Login : BaseTest
    {
        [SetUp]
        public void SetUp()
        {
        }

        [QTestCase("Admin", "admin123", Author = "Anuj Jain", TestName = "Validate Login With Valid User.", Category = "Smoke,Sanity,Regression", Ticket = "AUT001", Description = "Validate Login With Valid User.", IssueId = "AUT007", IssueLink = "")]
        public void ValidateLogin(string userName, string password)
        {
            LoginPage.Instance.CommonValidate().VerifyPageText(LoginPage.Instance.pageSource).VerifyPageUrl(LoginPage.Instance.pageUrl);
            LoginPage.Instance.SetUserName(userName).SetPassword(password).ClickOnLogin();
            LoginPage.Instance.CommonValidate().VerifyPageText(DashboardPage.Instance.pageSource).VerifyPageUrl(DashboardPage.Instance.pageUrl);
            DashboardPage.Instance.Validate().VerifyLoginUserName();
        }

        [QTestCase("AutoQA", "AutoQA", TestName = "Validate Invalid Credentials Error Message.", Author = "Anuj Jain", Category = "Smoke,Sanity,Regression", Ticket = "AUT002", Description = "Validate Invalid Credentials Error Message.")]
        public void ValidateInvalidCredentials(string userName, string password)
        {
            LoginPage.Instance.CommonValidate().VerifyPageText(LoginPage.Instance.pageSource).VerifyPageUrl(LoginPage.Instance.pageUrl);
            LoginPage.Instance.Validate().VerifyInvalidCredentials(userName, password);
            LoginPage.Instance.CommonValidate().VerifyPageText(LoginPage.Instance.pageSource).VerifyPageUrl(LoginPage.Instance.pageUrl);
        }

        [QTestCase("AutoQA", TestName = "Validate Password Cannot Be Empty Error Message.", Author = "Anuj Jain", Category = "Smoke,Sanity,Regression", Ticket = "AUT003", Description = "Validate Password Cannot Be Empty Error Message.")]
        public void ValidatePasswordCanNotBeEmpty(string userName)
        {
            LoginPage.Instance.CommonValidate().VerifyPageText(LoginPage.Instance.pageSource).VerifyPageUrl(LoginPage.Instance.pageUrl);
            LoginPage.Instance.Validate().VerifyPasswordCanNotBeEmpty(userName);
            LoginPage.Instance.CommonValidate().VerifyPageText(LoginPage.Instance.pageSource).VerifyPageUrl(LoginPage.Instance.pageUrl);
        }

        [QTestCase("AutoQA", TestName = "Validate Username Cannot Be Empty Error Message.", Author = "Anuj Jain", Category = "Smoke,Sanity,Regression", Ticket = "AUT004", Description = "Validate Username Cannot Be Empty Error Message")]
        public void ValidateUserNameCanNotBeEmpty(string password)
        {
            LoginPage.Instance.CommonValidate().VerifyPageText(LoginPage.Instance.pageSource).VerifyPageUrl(LoginPage.Instance.pageUrl);
            LoginPage.Instance.Validate().VerifyUserNameCanNotBeEmpty(password);
            LoginPage.Instance.CommonValidate().VerifyPageText(LoginPage.Instance.pageSource).VerifyPageUrl(LoginPage.Instance.pageUrl);
        }

        [TearDown]
        public void TearDown()
        {
        }

    }
}