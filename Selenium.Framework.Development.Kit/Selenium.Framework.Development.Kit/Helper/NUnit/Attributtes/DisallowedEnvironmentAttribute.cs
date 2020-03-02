using System;
using System.Linq;
using System.Configuration;
using NUnit.Framework.Interfaces;
using NUnit.Framework.Internal;

namespace Selenium.Framework.Development.Kit.Helper.NUnit.Attributtes
{
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, Inherited = true)]
    public class DisallowedEnvironmentAttribute : Attribute, IApplyToTest
    {
        private readonly string[] disallowedEnvironment;

        public DisallowedEnvironmentAttribute(params string[] arguments)
        {
            this.disallowedEnvironment = arguments;
        }

        public void ApplyToTest(Test test)
        {
            if (disallowedEnvironment.Contains(ConfigurationManager.AppSettings["Environment"]))
            {
                test.RunState = RunState.Ignored;
                test.Properties.Set(PropertyNames.SkipReason, String.Format("Test is not allowed to run on current Environment. Forbidden environments are: {0}", String.Join(", ", this.disallowedEnvironment)));
            }
        }
    }
}
