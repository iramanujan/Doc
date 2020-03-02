using Automation.Common.Log;
using System;
using System.Diagnostics;
using System.Linq;
using WebAutomation.Common.Wait;

namespace WebAutomation.Common.GenericHelper.Utils
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
            System.Diagnostics.Process[] processes = System.Diagnostics.Process.GetProcessesByName(processName);
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

    }
}
