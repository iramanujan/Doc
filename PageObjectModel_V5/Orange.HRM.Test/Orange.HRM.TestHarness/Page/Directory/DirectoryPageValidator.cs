using FluentAssertions;
using OpenQA.Selenium;
using Orange.HRM.TestHarness.Core;
using Selenium.Framework.Development.Kit.Model.Extensions;
using System.Linq;

namespace Orange.HRM.TestHarness.Page.Directory
{
    public class DirectoryPageValidator : BasePageValidator<DirectoryPageMap>
    {

        public void ValidateJobTitleFilter(string jobTitle)
        {
            bool IsFound = false;
            if (jobTitle.Trim().ToLower() == "All".ToLower().Trim())
            {
                var actualCount = Map.JobTitleTable.Count;
                Map.ReSet.Click();
                var expectedCount = Map.JobTitleTable.Count;
                if (expectedCount == actualCount)
                {
                    ObjReport.Pass("Validate Job Title Filter.", "Where Job Title = " + jobTitle);
                }
                else
                {
                    ObjReport.Error("Validate Job Title Filter.Where Job Title = " + jobTitle, "Expected Row Count: " + expectedCount + "Actual Row Count: " + actualCount);
                }
            }
            else if (Map.JobTitleTable.Count == 0)
            {
                ObjReport.Warning("No Record Found For Job Title", "Where Job Title = " + jobTitle);
            }
            else
            {
                int index = 1;
                foreach (IWebElement webElement in Map.JobTitleTable)
                {
                    if (webElement.GetTextValue().Trim().ToLower() == jobTitle.Trim().ToLower())
                        IsFound = true;
                    else
                    {
                        IsFound = false;
                        ObjReport.Error("Validate Job Title Filter. Where Job Title = " + jobTitle, "Different Record Found At: Position " + index + "; Value: " + webElement.GetTextValue().Trim().ToLower());
                        IsFound.Should().BeTrue();
                    }
                    index = index + 1;
                }

                if (IsFound) ObjReport.Pass("Validate Job Title Filter.", "Where Job Title = " + jobTitle);

            }
        }

        public void ValidateLocationFilter(string location)
        {
            bool IsFound = false;
            if (location.Trim().ToLower().Contains("All".ToLower().Trim()))
            {
                var actualCount = Map.JobTitleTable.Count;
                Map.ReSet.Click();
                var expectedCount = Map.JobTitleTable.Count;
                if (expectedCount == actualCount)
                {
                    ObjReport.Pass("Validate Job Title Filter.", "Where Job Title = " + location);
                }
                else
                {
                    ObjReport.Error("Validate Job Title Filter.Where Job Title = " + location, "Expected Row Count: " + expectedCount + "Actual Row Count: " + actualCount);
                }
            }
            else if (location.Trim().ToLower().Contains("Canada".ToLower().Trim()))
            {
                int index = 1;
                foreach (IWebElement webElement in Map.LocationTable)
                {
                    if (webElement.GetTextValue().Trim().ToLower().Contains("Canadian Development Center".Trim().ToLower()))
                        IsFound = true;
                    else
                    {
                        IsFound = false;
                        ObjReport.Error("Validate Location  Filter.", "Different Record Found At: Position " + index + "; Value: " + webElement.GetTextValue().Trim().ToLower());
                        IsFound.Should().BeTrue();
                    }
                    index = index + 1;
                }

                if (IsFound) ObjReport.Pass("Validate Location Filter.", "Where Location = " + location);
            }
            else if (location.Trim().ToLower().Contains("United States".ToLower().Trim()))
            {
                int index = 1;
                string[] arr = { "Texas R&D", "New York Sales Office", "HQ - CA" };

                foreach (IWebElement webElement in Map.LocationTable)
                {
                    if (arr.Any((webElement.GetTextValue().Trim().Contains)))
                        IsFound = true;
                    else
                    {
                        IsFound = false;
                        ObjReport.Error("Validate Location  Filter.", "Different Record Found At: Position " + index + "; Value: " + webElement.GetTextValue().Trim().ToLower());
                        IsFound.Should().BeTrue();
                    }
                    index = index + 1;
                }

                if (IsFound) ObjReport.Pass("Validate Location Filter.", "Where Location = " + location);
            }
            else if (Map.LocationTable.Count == 0)
            {
                ObjReport.Warning("Validate Location Filter.", "No Record Found For Location For Where Location = " + location);
            }
            else
            {
                int index = 1;
                foreach (IWebElement webElement in Map.LocationTable)
                {
                    if (webElement.GetTextValue().Trim().ToLower().Contains(location.Trim().ToLower()))
                        IsFound = true;
                    else
                    {
                        IsFound = false;
                        ObjReport.Error("Validate Location  Filter.", "Different Record Found At: Position " + index + "; Value: " + webElement.GetTextValue().Trim().ToLower());
                        IsFound.Should().BeTrue();
                    }
                    index = index + 1;
                }

                if (IsFound) ObjReport.Pass("Validate Location Filter.", "Where Location = " + location);

            }
        }

        public void ValidateNameFilter(string name)
        {
            bool IsFound = false;

            if (Map.NameTable.Count == 0)
            {
                ObjReport.Warning("No Record Found For Name", "Where Name = " + name);
            }
            else
            {
                int index = 1;
                foreach (IWebElement webElement in Map.NameTable)
                {
                    if (webElement.GetTextValue().Trim().ToLower() == name.Trim().ToLower())
                        IsFound = true;
                    else
                    {
                        IsFound = false;
                        ObjReport.Error("Validate Name Filter. Where Name = " + name, "Different Record Found At: Position " + index + "; Value: " + webElement.GetTextValue().Trim().ToLower());
                        IsFound.Should().BeTrue();
                    }
                    index = index + 1;
                }

                if (IsFound) ObjReport.Pass("Validate Name Filter.", "Where Name = " + name);

            }
        }

        public void ValidateReSet(int expectedRowCount)
        {
            int actualRowCount = Map.NameTable.Count;
            if (actualRowCount == expectedRowCount)
                ObjReport.Pass("Validate Reset Functionality For Jon Title", "Before Reset Row Count: " + expectedRowCount + " After Reset Row Count: " + actualRowCount);
            else
            {
                ObjReport.Pass("Validate Reset Functionality For Jon Title", "Before Reset Row Count: " + expectedRowCount + " After Reset Row Count: " + actualRowCount);
                actualRowCount.Should().Be(expectedRowCount);
            }
        }
    }
}
