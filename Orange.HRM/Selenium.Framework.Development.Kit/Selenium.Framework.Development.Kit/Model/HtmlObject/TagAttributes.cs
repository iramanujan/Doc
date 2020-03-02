using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Selenium.Framework.Development.Kit.Model.HtmlObject
{
    public static class TagAttributes
    {
        public const string Text = "text";
        public const string Style = "style";
        public const string Href = "href";
        public const string Src = "src";
        public const string Value = "value";
        public const string Title = "title";
        public const string Class = "class";
        public const string Disabled = "disabled";
        public const string Checked = "checked";
        public const string TextContent = "textContent";
        public const string InnerText = "innerText";
        public const string OuterHtml = "outerHTML";
        public const string InnerHtml = "innerHTML";

        public static class StyleAttribute
        {
            public const string DisplayBlock = "display: block";
            public const string DisplayInline = "display: inline";
            public const string DisplayNone = "display: none";
        }
    }
}
