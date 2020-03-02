using OpenQA.Selenium;

namespace WebAutomation.Common.WebDriveHandler
{
    public interface IWebDriverFactory
    {
        IWebDriver InitializeWebDriver();
    }
}
