using Automation.Common.Log;
using System;
using WebAutomation.Common.AppConfigHandler;

namespace Testing
{
    class Program
    {
        //private static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();

        private static readonly ToolConfigMember appConfigMember = ToolConfigReader.GetToolConfig();
        static void Main(string[] args)
        {
            Logger.Info(appConfigMember.RootDownloadLocation);
            Logger.Debug(appConfigMember.RootUploadLocation);
            Console.ReadKey();
        }
    }
}
