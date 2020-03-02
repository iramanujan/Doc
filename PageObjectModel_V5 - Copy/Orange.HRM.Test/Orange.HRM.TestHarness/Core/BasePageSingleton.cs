using AutomationCommonDevelopmentKit.Configuration;
using AutomationCommonDevelopmentKit.Report;
using OpenQA.Selenium;
using Orange.HRM.TestHarness.GenericValidation;
using SeleniumFrameworkDevelopmentKit.Model.Extensions;

namespace Orange.HRM.TestHarness.Core
{
    public abstract class BasePageSingleton<TS, TM> : ThreadSafeLazyBaseSingleton<TS> where TM : BasePageElementMap, new() where TS : BasePageSingleton<TS, TM>, new()
    {
        internal static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        internal Report ObjReport => Report.ReportInstance;
        protected IWebDriver webDriver => TestHarnessContextHelper.webDriver;
        public BasePageSingleton()
        {
        }

        public TM Map
        {
            get
            {
                return new TM();
            }
        }

        internal void WaitTillPageLoad()
        {
            webDriver.WaitForAjax();
            webDriver.WaitForPage();
        }
    }

    public abstract class BasePageSingleton<TS, TM, TV> : BasePageSingleton<TS, TM> where TM : BasePageElementMap, new() where TV : BasePageValidator<TM>, new() where TS : BasePageSingleton<TS, TM, TV>, new()
    {
        public TV Validate()
        {
            return new TV();
        }

        public GenericValidate CommonValidate()
        {
            return new GenericValidate();
        }
        internal void WaitTillPageLoad()
        {
            webDriver.WaitForAjax();
            webDriver.WaitForPage();
        }
    }
}
