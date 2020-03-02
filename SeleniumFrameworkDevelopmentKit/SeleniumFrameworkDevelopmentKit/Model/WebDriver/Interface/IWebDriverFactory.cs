using OpenQA.Selenium;

namespace SeleniumFrameworkDevelopmentKit.Model.WebDriver.Interface
{
    public interface IWebDriverFactory
    {
        //void BeforeWebDriverSetupSetps();
        IWebDriver InitializeWebDriver();
        //void AfterWebDriverSetupSetps();
    }
}
