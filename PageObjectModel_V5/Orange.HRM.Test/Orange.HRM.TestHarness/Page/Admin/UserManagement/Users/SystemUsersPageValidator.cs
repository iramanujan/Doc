using FluentAssertions;
using OpenQA.Selenium;
using Orange.HRM.TestHarness.Core;
using Selenium.Framework.Development.Kit.Model.Extensions;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Orange.HRM.TestHarness.Page.Admin.UserManagement.Users
{
    public class SystemUsersPageValidator : BasePageValidator<SystemUsersPageMap>
    {
        public void ValidateUserRoleFilter(string userRole)
        {
            bool IsFound = false;
            if (userRole.Trim().ToLower() == "All".ToLower().Trim())
            {
                var actualCount = Map.RowsUserRole.Count;
                Map.ReSet.Click();
                var expectedCount = Map.RowsUserRole.Count;
                if (expectedCount == actualCount)
                {
                    ObjReport.Pass("Validate User Role Filter.", "Where User Role = " + userRole);
                }
                else
                {
                    ObjReport.Error("Validate User Role Filter. Where User Role = " + userRole, "Expected Row Count: " + expectedCount + "Actual Row Count: " + actualCount);
                }
            }
            else if (Map.RowsUserRole.Count == 0)
            {
                ObjReport.Warning("No Record Found For User Role", "Where User Role = " + userRole);
            }
            else
            {
                int index = 1;
                foreach (IWebElement webElement in Map.RowsUserRole)
                {
                    if (webElement.GetTextValue().Trim().ToLower() == userRole.Trim().ToLower())
                        IsFound = true;
                    else
                    {
                        IsFound = false;
                        ObjReport.Error("Validate User Role Filter. Where User Role = " + userRole, "Different Record Found At: Position " + index + "; Value: " + webElement.GetTextValue().Trim().ToLower());
                        IsFound.Should().BeTrue();
                    }
                    index = index + 1;
                }

                if (IsFound)
                    ObjReport.Pass("Validate User Role Filter.", "Where User Role = " + userRole);
            }
        }

        public void ValidateStatusFilter(string status)
        {
            bool IsFound = false;
            if (status.Trim().ToLower() == "All".ToLower().Trim())
            {
                var actualCount = Map.RowsStatus.Count;
                Map.ReSet.Click();
                var expectedCount = Map.RowsStatus.Count;
                if (expectedCount == actualCount)
                {
                    ObjReport.Pass("Validate Status Filter.", "Where Status = " + status);
                }
                else
                {
                    ObjReport.Error("Validate Status Filter. Where Status = " + status, "Expected Row Count: " + expectedCount + "Actual Row Count: " + actualCount);
                }
            }
            else if (Map.RowsStatus.Count == 0)
            {
                ObjReport.Warning("No Record Found For Status", "Where Status = " + status);
            }
            else
            {
                int index = 1;
                foreach (IWebElement webElement in Map.RowsStatus)
                {
                    if (webElement.GetTextValue().Trim().ToLower() == status.Trim().ToLower())
                        IsFound = true;
                    else
                    {
                        IsFound = false;
                        ObjReport.Error("Validate Status Filter. Where Status = " + status, "Different Record Found At: Position " + index + "; Value: " + webElement.GetTextValue().Trim().ToLower());
                        IsFound.Should().BeTrue();
                    }
                    index = index + 1;
                }

                if (IsFound)
                    ObjReport.Pass("Validate Status Filter.", "Where User Role = " + status);
            }
        }

    }
}
