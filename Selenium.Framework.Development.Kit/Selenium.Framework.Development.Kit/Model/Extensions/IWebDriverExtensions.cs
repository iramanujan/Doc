using OpenQA.Selenium;
using OpenQA.Selenium.Internal;
using OpenQA.Selenium.Support.UI;
using Selenium.Framework.Development.Kit.Configuration;
using Selenium.Framework.Development.Kit.Helper.Attributes;
using Selenium.Framework.Development.Kit.Helper.Log;
using Selenium.Framework.Development.Kit.Helper.Utils;
using Selenium.Framework.Development.Kit.Helper.Wait;
using Selenium.Framework.Development.Kit.Model.JavaScript;
using System;
using System.Collections.ObjectModel;
using System.Linq;
using static Selenium.Framework.Development.Kit.Configuration.AppConfigMember;

namespace Selenium.Framework.Development.Kit.Model.Extensions
{
    public static class IWebDriverExtensions
    {
        private static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        private static DefaultWait<IWebElement> webElementFluentWait = null;
        public static bool WaitForAjax(this IWebDriver webDriver, int waitTimeInSec = -1)
        {

            bool isAjaxFinished = false;
            IJavaScriptExecutor javascript = webDriver as IJavaScriptExecutor;
            if (javascript == null)
                throw new ArgumentException("driver", "Driver must support javascript execution");
            Waiter.Wait(webDriver, waitTimeInSec == -1 ? appConfigMember.PageTimeout : waitTimeInSec).Until((driver) =>
            {
                isAjaxFinished = (bool)javascript.ExecuteScript("return window.jQuery != undefined && jQuery.active === 0");
                return isAjaxFinished;
            });
            return isAjaxFinished;
        }

        public static bool WaitForPage(this IWebDriver webDriver, int waitTimeInSec = -1)
        {
            bool IsPageLoad = false;
            IJavaScriptExecutor javascript = webDriver as IJavaScriptExecutor;
            if (javascript == null)
                throw new ArgumentException("driver", "Driver must support javascript execution");
            try
            {
                Waiter.Wait(webDriver, waitTimeInSec == -1 ? appConfigMember.PageTimeout : waitTimeInSec).Until((driver) =>
                {
                    try
                    {
                        IsPageLoad = (bool)javascript.ExecuteScript(JScriptType.PageLoad.GetDescription()).ToString().Contains("complete");
                        return IsPageLoad;
                    }
                    catch (InvalidOperationException e)
                    {
                        Logger.Error(e.Message);
                        IsPageLoad = e.Message.ToLower().Contains("unable to get browser");
                        return IsPageLoad;
                    }
                    catch (WebDriverException e)
                    {
                        Logger.Error(e.Message);
                        IsPageLoad = e.Message.ToLower().Contains("unable to connect");
                        return IsPageLoad;
                    }
                    catch (Exception e)
                    {
                        Logger.Error(e.Message);
                        return IsPageLoad;
                    }
                });
            }
            catch (WebDriverTimeoutException ObjWebDriverTimeoutException)
            {
                Logger.Error(String.Format("Wait Till Page Load: Exception Thrown While Running JS Script.:{0}", ObjWebDriverTimeoutException.Message));
            }
            return IsPageLoad;
        }

        public static IJavaScriptExecutor JavaScriptExecutor(this IWebDriver webDriver)
        {
            IJavaScriptExecutor javascript = webDriver as IJavaScriptExecutor;
            if (javascript == null)
                throw new ArgumentException("driver", "Driver must support javascript execution");
            return javascript;
        }

        public static ITakesScreenshot ScreenShoter(this IWebDriver webDriver)
        {
            ITakesScreenshot takesScreenshot = webDriver as ITakesScreenshot;
            if (takesScreenshot == null)
                throw new ArgumentException("driver", "Driver must support javascript execution");
            return takesScreenshot;
        }

        #region Window Handles
        public static IWebDriver SwitchToWindow(this IWebDriver webDriver, string windowName)
        {
            return webDriver.SwitchTo().Window(windowName);
        }
        public static string SwitchToFirstWindow(this IWebDriver webDriver)
        {
            return webDriver.WindowHandles.First();
        }
        public static string SwitchToLastWindow(this IWebDriver webDriver)
        {
            return webDriver.WindowHandles.Last();
        }
        public static IWebDriver SwitchToDefaultContent(this IWebDriver webDriver)
        {
            return webDriver.SwitchTo().DefaultContent();
        }
        #endregion

        #region Navigation History
        public static void Forward(this IWebDriver webDriver, string windowName)
        {
            webDriver.Navigate().Forward();
        }
        public static void Back(this IWebDriver webDriver)
        {
            webDriver.Navigate().Back();
        }
        public static void Refresh(this IWebDriver webDriver)
        {
            webDriver.Navigate().Refresh();
        }
        public static void GoToUrl(this IWebDriver webDriver, string url)
        {
            webDriver.Navigate().GoToUrl(url);
        }
        public static void Maximize(this IWebDriver webDriver)
        {
            webDriver.Manage().Window.Maximize();
        }
        #endregion

        #region Frame
        public static T SwitchToFrameByIndex<T>(this T webDriver, int frameIndex) where T : IWebDriver
        {
            webDriver.SwitchTo().Frame(frameIndex);
            return webDriver;
        }
        public static T SwitchToFrameByFrameName<T>(this T webDriver, string frameName) where T : IWebDriver
        {
            webDriver.SwitchTo().Frame(frameName);
            return webDriver;
        }
        public static T SwitchToFrameByWebElement<T>(this T webDriver) where T : IWebDriver
        {
            IWrapsElement wrapsElement = webDriver as IWrapsElement;
            if (wrapsElement == null)
                throw new ArgumentException("element", "Element must wrap a web driver");
            IWebElement webElement = wrapsElement.WrappedElement;
            webDriver.SwitchTo().Frame(webElement);
            return webDriver;
        }
        public static ReadOnlyCollection<IWebElement> FrameHandles(this IWebDriver webDriver)
        {
            return webDriver.FindElements(By.TagName("iframe"));
        }
        #endregion

        public static void QuitWebDriver(this IWebDriver webDriver)
        {
            try
            {
                foreach (var window in webDriver.WindowHandles)
                {
                    var win = webDriver.SwitchTo().Window(window);
                    Logger.Info("Below Window Close:" + win.Title);
                    webDriver.Close();
                }
                webDriver.Quit();
                ProcessUtils.KillAllBrowser();
            }
            catch (Exception ex)
            {
                Logger.Error($"Unable to Quit the browser. Reason: {ex.Message}");
                switch (appConfigMember.Browser)
                {
                    case BrowserType.IE:

                        ProcessUtils.KillProcesses("iexplore");
                        ProcessUtils.KillProcesses("IEDriverServer");
                        break;
                    case BrowserType.Chrome:
                        ProcessUtils.KillProcesses("chrome");
                        ProcessUtils.KillProcesses("chromedriver");
                        ProcessUtils.KillProcesses("chrome.exe");
                        ProcessUtils.KillProcesses("chromedriver.exe");
                        break;
                    case BrowserType.Firefox:
                        ProcessUtils.KillProcesses("firefox.exe");
                        ProcessUtils.KillProcesses("geckodriver.exe");
                        ProcessUtils.KillProcesses("firefox");
                        ProcessUtils.KillProcesses("geckodriver");
                        break;
                }
            }
        }

        public static void KillAllBrowser(this IWebDriver webDriver)
        {
            ProcessUtils.KillProcesses("iexplore");
            ProcessUtils.KillProcesses("IEDriverServer");
            ProcessUtils.KillProcesses("iexplore.exe");
            ProcessUtils.KillProcesses("IEDriverServer.exe");
            ProcessUtils.KillProcesses("chrome");
            ProcessUtils.KillProcesses("chromedriver");
            ProcessUtils.KillProcesses("chrome.exe");
            ProcessUtils.KillProcesses("chromedriver.exe");
            ProcessUtils.KillProcesses("firefox.exe");
            ProcessUtils.KillProcesses("geckodriver.exe");
            ProcessUtils.KillProcesses("firefox");
            ProcessUtils.KillProcesses("geckodriver");
        }

        public static void InitializeApplication(this IWebDriver webDriver)
        {
            webDriver.GoToUrl(appConfigMember.Url);
            webDriver.WaitForPage(300);
            webDriver.WaitForAjax(300);
            webDriver.Maximize();
        }

        public static string GetDecodedUrl(this IWebDriver webDriver)
        {
            var url = webDriver.Url;
            return HttpUtility.UrlDecode(url);
        }

        public static IWebElement ElementExists(this IWebDriver webDriver , By by)
        {
            IWebElement webElement = null;
            int retry = 5;
            do
            {
                try
                {
                    webElement = webDriver.FindElement(by);
                    return webElement;
                }
                catch (OpenQA.Selenium.StaleElementReferenceException)
                {
                    if (retry == 0)
                    {
                        throw;
                    }
                }
                catch (OpenQA.Selenium.WebDriverException)
                {
                    return webElement;
                }
                retry--;
            } while (retry >= 0);
            return webElement;
        }

        public static IWebElement GetWebElement(this IWebDriver webDriver,By by)
        {
            IWebElement webElement = null;
            webElement = webDriver.FindElement(by);
            webElementFluentWait = new DefaultWait<IWebElement>(webElement);
            webElementFluentWait.Timeout = TimeSpan.FromSeconds(appConfigMember.ObjectTimeout);
            webElementFluentWait.PollingInterval = TimeSpan.FromMilliseconds(appConfigMember.PollingInterval);
            webElementFluentWait.IgnoreExceptionTypes(typeof(NoSuchElementException), typeof(StaleElementReferenceException));
            Func<IWebElement, IWebElement> waiter = new Func<IWebElement, IWebElement>((IWebElement ele) =>
            {
                if (webElement.Enabled & webElement.Displayed & webDriver.FindElement(by).Size.Width > 0 & webDriver.FindElement(by).Size.Height > 0)
                {
                    return webElement;
                }
                else
                {
                    return null;
                }
            });
            webElementFluentWait.Until(waiter);
            return webElement;
        }
    }
}
