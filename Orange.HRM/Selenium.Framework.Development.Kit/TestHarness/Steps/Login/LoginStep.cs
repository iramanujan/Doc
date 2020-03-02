using NUnit.Framework;
using OpenQA.Selenium;
using Selenium.Framework.Development.Kit.Helper.Attributes;
using Selenium.Framework.Development.Kit.Helper.Log;
using Selenium.Framework.Development.Kit.Helper.Wait;
using System;
using TestHarness.Pages.Dashboard;
using TestHarness.Pages.Login;
using DescriptionAttribute = System.ComponentModel.DescriptionAttribute;

namespace TestHarness.Steps.Login
{
    public class LoginStep : BaseSteps
    {
        private LoginPage ObjLoginPage = null;
        private DashboardPage dashboardPage = null;

        public LoginStep(IWebDriver webDriver):base (webDriver)
        {
            this.ObjLoginPage = new LoginPage(webDriver);
            dashboardPage = new DashboardPage(webDriver);
        }

        public enum ErrorMessageType
        {
            [Description("Username cannot be empty")]
            UserNameEmpty = 0,

            [Description("Password cannot be empty")]
            PasswordEmpty = 1,

            [Description("Invalid credentials")]
            InvalidCredentials = 2
        }

        public void LoginOrangeHRM(string userName, string password)
        {
            ObjReport.Info("Verify Page Url and Text before Login");
            validation.VerifyPageText(ObjLoginPage.pageSource);
            validation.VerifyPageUrl(ObjLoginPage.pageUrl);
            ObjReport.Info("Enter User Name and Password.");
            ObjLoginPage.UserName.SendKeys(userName);
            ObjLoginPage.Password.SendKeys(password);
            ObjLoginPage.Login.Submit();
            ObjReport.Info("Verify Page Url and Text after Login");
            ObjReport.Info("Verify Page Url and Text after Login");
            validation.VerifyPageText(dashboardPage.pageSource);
            validation.VerifyPageUrl(dashboardPage.pageUrl);
        }

        private void WaitForErrorMessage()
        {
            Waiter.SpinWaitEnsureSatisfied(() =>
            {
                Logger.Info($"Wait For Error Message....");
                try
                {
                    var msg = ObjLoginPage.ErrorMessage;
                    ObjReport.Info("Error Message", msg, true);
                }
                catch (Exception e)
                {
                    ObjReport.Error("Error Message Did Not Show After 5 Sec.", e.Message, true);
                }
                return true;
            }, TimeSpan.FromSeconds(5), TimeSpan.FromMilliseconds(200), $"Could not Set clipboard to text ");
        }

        public void VerifyErrorMessage(ErrorMessageType errorMessageType, string userName, string password)
        {
            ObjReport.Info("Verify Page Url and Text before Login");
            validation.VerifyPageText(ObjLoginPage.pageSource);
            validation.VerifyPageUrl(ObjLoginPage.pageUrl);
            if (errorMessageType.Equals(ErrorMessageType.UserNameEmpty))
            {
                ObjLoginPage.Password.SendKeys(password);
                ObjLoginPage.Login.Submit();
                WaitForErrorMessage();
                Assert.AreEqual(ErrorMessageType.UserNameEmpty.GetDescription(), ObjLoginPage.ErrorMessage, "Error Message is not matched.");
                var info = "Expected Error Msg: " + ErrorMessageType.UserNameEmpty.GetDescription() + "\t" + "Actual Error Msg: " + ObjLoginPage.ErrorMessage;
                ObjReport.Pass("Verify User Empty Error Message", info);
            }
            if (errorMessageType.Equals(ErrorMessageType.PasswordEmpty))
            {
                Logger.Info("Verify Password Empty Error Message");
                ObjLoginPage.UserName.SendKeys(userName);
                ObjLoginPage.Login.Submit();
                WaitForErrorMessage();
                Assert.AreEqual(ErrorMessageType.PasswordEmpty.GetDescription(), ObjLoginPage.ErrorMessage, "Error Message is not matched.");
                var info = "Expected Error Msg: " + ErrorMessageType.UserNameEmpty.GetDescription() + "\t" + "Actual Error Msg: " + ObjLoginPage.ErrorMessage;
                ObjReport.Pass("Verify Password Empty Error Message", info);
            }
            if (errorMessageType.Equals(ErrorMessageType.InvalidCredentials))
            {
                Logger.Info("Verify Invalid Credentials Error Message");
                ObjLoginPage.UserName.SendKeys(userName);
                ObjLoginPage.Password.SendKeys(password);
                ObjLoginPage.Login.Submit();
                WaitForErrorMessage();
                Assert.AreEqual(ErrorMessageType.InvalidCredentials.GetDescription(), ObjLoginPage.ErrorMessage, "Error Message is not matched.");
                var info = "Expected Error Msg: " + ErrorMessageType.UserNameEmpty.GetDescription() + "\t" + "Actual Error Msg: " + ObjLoginPage.ErrorMessage;
                ObjReport.Pass("Verify Invalid Credentials Error Message", info);
            }
            ObjReport.Info("Verify Page Url and Text After Login");
            validation.VerifyPageText(ObjLoginPage.pageSource);
            validation.VerifyPageUrl(ObjLoginPage.pageUrl);
        }

    }
}