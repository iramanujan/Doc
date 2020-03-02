using OpenQA.Selenium;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PhpTravels.Pages.Login
{
    public class LoginPage
    {
        public IWebDriver webDriver = null;

        public LoginPage(IWebDriver webDriver)
        {
            this.webDriver = webDriver;
        }

        internal string pageLoadedText => "Selenium, Bots, or any automated softwares are not allowed to test here";
        internal string pageUrl => "/admin";

        internal IWebElement EmailAddress => webDriver.FindElement(By.CssSelector("form.form-signin.form-horizontal.wow.fadeIn.animated.animated input[name='email']"));
        internal IWebElement Password => webDriver.FindElement(By.CssSelector("form.form-signin.form-horizontal.wow.fadeIn.animated.animated input[name='password']"));
        internal IWebElement Login => webDriver.FindElement(By.CssSelector("form.form-signin.form-horizontal.wow.fadeIn.animated.animated > button[type='submit']"));

    }
}
