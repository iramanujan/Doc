using AutomationCommonDevelopmentKit.Log;
using AutomationCommonDevelopmentKit.Wait;
using System;
using System.Diagnostics;
using System.Linq;
using System.Threading;

namespace AutomationCommonDevelopmentKit.Utils
{
    public static class ProcessUtils
    {

        public static Process[] GetCurrentSessionProcessesByName(string name)
        {
            var currentSessionId = Process.GetCurrentProcess().SessionId;
            return Process.GetProcessesByName(name).Where(x => x.SessionId == currentSessionId).ToArray();
        }

        public static void RunCommandRunAsAdmin(string command)
        {
            Thread.Sleep(2000);
            ProcessStartInfo myProcessInfo = new ProcessStartInfo();
            myProcessInfo = new ProcessStartInfo();
            myProcessInfo.FileName = Environment.ExpandEnvironmentVariables("%SystemRoot%") + @"\System32\cmd.exe";
            myProcessInfo.Arguments = command;
            myProcessInfo.Verb = "runas";
            var adminProcess = Process.Start(myProcessInfo);
            adminProcess.Close();
            Thread.Sleep(2000);
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
            ProcessUtils.RunCommandRunAsAdmin(@"/c taskkill.exe /F /IM MicrosoftEdge.exe /IM iexplore.exe /IM IEDriverServer.exe /IM chrome.exe /IM chromedriver.exe /IM firefox.exe /IM geckodriver.exe /IM Excel.exe /T");


            ProcessUtils.KillProcesses("iexplore");
            ProcessUtils.KillProcesses("iexplore.exe");

            ProcessUtils.KillProcesses("IEDriverServer");
            ProcessUtils.KillProcesses("IEDriverServer.exe");

            ProcessUtils.KillProcesses("chrome");
            ProcessUtils.KillProcesses("chrome.exe");

            ProcessUtils.KillProcesses("chromedriver");
            ProcessUtils.KillProcesses("chromedriver.exe");

            ProcessUtils.KillProcesses("firefox");
            ProcessUtils.KillProcesses("firefox.exe");

            ProcessUtils.KillProcesses("geckodriver");
            ProcessUtils.KillProcesses("geckodriver.exe");
        }
    }
}
