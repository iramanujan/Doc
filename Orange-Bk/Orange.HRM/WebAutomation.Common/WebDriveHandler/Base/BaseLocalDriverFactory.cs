using WebAutomation.Common.AppConfigHandler;

namespace WebAutomation.Common.WebDriveHandler.Base
{
    public class BaseLocalDriverFactory
    {
        protected static readonly ToolConfigMember toolConfigMember = ToolConfigReader.GetToolConfig();
    }
}
