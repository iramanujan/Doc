using OpenQA.Selenium;
using Orange.HRM.TestHarness.Core;
using System;

namespace Orange.HRM.TestHarness.Page.Login
{
    public class LoginPageMap : BasePageElementMap
    {
        public IWebElement UserName => webDriver.FindElement(By.CssSelector("#txtUsername"));
        public IWebElement Password => webDriver.FindElement(By.CssSelector("#txtPassword"));
        public IWebElement Login => webDriver.FindElement(By.CssSelector("#btnLogin"));
        public IWebElement Message => webDriver.FindElement(By.CssSelector("#spanMessage"));
        public String ErrorMessage => Message.Text.Trim();
    }
}
