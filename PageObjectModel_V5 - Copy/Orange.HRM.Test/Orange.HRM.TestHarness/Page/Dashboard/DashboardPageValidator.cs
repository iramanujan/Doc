using FluentAssertions;
using Orange.HRM.TestHarness.Core;
using SeleniumFrameworkDevelopmentKit.Model.Extensions;

namespace Orange.HRM.TestHarness.Page.Dashboard
{
    public class DashboardPageValidator : BasePageValidator<DashboardPageMap>
    {
        public void VerifyLoginUserName()
        {
            var actualUserName = Map.Welcome.GetTextValue();
            var expectedUserName = DashboardPage.Instance.welcomeText;
            actualUserName.ToLower().Trim().Should().Be(expectedUserName.ToLower().Trim());
            var info = "Expected Login User: " + expectedUserName + "\t" + "Actual Login User: " + actualUserName;
            ObjReport.Pass("User Login Successfully.", info);
        }
    }
}
