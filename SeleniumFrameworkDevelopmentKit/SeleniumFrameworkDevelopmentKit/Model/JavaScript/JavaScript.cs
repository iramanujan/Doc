﻿using AutomationCommonDevelopmentKit.Attributes.EnumAttribute;
using AutomationCommonDevelopmentKit.Configuration;
using AutomationCommonDevelopmentKit.Log;
using OpenQA.Selenium;
using SeleniumFrameworkDevelopmentKit.WebDriverUtils.WebDriverWaits;
using System;
using System.Collections.Generic;
using System.ComponentModel;

namespace SeleniumFrameworkDevelopmentKit.Model.JavaScript
{
    public enum JScriptType
    {
        [Description("var nodes = arguments[0].childNodes;" +
                     "var text = '';" +
                     "for (var i = 0; i < nodes.length; i++) {" +
                     "    if (nodes[i].nodeName === '#text') {" +
                     "        text += nodes[i].nodeValue; " +
                     "    }" +
                     "}" +
                     "return text;")]
        NodeTextWithoutChildrenScript = 0,

        [Description("arguments[0].style.visibility='visible'; arguments[0].style.opacity = 1;")]
        ChooseFile = 1,

        [Description("arguments[0].scrollIntoView(false)")]
        ScrollIntoViewScript = 2,

        [Description("return document.readyState")]
        PageLoad = 3,

        [Description("return (typeof jQuery != 'undefined') && (jQuery.active === 0)")]
        AjaxLoad = 4,

        [Description("return (typeof jQuery == 'undefined') || (jQuery.active === 0)")]
        AjaxLoadIfExists = 5,

        [Description("$(window).scrollTop($(document).height())")]
        ScrollBottom = 6,

        [Description("$(window).scrollTop(0)")]
        ScrollTop = 7,


        [Description("arguments[0].scrollIntoView(true)")]
        ScrollToElementTop = 8,

        [Description("arguments[0].scrollIntoView(false)")]
        ScrollToElementBottom = 9,


        [Description(@"var n='REPNAME'+'=';var cookies=decodeURIComponent(document.cookie).split(';');" +
                    @"for(var i=0;i<cookies.length;i++){var c=cookies[i];while (c.charAt(0)==' '){" +
                    @"c=c.substring(1);}if (c.indexOf(n)==0&&c.length!=n.length)" +
                    @"{return c.substring(n.length, c.length);}}return ''")]
        CookieNamed = 10,


        [Description(@"var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;")]
        GetAllAttribute = 11,


        [Description(@"arguments[0].click();")]
        Click = 12,

    }

    public enum AsyncScript
    {
        [Description("var nodes = arguments[0].childNodes;" +
                     "var text = '';" +
                     "for (var i = 0; i < nodes.length; i++) {" +
                     "    if (nodes[i].nodeName === '#text') {" +
                     "        text += nodes[i].nodeValue; " +
                     "    }" +
                     "}" +
                     "return text;")]
        NodeTextWithoutChildrenScript = 0,

        [Description("arguments[0].style.visibility='visible'; arguments[0].style.opacity = 1;")]
        ChooseFile = 1,

        [Description("arguments[0].scrollIntoView(false)")]
        ScrollIntoViewScript = 2,

        [Description("return document.readyState")]
        PageLoad = 3,

        [Description("return (typeof jQuery != 'undefined') && (jQuery.active === 0)")]
        AjaxLoad = 4,

        [Description("return (typeof jQuery == 'undefined') || (jQuery.active === 0)")]
        AjaxLoadIfExists = 5,

        [Description("$(window).scrollTop($(document).height())")]
        ScrollBottom = 6,

        [Description("$(window).scrollTop(0)")]
        ScrollTop = 7
    }

    public class JavaScript
    {
        public readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();

        public object ExecuteScript(string jScriptType, IWebDriver webDriver)
        {
            try
            {
                var retVal = ((IJavaScriptExecutor)webDriver).ExecuteScript(jScriptType);
                return retVal;
            }
            catch (InvalidOperationException ObjInvalidOperationException)
            {
                Logger.Error("WaitTillAjaxLoad threw InvalidOperationException with message '{0}'", ObjInvalidOperationException.Message);
                return null;
            }
            catch (WebDriverTimeoutException ObjWebDriverTimeoutException)
            {
                Logger.Error(String.Format("Error: Exception thrown while running JS Script:{0}{1}{2}", Environment.NewLine, jScriptType, ObjWebDriverTimeoutException.Message));
                return null;
            }
            catch (Exception ObjException)
            {
                Logger.Error(String.Format("Error: Exception thrown while running JS Script:{0}", Environment.NewLine, ObjException.Message));
                return null;
            }
        }

        public object ExecuteScript(string jScriptType, IWebDriver webDriver, IWebElement webElement)
        {
            try
            {
                return ((IJavaScriptExecutor)webDriver).ExecuteScript(jScriptType, webElement);
            }
            catch (InvalidOperationException ObjInvalidOperationException)
            {
                Logger.Error("WaitTillAjaxLoad threw InvalidOperationException with message '{0}'", ObjInvalidOperationException.Message);
                return null;
            }
            catch (WebDriverTimeoutException ObjWebDriverTimeoutException)
            {
                Logger.Error(String.Format("Error: Exception thrown while running JS Script:{0}{1}{2}", Environment.NewLine, jScriptType, ObjWebDriverTimeoutException.Message));
                return null;
            }
            catch (Exception ObjException)
            {
                Logger.Error(String.Format("Error: Exception thrown while running JS Script:{0}", Environment.NewLine, ObjException.Message));
                return null;
            }
        }

        public object ExecuteScript(JScriptType jScriptType, IWebDriver webDriver)
        {
            try
            {
                var retVal = ((IJavaScriptExecutor)webDriver).ExecuteScript(jScriptType.GetDescription());
                return retVal;
            }
            catch (InvalidOperationException ObjInvalidOperationException)
            {
                Logger.Error("WaitTillAjaxLoad threw InvalidOperationException with message '{0}'", ObjInvalidOperationException.Message);
                return null;
            }
            catch (WebDriverTimeoutException ObjWebDriverTimeoutException)
            {
                Logger.Error(String.Format("Error: Exception thrown while running JS Script:{0}{1}{2}", Environment.NewLine, jScriptType.GetDescription(), ObjWebDriverTimeoutException.Message));
                return null;
            }
            catch (Exception ObjException)
            {
                Logger.Error(String.Format("Error: Exception thrown while running JS Script:{0}", Environment.NewLine, ObjException.Message));
                return null;
            }
        }

        public object ExecuteScript(JScriptType jScriptType, IWebDriver webDriver, IWebElement webElement)
        {
            try
            {
                return ((IJavaScriptExecutor)webDriver).ExecuteScript(jScriptType.GetDescription(), webElement);
            }
            catch (InvalidOperationException ObjInvalidOperationException)
            {
                Logger.Error("WaitTillAjaxLoad threw InvalidOperationException with message '{0}'", ObjInvalidOperationException.Message);
                return null;
            }
            catch (WebDriverTimeoutException ObjWebDriverTimeoutException)
            {
                Logger.Error(String.Format("Error: Exception thrown while running JS Script:{0}{1}{2}", Environment.NewLine, jScriptType.GetDescription(), ObjWebDriverTimeoutException.Message));
                return null;
            }
            catch (Exception ObjException)
            {
                Logger.Error(String.Format("Error: Exception thrown while running JS Script:{0}", Environment.NewLine, ObjException.Message));
                return null;
            }
        }

        public object ExecuteAsyncScript(AsyncScript asyncScript, IWebDriver webDriver, params object[] args)
        {
            try
            {
                return ((IJavaScriptExecutor)webDriver).ExecuteAsyncScript(asyncScript.GetDescription(), args);
            }
            catch (WebDriverTimeoutException)
            {
                Logger.Error(String.Format("Error: Exception thrown while running JS Script:{0}{1}", Environment.NewLine, asyncScript.GetDescription()));
                return null;
            }
        }

        public object WaitTillAjaxLoad(IWebDriver webDriver)
        {
            return WaitTillAjaxLoad(webDriver, appConfigMember.ObjectTimeout);
        }

        public object WaitTillAjaxLoad(IWebDriver webDriver, int waitTimeInSec = -1)
        {
            try
            {
                WebDriverWaiter.Wait(webDriver, waitTimeInSec == -1 ? appConfigMember.ObjectTimeout : waitTimeInSec).Until((IWebDriver) =>
                {
                    try
                    {
                        return (bool)((IJavaScriptExecutor)webDriver).ExecuteScript(JScriptType.AjaxLoad.GetDescription());
                    }
                    catch (Exception ObjException)
                    {
                        if (ObjException is InvalidOperationException)
                        {
                            Logger.Error(String.Format("Wait Till Ajax Load: Exception Thrown While Running JS Script. '{0}'", ObjException.Message));
                        }
                        else
                        {
                            Logger.Error(String.Format("Wait Till Ajax Load: Exception Thrown While Running JS Script.'{0}'", ObjException.Message));
                        }
                        return false;
                    }
                });
            }
            catch (WebDriverTimeoutException ObjWebDriverTimeoutException)
            {
                Logger.Debug(String.Format("Wait Till Ajax Load: Exception Thrown While Running JS Script.:{0}", ObjWebDriverTimeoutException.Message));
            }
            return false;
        }

        public object WaitTillAjaxLoadIfExists(IWebDriver webDriver)
        {
            return WaitTillAjaxLoadIfExists(webDriver, appConfigMember.ObjectTimeout);
        }

        public object WaitTillAjaxLoadIfExists(IWebDriver webDriver, int waitTimeInSec = -1)
        {
            try
            {
                WebDriverWaiter.Wait(webDriver, waitTimeInSec == -1 ? appConfigMember.ObjectTimeout / 1000 : waitTimeInSec).Until((driver) =>
                {
                    try
                    {
                        return (bool)((IJavaScriptExecutor)driver).ExecuteScript(JScriptType.AjaxLoadIfExists.GetDescription());
                    }
                    catch (Exception ObjException)
                    {
                        if (ObjException is InvalidOperationException)
                        {
                            Logger.Error(String.Format("Wait Till Ajax Load If Exists: Exception Thrown While Running JS Script. '{0}'", ObjException.Message));
                        }
                        else
                        {
                            Logger.Error(String.Format("Wait Till Ajax Load If Exists: Exception Thrown While Running JS Script.'{0}'", ObjException.Message));
                        }
                        return false;
                    }
                });
            }
            catch (WebDriverTimeoutException ObjWebDriverTimeoutException)
            {
                Logger.Error(String.Format("Wait Till Ajax Load If Exists: Exception Thrown While Running JS Script.:{0}", ObjWebDriverTimeoutException.Message));
            }
            return false;
        }

        public object WaitTillPageLoad(IWebDriver webDriver)
        {
            return WaitTillPageLoad(webDriver, appConfigMember.PageTimeout);
        }

        public object WaitTillPageLoad(IWebDriver webDriver, int waitTimeInSec)
        {
            try
            {
                WebDriverWaiter.Wait(webDriver, waitTimeInSec == -1 ? appConfigMember.PageTimeout : waitTimeInSec).Until((driver) =>
                {
                    try
                    {
                        return ((IJavaScriptExecutor)driver).ExecuteScript(JScriptType.PageLoad.GetDescription()).ToString().Contains("complete");
                    }
                    catch (Exception ObjException)
                    {
                        Logger.Error(String.Format("Wait Till Page Load: Exception Thrown While Running JS Script.:{0}", ObjException.Message));
                        return false;
                    }
                });
            }
            catch (WebDriverTimeoutException ObjWebDriverTimeoutException)
            {
                Logger.Debug(String.Format("Wait Till Page Load: Exception Thrown While Running JS Script.:{0}", ObjWebDriverTimeoutException.Message));
            }
            return false;
        }

        public void ScrollBottom(IWebDriver webDriver)
        {
            ExecuteScript(JScriptType.ScrollBottom.GetDescription(), webDriver);
            WaitTillAjaxLoad(webDriver);
        }

        public void ScrollTop(JScriptType jScriptType, IWebDriver webDriver)
        {
            ExecuteScript(JScriptType.ScrollTop.GetDescription(), webDriver);
            WaitTillAjaxLoad(webDriver);
        }

        public IWebElement JsScrollToElement(IWebDriver webDriver, IWebElement webElement, bool alignToTop = false)
        {
            ExecuteScript(alignToTop == false ? JScriptType.ScrollBottom : JScriptType.ScrollTop, webDriver, webElement);
            return webElement;
        }

        public string JsGetCookieNamed(string name, IWebDriver webDriver)
        {
            var script = JScriptType.CookieNamed.GetDescription().Replace("REPNAME", name);
            return ExecuteScript(script, webDriver) as string;
        }

        public Dictionary<string, object> GetAttributes(JScriptType jScriptType, IWebDriver webDriver, IWebElement webElement)
        {
            IJavaScriptExecutor js = (IJavaScriptExecutor)webDriver;
            Dictionary<string, Object> Attribute = new Dictionary<string, object>();
            Attribute = (Dictionary<string, Object>)js.ExecuteScript(jScriptType.GetDescription(), webElement);
            return Attribute;
        }
    }
}
