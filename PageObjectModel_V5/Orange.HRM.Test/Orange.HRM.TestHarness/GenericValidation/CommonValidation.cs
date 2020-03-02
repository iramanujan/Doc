using OpenQA.Selenium;
using Orange.HRM.TestHarness.Core;
using Selenium.Framework.Development.Kit.Helper.Report;
using Selenium.Framework.Development.Kit.Helper.Wait;
using Selenium.Framework.Development.Kit.Model.Extensions;
using System;

namespace Orange.HRM.TestHarness.GenericValidation
{
    public class GenericValidate
    {
        private Report ObjReport => Report.ReportInstance;
        protected IWebDriver webDriver;

        public GenericValidate()
        {
            webDriver = TestHarnessContextHelper.webDriver;
        }

        public GenericValidate VerifyPageText(string pageSource)
        {
            Waiter.SpinWaitEnsureSatisfied(
                () => webDriver.PageSource.ToLower().Contains(pageSource.ToLower()),
                TimeSpan.FromSeconds(60),
                TimeSpan.FromSeconds(3),
                $"Page Source Match : Page Source '{webDriver.GetDecodedUrl()}' contain \"{pageSource}\".",
                $"Page Source Mismatch : Page Source '{webDriver.GetDecodedUrl()}' doesn't contain \"{pageSource}\"."
             );
            return this;
        }

        public GenericValidate VerifyPageUrl(string pageUrl)
        {
            Waiter.SpinWaitEnsureSatisfied(
                  () => webDriver.Url.ToLower().Contains(pageUrl.ToLower()),
                  TimeSpan.FromSeconds(60),
                  TimeSpan.FromSeconds(3),
                  $"URL Match : Url '{webDriver.Url}' contain \"{pageUrl}\".",
                  $"URL Mismatch : Url '{webDriver.Url}' doesn't contain \"{pageUrl}\"."
               );
            return this;
        }

        public GenericValidate VerifyText(string expectedText, string actuslText, string info)
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
            return this;
        }
    }
}
