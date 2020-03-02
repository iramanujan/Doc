using AutomationCommonDevelopmentKit.Attributes.EnumAttribute;
using AutomationCommonDevelopmentKit.Configuration;
using AutomationCommonDevelopmentKit.Log;
using OpenQA.Selenium;
using OpenQA.Selenium.Interactions;
using OpenQA.Selenium.Internal;
using OpenQA.Selenium.Support.UI;
using SeleniumFrameworkDevelopmentKit.Model.HtmlObject;
using SeleniumFrameworkDevelopmentKit.Model.JavaScript;
using SeleniumFrameworkDevelopmentKit.WebDriverUtils.WebDriverWaits;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;

namespace SeleniumFrameworkDevelopmentKit.Model.Extensions
{
    public static class IWebElementExtensions
    {
        private static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();

        #region Page Scroll(Vertical,Horizontal) and Object Scroll(Vertical,Horizontal)
        public static void ScrollPageVertically(this IWebElement webElement)
        {
            IWebDriver webDriver = webElement.GetIWebDriver();

            if (webElement is ILocatable locatableCalendar)
            {
                var halfWindowHeight = webDriver.Manage().Window.Size.Height / 2;
                var targetElementVerticalPosition = locatableCalendar.Coordinates.LocationInDom.Y;
                var yCoordinateForElementCenterScreen = targetElementVerticalPosition - halfWindowHeight; //locatableCalendar.Coordinates.LocationInDom.Y
                webDriver.JavaScriptExecutor().ExecuteScript($"window.scrollTo(0, {yCoordinateForElementCenterScreen});");
            }
        }

        public static void ScrollPageHorizontally(this IWebElement webElement)
        {
            IWebDriver webDriver = webElement.GetIWebDriver();

            if (webElement is ILocatable locatableCalendar)
            {
                var halfWindowWidth = webDriver.Manage().Window.Size.Width / 2;
                var targetElementHorizontalPosition = locatableCalendar.Coordinates.LocationInDom.X;
                var xCoordinateForElementCenterScreen = targetElementHorizontalPosition - halfWindowWidth;
                webDriver.JavaScriptExecutor().ExecuteScript($"window.scrollTo({xCoordinateForElementCenterScreen},0);");
            }
        }

        public static void ScrollIntoPageView(this IWebElement webElement)
        {
            IWebDriver webDriver = webElement.GetIWebDriver();

            if (webElement is ILocatable locatableCalendar)
            {
                var halfWindowWidth = webDriver.Manage().Window.Size.Width / 2;
                var targetElementHorizontalPosition = locatableCalendar.Coordinates.LocationInDom.X;
                var xCoordinateForElementCenterScreen = targetElementHorizontalPosition - halfWindowWidth;

                var halfWindowHeight = webDriver.Manage().Window.Size.Height / 2;
                var targetElementVerticalPosition = locatableCalendar.Coordinates.LocationInDom.Y;
                var yCoordinateForElementCenterScreen = targetElementVerticalPosition - halfWindowHeight;

                webDriver.JavaScriptExecutor().ExecuteScript($"window.scrollTo({xCoordinateForElementCenterScreen},{yCoordinateForElementCenterScreen});");
            }
        }

        public static void ScrollIntoObjectByMouse(this IWebElement webElement)
        {
            IWebDriver webDriver = webElement.GetIWebDriver();
            try
            {
                Actions action = new Actions(webDriver);
                var X = webElement.Size.Width;
                var Y = webElement.Size.Height;
                action.MoveToElement(webElement, X, Y).Perform();
            }
            catch (Exception e)
            {
                Logger.Error(e.Message);
            }
        }
        #endregion

        #region DropDown
        public static void EnterText(this IWebElement webElement, string value)
        {
            Enumerable.Range(0, webElement.Text.Length).ToList().ForEach(arg => webElement.SendKeys(Keys.Backspace));
            webElement.SendKeys(value);
            webElement.SendKeys(Keys.Enter);
        }

        public static void SelectByIndex(this IWebElement webElement, int index)
        {
            var selectElement = new SelectElement(webElement);
            selectElement.SelectByIndex(index);
        }

        public static void SelectByValue(this IWebElement webElement, string value)
        {
            var selectElement = new SelectElement(webElement);
            selectElement.SelectByValue(value);
        }

        public static void SelectByText(this IWebElement webElement, string text)
        {
            var selectElement = new SelectElement(webElement);
            selectElement.SelectByText(text);
        }

        public static string SelectedOption(this IWebElement webElement)
        {
            var selectElement = new SelectElement(webElement);
            return selectElement.SelectedOption.Text;
        }

        public static List<String> GetOptions(this IWebElement webElement)
        {
            List<String> Options = new List<string>();
            var selectElement = new SelectElement(webElement);
            Options = selectElement.Options.Select(item => item.Text).ToList();
            return Options;
        }

        public static void DeselectAll(this IWebElement webElement)
        {
            var selectElement = new SelectElement(webElement);
            selectElement.DeselectAll();
        }

        public static void DeselectByIndex(this IWebElement webElement, int index)
        {
            var selectElement = new SelectElement(webElement);
            selectElement.DeselectByIndex(index);
        }

        public static void DeselectByValue(this IWebElement webElement, string value)
        {
            var selectElement = new SelectElement(webElement);
            selectElement.DeselectByValue(value);
        }

        public static void DeselectByText(this IWebElement webElement, string text)
        {
            var selectElement = new SelectElement(webElement);
            selectElement.DeselectByText(text);
        }

        public static Boolean IsMultiple(this IWebElement webElement)
        {
            var selectElement = new SelectElement(webElement);
            return selectElement.IsMultiple;
        }
        #endregion

        #region Attribute
        public static string GetText(this IWebElement webElement)
        {
            return webElement.GetAttribute(TagAttributes.Text);
        }

        public static string GetTextValue(this IWebElement webElement)
        {
            String text = null;
            try
            {
                string textContentValue = webElement.GetAttribute(TagAttributes.TextContent);
                if (!string.IsNullOrEmpty(textContentValue))
                {
                    text = textContentValue;
                }
            }
            catch (Exception)
            {
                try
                {
                    string value = webElement.GetAttribute(TagAttributes.Value);
                    if (!string.IsNullOrEmpty(value))
                    {
                        text = value;
                    }
                }
                catch (Exception)
                {
                    string textValue = webElement.Text;
                    if (!string.IsNullOrEmpty(textValue))
                    {
                        text = textValue;
                    }
                }
            }
            return text;
        }

        public static string GetHref(this IWebElement webElement)
        {
            return webElement.GetAttribute(TagAttributes.Href);
        }

        public static string GetSrc(this IWebElement webElement)
        {
            return webElement.GetAttribute(TagAttributes.Src);
        }

        public static string GetValue(this IWebElement webElement)
        {
            return webElement.GetAttribute(TagAttributes.Value);
        }

        public static string GetInnerHtml(this IWebElement webElement)
        {
            return webElement.GetAttribute(TagAttributes.InnerHtml);
        }

        public static string GetOuterHtml(this IWebElement webElement)
        {
            return webElement.GetAttribute(TagAttributes.OuterHtml);
        }

        public static string GetInnerText(this IWebElement webElement)
        {
            return webElement.GetAttribute(TagAttributes.InnerText);
        }

        public static string GetClass(this IWebElement webElement)
        {
            return webElement.GetAttribute(TagAttributes.Class);
        }

        public static bool HasClass(this IWebElement webElement, string className)
        {
            return webElement.GetAttribute("class")?.Split(' ').Contains(className) ?? false;
        }

        public static bool HasAttribute(this IWebElement webElement, string attribute)
        {
            bool IsHasAttribute;
            try
            {
                var value = webElement.GetAttribute(attribute);
                if (value != null)
                    IsHasAttribute = true;
                else
                {
                    IsHasAttribute = false;
                }
            }
            catch (StaleElementReferenceException)
            {
                IsHasAttribute = false;
            }
            catch (Exception)
            {
                IsHasAttribute = false;
            }
            return IsHasAttribute;
        }

        public static Dictionary<string, Object> GetAllAttribute(this IWebElement webElement)
        {
            IWebDriver webDriver = webElement.GetIWebDriver();
            return (Dictionary<string, Object>)GetIWebDriver(webElement).JavaScriptExecutor().ExecuteScript(JScriptType.GetAllAttribute.GetDescription(), webElement);
        }
        #endregion

        private static IWebDriver GetIWebDriver(this IWebElement webElement)
        {
            IWrapsDriver wrapsDriver = webElement as IWrapsDriver;
            if (wrapsDriver == null)
                throw new ArgumentException("element", "Element must wrap a web driver");
            IWebDriver webDriver = wrapsDriver.WrappedDriver;
            return webDriver;
        }

        public static void SendKeysInUpperCase(this IWebElement webElement, String text)
        {
            webElement.SendKeys(text.ToUpper());
        }

        public static void SendKeysInLowerCase(this IWebElement webElement, String text)
        {
            webElement.SendKeys(text.ToLower());
        }

        public static void SendKeysWithAction(this IWebElement webElement, String text, String keys)
        {
            webElement.SendKeys(text);
            webElement.SendKeys(keys);
        }
        public static int GetColumnIndex(this ReadOnlyCollection<IWebElement> TableHeader, string ColumnName, int ColumnIndex = 0, string Attribute = TagAttributes.Value)
        {
            foreach (var item in TableHeader)
            {
                try
                {
                    if (item.GetAttribute(Attribute).Trim().ToLower() == ColumnName.Trim().ToLower()) break;
                }
                catch
                {
                    try
                    {
                        if (item.Text.Trim().ToLower() == ColumnName.Trim().ToLower()) break;
                    }
                    catch (Exception ObjException2)
                    {
                        Logger.Error("Error Occured At Column" + ObjException2.Message);
                    }
                }
                ColumnIndex = ColumnIndex + 1;
            }
            return ColumnIndex;
        }

        public static IWebElement WaitForElement(this IWebElement webElement)
        {
            WebDriverWaiter.Wait(webElement.GetIWebDriver(), appConfigMember.ObjectTimeout).Until<Boolean>(webDriver =>
                                                                    webElement.Enabled
                                                                & webElement.Displayed
                                                                & webElement.Size.Width > 0
                                                                & webElement.Size.Height > 0);
            return webElement;
        }

    }
}
