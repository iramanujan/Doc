using System;
using NUnit.Framework.Interfaces;
using NUnit.Framework.Internal;

namespace AutomationCommonDevelopmentKit.NUnit.Attributtes
{
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, Inherited = true)]
    public class IgnoreForX86 : Attribute, IApplyToTest
    {
        public void ApplyToTest(Test test)
        {
            if(!Environment.Is64BitOperatingSystem)
            {
                test.RunState = RunState.Ignored;
                test.Properties.Set(PropertyNames.SkipReason, String.Format("Test is not allowed to run on x86 systems"));
            }
        }
     }
}
