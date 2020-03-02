using Orange.HRM.TestHarness.Core;

namespace Orange.HRM.TestHarness.Page.Dashboard
{
    public class DashboardPage : BasePageSingleton<DashboardPage, DashboardPageMap, DashboardPageValidator>
    {
        public readonly string pageSource = "Leave Entitlements and Usage Report";

        public readonly string pageUrl = "/index.php/dashboard";

        public readonly string welcomeText = "Welcome "+ appConfigMember.UserName;
    }
}
