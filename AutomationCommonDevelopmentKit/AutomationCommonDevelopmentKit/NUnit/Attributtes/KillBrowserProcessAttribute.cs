using AutomationCommonDevelopmentKit.Utils;
using NUnit.Framework;
using NUnit.Framework.Interfaces;
using System;

namespace AutomationCommonDevelopmentKit.NUnit.Attributtes
{
    [AttributeUsage(AttributeTargets.Method, Inherited = true)]
    public class KillBrowserProcessAttribute : Attribute, ITestAction
    {
        public void BeforeTest(ITest test)
        {
            ProcessUtils.KillProcesses("chrome");
        }

        public void AfterTest(ITest test)
        {
            ProcessUtils.KillProcesses("chrome");
        }

        public ActionTargets Targets
        {
            get { return ActionTargets.Test; }
        }
    }
}
