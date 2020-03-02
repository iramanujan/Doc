using System;
using System.Linq;
using System.Configuration;
using NUnit.Framework.Interfaces;
using NUnit.Framework.Internal;

namespace Selenium.Framework.Development.Kit.Helper.NUnit.Attributtes
{
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, Inherited = true)]
    public class AllowedEnvironments : Attribute, IApplyToTest
    {
        private readonly string[] allowedEnvironments;

        public AllowedEnvironments(params string[] arguments)
        {
            this.allowedEnvironments = arguments;
        }

        public void ApplyToTest(Test test)
        {
            if (!allowedEnvironments.Contains(ConfigurationManager.AppSettings["Environment"]))
            {
                test.RunState = RunState.Ignored;
                test.Properties.Set(PropertyNames.SkipReason, String.Format("Test is not allowed to run on current Environment. Allowed environments are: {0}", String.Join(", ", this.allowedEnvironments)));
            }
        }
     }
}
