using System;
using System.IO;
using System.Text;
using System.Xml;
using System.Xml.Linq;
using System.Xml.Serialization;

namespace Selenium.Framework.Development.Kit.Helper.Utils
{ 
    public class XMLUtils
    {
        private readonly XmlDocument doc;
        private readonly string path;

        public XMLUtils(string filePath)
        {
            doc = new XmlDocument();
            doc.Load(filePath);
            path = filePath;
        }

        public string FetchValue(string section, string key)
        {
            string retString = null;
            string value = ReadValue(section, key);
            if (value == null)
            {
                return null;
            }
            if (value.Contains("${"))
            {
                int start = value.IndexOf("${");
                string first = value.Substring(0, start);
                string sec = null;
                string k = null;
                if (value.IndexOf("/") == -1)
                {
                    sec = section;
                    k = value.Substring(start + 2, value.IndexOf("}") - (start + 2));
                }
                else
                {
                    sec = value.Substring(start + 2, value.IndexOf("/") - (start + 2));
                    k = value.Substring(value.IndexOf("/") + 1, value.IndexOf("}") - (value.IndexOf("/") + 1));
                }
                string last = value.Substring(value.IndexOf("}") + 1);
                retString = FetchValue(sec, k);
                retString = first + retString + last;
            }
            else retString = value;
            return retString;
        }

        public string ReadValue(string section, string key)
        {
            var node = doc.SelectSingleNode("//Section[@name='" + section + "']//" + key);
            return (node == null) ? null : node.InnerText;
        }

        public bool WriteValue(string section, string key, string value)
        {
            XmlNode node = doc.CreateElement(key);
            node.InnerText = value;
            if (doc.SelectSingleNode("//Section[@name='" + section + "']") != null)
            {
                if (doc.SelectSingleNode("//Section[@name='" + section + "']//" + key) != null)
                    doc.SelectSingleNode("//Section[@name='" + section + "']//" + key).InnerText = value;
                else doc.SelectSingleNode("//Section[@name='" + section + "']").AppendChild(node);
            }
            else
            {
                XmlElement sec = doc.CreateElement("Section");
                sec.SetAttribute("name", section);
                sec.AppendChild(node);
                doc.SelectSingleNode("//Config").AppendChild(sec);
            }
            doc.Save(path);
            return true;
        }

        public static Object DeserializeXElement(XElement data, Type type)
        {
            using (var memoryStream = new MemoryStream(Encoding.Unicode.GetBytes(data.ToString())))
            {
                var xmlSerializer = new XmlSerializer(type);
                return xmlSerializer.Deserialize(memoryStream);
            }
        }

        public static Object DeserializeXml(string locationPath, Type deserializerClassType)
        {
            return null;
            //string locatorsFilePath = Path.Combine(AutoUtils.GetTestHome(), locationPath);
            //XmlSerializer xs = new XmlSerializer(deserializerClassType);
            //using (Stream locatorsStream = File.Open(locatorsFilePath, FileMode.Open))
            //{
            //    return xs.Deserialize(locatorsStream);
            //}
        }
    }
}
