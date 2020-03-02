using KellermanSoftware.CompareNetObjects;
using NUnit.Framework;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Selenium.Framework.Development.Kit.Helper.NUnit.Asserts
{
    public static class Asserts
    {
        public static void AreCollectionsEqual<T>(IList<T> expected, IList<T> actual, bool ignoreOrder = true,
            string errorMessage = "", IList<string> membersToInclude = null, IList<string> membersToIgnore = null, string expectedName = null, string actualName = null)
        {
            var config = new ComparisonConfig
            {
                MaxDifferences = 100,
                IgnoreCollectionOrder = ignoreOrder
            };
            if (membersToInclude != null)
            {
                config.MembersToInclude = membersToInclude.ToList();
            }
            if (membersToIgnore != null)
            {
                config.MembersToIgnore = membersToIgnore.ToList();
            }
            if (expectedName != null)
            {
                config.ExpectedName = expectedName;
            }

            if (actualName != null)
            {
                config.ActualName = actualName;
            }

            var compareLogic = new CompareLogic { Config = config };
            var result = compareLogic.Compare(expected, actual);

            Assert.IsTrue(result.AreEqual, errorMessage + ": " + result.DifferencesString);
        }

        public static void AreNormalizedSpaceStringsEqual(string expected, string actual, string errorMessage = null)
        {
            string normalizedExpected = Regex.Replace(expected, @"\s", "");
            string normalizedActual = Regex.Replace(actual, @"\s", "");
            Assert.AreEqual(normalizedExpected, normalizedActual, errorMessage);
        }
    }
}
