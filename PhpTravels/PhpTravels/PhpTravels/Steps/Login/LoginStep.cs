using OpenQA.Selenium;
using PhpTravels.Pages.Login;
using PhpTravels.Steps.Base;

namespace PhpTravels.Steps.Login
{
    public class LoginStep : BaseSteps
    {
        private LoginPage loginPage = null;
        public LoginStep(IWebDriver webDriver) : base(webDriver)
        {
            this.loginPage = new LoginPage(webDriver);
        }

        public void LoginPhpTravels(string userName, string password)
        {
            ObjReport.Info("Verify Page Url and Text before Login");
            validation.VerifyPageText(loginPage.pageLoadedText);
            validation.VerifyPageUrl(loginPage.pageUrl);
            ObjReport.Info("Enter User Name and Password.");
            loginPage.EmailAddress.SendKeys(userName);
            loginPage.Password.SendKeys(password);
            loginPage.Login.Click();

        }
    }
}
