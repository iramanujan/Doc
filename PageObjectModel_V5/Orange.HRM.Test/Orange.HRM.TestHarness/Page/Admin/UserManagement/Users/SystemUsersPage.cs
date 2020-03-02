using Orange.HRM.TestHarness.Core;
using Selenium.Framework.Development.Kit.Helper.Extensions;
using Selenium.Framework.Development.Kit.Model.Extensions;

namespace Orange.HRM.TestHarness.Page.Admin.UserManagement.Users
{
    public class SystemUsersPage : BasePageSingleton<SystemUsersPage, SystemUsersPageMap, SystemUsersPageValidator>
    {
        public readonly string pageLoadedText = "Leave Entitlements and Usage Report";
        public readonly string pageUrl = "/index.php/admin/viewSystemUsers";
        public string UserRole = null;
        public string Status = null;

        public SystemUsersPage NavigateToSystemUsersPage()
        {
            ObjReport.Info("Navigate To System Users Page.");
            Map.Admin.Click();
            Map.UserManagement.Click();
            Map.User.Click();
            return this;
        }

        public SystemUsersPage WaitForSystemUsersPageLoad()
        {
            WaitTillPageLoad();
            return this;
        }

        public SystemUsersPage SelectUserRole()
        {
            this.UserRole = Map.UserRole.GetOptions().RandomElement();
            Map.UserRole.SelectByText(this.UserRole);
            ObjReport.Info("Select Job Title From Dropdown " + this.UserRole, IsScreenshot: true);
            return this;
        }

        public SystemUsersPage SelectStatus()
        {
            this.Status = Map.Status.GetOptions().RandomElement();
            Map.Status.SelectByText(this.Status);
            ObjReport.Info("Select Job Title From Dropdown " + this.Status, IsScreenshot: true);
            return this;
        }

        public SystemUsersPage ClickOnSearch()
        {
            ObjReport.Info("Click On Search Button");
            Map.Search.Click();
            return this;
        }

    }
}
