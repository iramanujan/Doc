using OpenQA.Selenium;

namespace Orange.HRM.TestHarness.Core
{
    public class BasePageElementMap
    { 
        protected IWebDriver webDriver;

        public BasePageElementMap()
        {
            webDriver = TestHarnessContextHelper.webDriver;
        }

        public void SwitchToDefault()
        {
            webDriver.SwitchTo().DefaultContent();
        }
    }
}
