using OpenQA.Selenium;
using Selenium.Framework.Development.Kit.Helper.Wait;
using System;
using TestHarness.Pages.Qualifications;
using static TestHarness.Pages.Qualifications.EducationPage;
using Selenium.Framework.Development.Kit.Model.Extensions;
namespace TestHarness.Steps.Qualifications
{
    public class EducationStep : BaseSteps
    {
        EducationPage educationPage = null;

        public EducationStep(IWebDriver webDriver) : base(webDriver)
        {
            educationPage = new EducationPage(webDriver);
        }

        public void NavigateToEducation()
        {
            webDriver.WaitForAjax();
            webDriver.WaitForPage();
            educationPage.Admin.Click();
            educationPage.Qualifications.Click();
            Waiter.Wait(TimeSpan.FromSeconds(5));
            educationPage.Education.Click();
            validation.VerifyPageText(educationPage.pageSource);
            validation.VerifyPageUrl(educationPage.pageUrl);
        }

        public void AddEducation(string education)
        {
            educationPage.Add.Click();
            educationPage.Level.SendKeys(education);
            educationPage.Save.Click();
            var actualEducation = educationPage.GetEducation("Level", CellPosition.VALUE_BASE, education, IsHyperLink: true).Text;
            validation.VerifyText(education, actualEducation, "Validate Education Level Added Successfully.");
        }

        public void DeleteEducation(string education)
        {
            educationPage.Delete.Click();
        }
    }
}
