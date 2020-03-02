using Orange.HRM.TestHarness.Core;

namespace Orange.HRM.TestHarness.Page.Login
{
    public class LoginPage : BasePageSingleton<LoginPage, LoginPageMap, LoginPageValidator>
    {
        public readonly string pageSource = "( Username : Admin | Password : admin123 )";

        public readonly string pageUrl = @"Https://Opensource-Demo.Orangehrmlive.Com/";

        public LoginPage()
        {
        }
        public LoginPage SetUserName(string userName)
        {
            ObjReport.Info("Enter User Name "+ userName);
            Map.UserName.SendKeys(userName);
            return this;
        }
        public LoginPage SetPassword(string password)
        {
            ObjReport.Info("Enter Password " + password);
            Map.Password.SendKeys(password);
            return this;
        }
        public LoginPage ClickOnLogin()
        {
            ObjReport.Info("Click On Login Button.");
            Map.Login.Submit();
            return this;
        }
    
    }
}
