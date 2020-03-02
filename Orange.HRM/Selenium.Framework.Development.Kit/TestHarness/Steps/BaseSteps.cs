using OpenQA.Selenium;
using Selenium.Framework.Development.Kit.Configuration;
using Selenium.Framework.Development.Kit.Helper.Report;
using TestHarness.Steps.CommonValidation;
using TestHarness.Steps.Login;

namespace TestHarness.Steps
{
    public class BaseSteps
    {
        public IWebDriver webDriver { get; }
        public static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        public Report ObjReport => Report.ReportInstance;
        public Validation validation = null;
        public LoginStep loginStep = null;


        public BaseSteps(IWebDriver webDriver)
        {
            this.webDriver = webDriver;
            this.validation = new Validation(this.webDriver);
        }

    }
}
