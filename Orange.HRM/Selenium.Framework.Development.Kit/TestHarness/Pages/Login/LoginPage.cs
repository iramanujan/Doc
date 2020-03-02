using OpenQA.Selenium;
using System;


namespace TestHarness.Pages.Login
{
    public class LoginPage
    {
        public IWebDriver webDriver = null;

        public LoginPage(IWebDriver webDriver)
        {
            this.webDriver = webDriver;
        }

        internal readonly string pageSource = "( Username : Admin | Password : admin123 )";

        internal readonly string pageUrl = @"Https://Opensource-Demo.Orangehrmlive.Com/";
        internal IWebElement UserName => webDriver.FindElement(By.CssSelector("#txtUsername"));
        internal IWebElement Password => webDriver.FindElement(By.CssSelector("#txtPassword"));
        internal IWebElement Login => webDriver.FindElement(By.CssSelector("#btnLogin"));
        internal IWebElement Message => webDriver.FindElement(By.CssSelector("#spanMessage"));
        internal String ErrorMessage => Message.Text.Trim();
    }
}
