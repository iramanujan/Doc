using OpenQA.Selenium;
using Selenium.Framework.Development.Kit.Helper.Report;
using Selenium.Framework.Development.Kit.Helper.Wait;
using Selenium.Framework.Development.Kit.Model.Extensions;
using System;

namespace TestHarness.Steps.CommonValidation
{
    public class Validation
    {
        private Report ObjReport => Report.ReportInstance;
        private IWebDriver webDriver = null;
        public Validation(IWebDriver webDriver)
        {
            this.webDriver = webDriver;
        }

        public void VerifyPageText(string pageSource)
        {
            Waiter.SpinWaitEnsureSatisfied(
                () => webDriver.PageSource.ToLower().Contains(pageSource.ToLower()),
                TimeSpan.FromSeconds(60),
                TimeSpan.FromSeconds(3),
                $"Page Source Match : Page Source '{webDriver.GetDecodedUrl()}' contain \"{pageSource}\".",
                $"Page Source Mismatch : Page Source '{webDriver.GetDecodedUrl()}' doesn't contain \"{pageSource}\"."
             );

        }

        public void VerifyPageUrl(string pageUrl)
        {
            Waiter.SpinWaitEnsureSatisfied(
                  () => webDriver.Url.ToLower().Contains(pageUrl.ToLower()),
                  TimeSpan.FromSeconds(60),
                  TimeSpan.FromSeconds(3),
                  $"URL Match : Url '{webDriver.Url}' contain \"{pageUrl}\".",
                  $"URL Mismatch : Url '{webDriver.Url}' doesn't contain \"{pageUrl}\"."
               );
        }

        public void VerifyText(string expectedText, string actuslText, string info)
        {
            string msg = "Actual Text: " + actuslText + "\n Expected Text: " + expectedText;
            if (expectedText.Trim().ToLower().Equals(actuslText.Trim().ToLower()))
            {
                ObjReport.Pass(info, msg);
            }
            else
            {
                ObjReport.Error(info, msg);
            }

        }

    }
}
