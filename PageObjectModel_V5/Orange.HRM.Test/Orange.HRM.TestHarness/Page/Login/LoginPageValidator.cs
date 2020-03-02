using FluentAssertions;
using Orange.HRM.TestHarness.Core;
using Orange.HRM.TestHarness.Data;
using Selenium.Framework.Development.Kit.Helper.Attributes;

namespace Orange.HRM.TestHarness.Page.Login
{
    public class LoginPageValidator : BasePageValidator<LoginPageMap>
    {
        public void VerifyUserNameCanNotBeEmpty(string password)
        {
            ObjReport.Info("Enter Password " + password);
            Map.Password.SendKeys(password);
            ObjReport.Info("Click On Login Button.");
            Map.Login.Submit();
            Map.ErrorMessage.Should().Be(ErrorMessageType.UserNameEmpty.GetDescription());
            var info = "Expected Error Msg: " + ErrorMessageType.UserNameEmpty.GetDescription() + "\t" + "Actual Error Msg: " + Map.ErrorMessage;
            ObjReport.Pass("Verify User Empty Error Message", info);
        }

        public void VerifyPasswordCanNotBeEmpty(string userName)
        {
            ObjReport.Info("Enter User Name " + userName);
            Map.UserName.SendKeys(userName);
            ObjReport.Info("Click On Login Button.");
            Map.Login.Submit();
            Map.ErrorMessage.Should().Be(ErrorMessageType.PasswordEmpty.GetDescription());
            var info = "Expected Error Msg: " + ErrorMessageType.PasswordEmpty.GetDescription() + "\t" + "Actual Error Msg: " + Map.ErrorMessage;
            ObjReport.Pass("Verify Password Empty Error Message", info);
        }

        public void VerifyInvalidCredentials(string userName, string password)
        {
            ObjReport.Info("Enter User Name " + userName);
            Map.UserName.SendKeys(userName);
            ObjReport.Info("Enter Password " + password);
            Map.Password.SendKeys(password);
            ObjReport.Info("Click On Login Button.");
            Map.Login.Submit();
            Map.ErrorMessage.Should().Be(ErrorMessageType.InvalidCredentials.GetDescription());
            var info = "Expected Error Msg: " + ErrorMessageType.InvalidCredentials.GetDescription() + "\t" + "Actual Error Msg: " + Map.ErrorMessage;
            ObjReport.Pass("Verify Invalid Credentials Error Message", info);
        }
    }
}
