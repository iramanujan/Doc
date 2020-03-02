using NUnit.Framework;
using NUnit.Framework.Interfaces;
using Selenium.Framework.Development.Kit.Helper.Utils;
using System;

namespace Selenium.Framework.Development.Kit.Helper.NUnit.Attributtes
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
