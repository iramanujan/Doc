using Selenium.Framework.Development.Kit.Helper.Log;
using Selenium.Framework.Development.Kit.Helper.Wait;
using System;
using System.Diagnostics;
using System.Linq;

namespace Selenium.Framework.Development.Kit.Helper.Utils
{
    public static class ProcessUtils
    {

        public static Process[] GetCurrentSessionProcessesByName(string name)
        {
            var currentSessionId = Process.GetCurrentProcess().SessionId;
            return Process.GetProcessesByName(name).Where(x => x.SessionId == currentSessionId).ToArray();
        }

        public static void KillProcesses(string processName)
        {
            Logger.Info("Kill processes if any by name {0}", processName);
            Process[] processes = Process.GetProcessesByName(processName);
            Logger.Info("{0} {1} processes found", processes.Length, processName);
            if (processes.Length == 0)
            {
                return;
            }
            foreach (var process in processes)
            {
                try
                {
                    process.Kill();
                }
                catch
                {
                }
            }
            WaitForProcessNotRunning(processName);
        }

        public static void WaitForProcessNotRunning(string processName)
        {
            Waiter.SpinWaitEnsureSatisfied(
                () => System.Diagnostics.Process.GetProcessesByName(processName).Length == 0, TimeSpan.FromSeconds(10),
                TimeSpan.FromSeconds(1), "The process '" + processName + "' still running");
        }

        public static void WaitForProcessRunning(string processName)
        {
            Waiter.SpinWaitEnsureSatisfied(
                () => Process.GetProcessesByName(processName).Length > 0, TimeSpan.FromSeconds(30),
                TimeSpan.FromSeconds(1), "The process '" + processName + "' still not running");
        }

        public static void KillAllBrowser()
        {
            ProcessUtils.KillProcesses("iexplore");
            ProcessUtils.KillProcesses("IEDriverServer");
            ProcessUtils.KillProcesses("iexplore.exe");
            ProcessUtils.KillProcesses("IEDriverServer.exe");
            ProcessUtils.KillProcesses("chrome");
            ProcessUtils.KillProcesses("chromedriver");
            ProcessUtils.KillProcesses("chrome.exe");
            ProcessUtils.KillProcesses("chromedriver.exe");
            ProcessUtils.KillProcesses("firefox.exe");
            ProcessUtils.KillProcesses("geckodriver.exe");
            ProcessUtils.KillProcesses("firefox");
            ProcessUtils.KillProcesses("geckodriver");
        }

    }
}
