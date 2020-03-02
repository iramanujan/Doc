using OpenQA.Selenium;
using Selenium.Framework.Development.Kit.Configuration;
using Selenium.Framework.Development.Kit.Helper.Report;

namespace PhpTravels.Steps.Base
{
    public class BaseSteps
    {
        public IWebDriver webDriver { get; }
        public static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        public Report ObjReport => Report.ReportInstance;
        public Validation validation = null;

        public BaseSteps(IWebDriver webDriver)
        {
            this.webDriver = webDriver;
            this.validation = new Validation(this.webDriver);
        }

    }
}
