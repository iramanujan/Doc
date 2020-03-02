using System.Configuration;

namespace Selenium.Framework.Development.Kit.Configuration
{
    public class AppConfigReader
    {
        public static readonly string ToolConfigSection = "AppConfigMember";

        private static readonly AppConfigMember toolConfigMember;

        //static constructor to initialize only once per domain
        static AppConfigReader()
        {
            toolConfigMember = ConfigurationManager.GetSection(AppConfigReader.ToolConfigSection) as AppConfigMember;
        }
        public static AppConfigMember GetToolConfig() => toolConfigMember;
    }
}
