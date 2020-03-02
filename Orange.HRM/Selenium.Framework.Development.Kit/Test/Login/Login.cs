using NUnit.Framework;
using NUnit.Framework.Interfaces;
using Selenium.Framework.Development.Kit.Helper.Utils;
using Selenium.Framework.Development.Kit.Model.Extensions;
using TestHarness.Steps.Context;
using TestHarness.Steps.Login;

namespace Test.Login
{
    [TestFixture]
    public class Login : BaseTest
    {
        private LoginStep loginStep = null;
        [SetUp]
        public void SetUp()
        {
            ObjReport.CreateTest(TestContext.CurrentContext.Test.Name);
            myContext = TestHarnessContextHelper.CreateDefault();
            webDriver.InitializeApplication();
            this.loginStep = new LoginStep(webDriver);
            
        }

        [TestCase("Admin", "admin123", TestName = "Validate Login With Valid User.", Author = "Anuj Jain")]
        public void ValidateLogin(string username, string password)
        {
            loginStep.LoginOrangeHRM(username, password);
        }

        [TestCase(LoginStep.ErrorMessageType.UserNameEmpty, "", "admin123", TestName = "Validate Error Message Username cannot be empty.", Author = "Anuj Jain")]
        [TestCase(LoginStep.ErrorMessageType.PasswordEmpty, "Admin", "", TestName = "Validate Error Message Password cannot be empty.", Author = "Anuj Jain")]
        [TestCase(LoginStep.ErrorMessageType.PasswordEmpty, "admin123", "Admin", TestName = "Validate Error Message Invalid credentials.", Author = "Anuj Jain")]
        public void ValidateErrorMessage(LoginStep.ErrorMessageType errorMessageType, string userName, string password)
        {
            loginStep.VerifyErrorMessage(errorMessageType, userName, password);
        }


        [TearDown]
        public void OrangeHrmBaseTestOneTimeTearDown()
        {
            if (TestContext.CurrentContext.Result.Outcome.Status == TestStatus.Failed)
            {
                ObjReport.Error(TestContext.CurrentContext.Test.MethodName);
            }
            if (TestContext.CurrentContext.Result.Outcome.Status == TestStatus.Warning)
            {
                ObjReport.Warning(TestContext.CurrentContext.Test.MethodName);
            }
            webDriver.QuitWebDriver();
        }
    }
}
