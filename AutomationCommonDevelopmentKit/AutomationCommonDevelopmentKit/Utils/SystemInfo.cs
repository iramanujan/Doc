using System;
using System.Text.RegularExpressions;
using Microsoft.Win32;


namespace AutomationCommonDevelopmentKit.Utils
{
    public static class SystemInfo
    {

        public static ulong GetSystemMemoryInBytes()
        {
            return new Microsoft.VisualBasic.Devices.ComputerInfo().TotalPhysicalMemory;
        }


        public static double GetWindowsVersion()
        {
            string productName = (string)Registry.GetValue(@"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion", "ProductName", string.Empty);
            double version = 7;
            Double.TryParse(Regex.Match(productName, "\\d+\\.?\\d*").ToString(), out version);
            return version;
        }

        public static string GetWindowsInfo()
        {
            string productName = (string)Registry.GetValue(@"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion", "ProductName", string.Empty);

            double version = 7;
            Double.TryParse(Regex.Match(productName, "\\d+\\.?\\d*").ToString(), out version);

            string PROCESSOR_ARCHITECTURE = (string)Registry.GetValue(@"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment", "PROCESSOR_ARCHITECTURE", string.Empty);

            double bit = 7;
            Double.TryParse(Regex.Match(PROCESSOR_ARCHITECTURE, "\\d{2}").ToString(), out bit);

            return (productName + " " + Convert.ToString(bit) + " Bit Processor Architecture");
        }
    }
}
