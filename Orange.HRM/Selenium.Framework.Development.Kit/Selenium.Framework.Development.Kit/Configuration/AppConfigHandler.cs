using System.Configuration;
using System.IO;
using System.Runtime.Serialization;
using System.Text;
using System.Xml;

namespace Selenium.Framework.Development.Kit.Configuration
{
    public class AppConfigHandler : IConfigurationSectionHandler
    {
        public object Create(object parent, object configContext, XmlNode section)
        {
            using (var ms = new MemoryStream(Encoding.UTF8.GetBytes(section.OuterXml)))
            {
                return (AppConfigMember)new DataContractSerializer(typeof(AppConfigMember)).ReadObject(ms);
            }
        }
    }
}
