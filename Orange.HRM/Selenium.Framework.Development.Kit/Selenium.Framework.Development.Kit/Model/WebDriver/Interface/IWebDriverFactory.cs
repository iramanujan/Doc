using OpenQA.Selenium;

namespace Selenium.Framework.Development.Kit.Model.WebDriver.Interface
{
    public interface IWebDriverFactory
    {
        //void BeforeWebDriverSetupSetps();
        IWebDriver InitializeWebDriver();
        //void AfterWebDriverSetupSetps();
    }
}
