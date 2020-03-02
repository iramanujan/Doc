using AutomationCommonDevelopmentKit.Utils;
using NUnit.Framework;
using NUnit.Framework.Interfaces;
using System;

namespace AutomationCommonDevelopmentKit.NUnit.Attributtes
{
    [AttributeUsage(AttributeTargets.Method, Inherited = true)]
    public class KillNotepadProcessAttribute : Attribute, ITestAction
    {
        public void BeforeTest(ITest test)
        {
            ProcessUtils.KillProcesses("notepad");
        }

        public void AfterTest(ITest test)
        {
            ProcessUtils.KillProcesses("notepad");
        }

        public ActionTargets Targets
        {
            get { return ActionTargets.Test; }
        }
    }
}
