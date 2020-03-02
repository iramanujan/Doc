using AventStack.ExtentReports;
using AventStack.ExtentReports.Reporter;
using AventStack.ExtentReports.Reporter.Configuration;
using NUnit.Framework;
using Selenium.Framework.Development.Kit.Configuration;
using Selenium.Framework.Development.Kit.Helper.Log;
using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Globalization;
using System.Windows.Forms;

namespace Selenium.Framework.Development.Kit.Helper.Report
{
    public sealed class Report
    {
        public ExtentReports extentReports = null;
        public ExtentTest test = null;
        private static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        private TextInfo textInfo = new CultureInfo("en-US", false).TextInfo;

        private string ScreenshotImagPath = "";
        private static readonly Report ObjReport = new Report();
        public static Report ReportInstance => ObjReport;

        static Report()
        {
        }

        private Report()
        {
        }

        public void ExtentReportsSetup()
        {
            try
            {
                string Is64BitOperatingSystem = " 32 bit";
                if (System.Environment.Is64BitOperatingSystem)
                    Is64BitOperatingSystem = " 64 bit";

                string pth = System.Reflection.Assembly.GetCallingAssembly().CodeBase;
                string actualPath = pth.Substring(0, pth.LastIndexOf("bin"));
                string projectPath = new Uri(actualPath).LocalPath; // project path 
                string reportPath = appConfigMember.AutomationReportPath + "AutomationReportReport.html";
                string subKey = @"SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion";
                Microsoft.Win32.RegistryKey key = Microsoft.Win32.Registry.LocalMachine;
                Microsoft.Win32.RegistryKey skey = key.OpenSubKey(subKey);
                string name = skey.GetValue("ProductName").ToString();
                extentReports = new ExtentReports();
                var htmlReporter = new ExtentHtmlReporter(reportPath);

                htmlReporter.Config.Theme = Theme.Standard;
                extentReports.AddSystemInfo("Environment", appConfigMember.Environment);
                extentReports.AddSystemInfo("Application Url:", appConfigMember.Url);
                extentReports.AddSystemInfo("Application Test On:", appConfigMember.Browser.ToString());
                extentReports.AddSystemInfo("Application User Name:", appConfigMember.UserName);
                extentReports.AddSystemInfo("Application Password:", appConfigMember.Password);
                extentReports.AddSystemInfo("System User Name", Environment.UserName);
                extentReports.AddSystemInfo("Window", name + Is64BitOperatingSystem);
                extentReports.AddSystemInfo("Machine Name", Environment.MachineName);
                extentReports.AttachReporter(htmlReporter);
                htmlReporter.LoadConfig(projectPath + "Extent-config.xml");
            }
            catch (Exception ObjException)
            {
                Logger.Error(ObjException.Message);
                throw (ObjException);
            }

        }

        public ExtentTest CreateTest(string name, string description = "")
        {
            test = extentReports.CreateTest(name, description);
            return test;
        }

        public void ExtentReportsTearDown()
        {
            extentReports.Flush();
        }

        public MediaEntityModelProvider GetMediaEntityModelProvider()
        {
            return MediaEntityBuilder.CreateScreenCaptureFromPath(MakeAndSaveScreenshot()).Build();
        }

        public string MakeAndSaveScreenshot()
        {
            this.ScreenshotImagPath = appConfigMember.AutomationReportPath + "\\" + GenerateScreenshotName(TestContext.CurrentContext.Test.Name.Replace(" ", string.Empty)) + ".png";
            Rectangle bounds = Screen.GetBounds(Point.Empty);
            using (Bitmap bitmap = new Bitmap(bounds.Width, bounds.Height))
            {
                using (Graphics g = Graphics.FromImage(bitmap))
                {
                    g.CopyFromScreen(Point.Empty, Point.Empty, bounds.Size);
                }
                bitmap.Save(ScreenshotImagPath, ImageFormat.Png);
            }
            return this.ScreenshotImagPath;
        }

        private string GenerateScreenshotName(string fileName)
        {
            return fileName + string.Format("{0:_yyyy_MM_dd_hh_mm_ss}", DateTime.Now);
        }

        public void Pass(string MessageText, string AdditionalInformation = "", bool IsScreenshot = true)
        {
            Logger.Info(textInfo.ToTitleCase(MessageText), textInfo.ToTitleCase(AdditionalInformation));
            MediaEntityModelProvider provider = null;
            if (IsScreenshot)
            {
                provider = GetMediaEntityModelProvider();
            }
            test.Pass(textInfo.ToTitleCase(MessageText + "\n" + AdditionalInformation), provider);
        }

        public void Error(string MessageText, string AdditionalInformation = "", bool IsScreenshot = true)
        {
            string exceptionMessage = "";
            string stackTrace = "";
            MediaEntityModelProvider provider = null;
            if (IsScreenshot)
            {
                provider = GetMediaEntityModelProvider();
            }
            if (!String.IsNullOrEmpty(TestContext.CurrentContext.Result.Message))
            {
                exceptionMessage = TestContext.CurrentContext.Result.Message;
            }
            if (!String.IsNullOrEmpty(TestContext.CurrentContext.Result.StackTrace))
            {
                stackTrace = TestContext.CurrentContext.Result.StackTrace;
            }
            AdditionalInformation = "\n Additional Information:" + AdditionalInformation + "\n Exception Message:" + exceptionMessage + "\n Stack Trace:" + stackTrace;
            Logger.Error(textInfo.ToTitleCase(MessageText + "\n" + AdditionalInformation));
            test.Error(textInfo.ToTitleCase(MessageText + "\n" + AdditionalInformation), provider);

        }

        public void Warning(string MessageText, string AdditionalInformation = "", bool IsScreenshot = true)
        {
            MediaEntityModelProvider provider = null;
            if (IsScreenshot)
            {
                provider = GetMediaEntityModelProvider();
            }
            Logger.Warn(textInfo.ToTitleCase(MessageText + "\n" + AdditionalInformation));
            test.Warning(textInfo.ToTitleCase(MessageText + "\n" + AdditionalInformation), provider);
        }

        public void Skip(string MessageText, string AdditionalInformation = "", bool IsScreenshot = false)
        {
            MediaEntityModelProvider provider = null;
            if (IsScreenshot)
            {
                provider = GetMediaEntityModelProvider();
            }
            Logger.Debug(textInfo.ToTitleCase(MessageText + "\n" + AdditionalInformation));
            test.Skip(textInfo.ToTitleCase(MessageText + "\n" + AdditionalInformation), provider);
        }

        public void Info(string MessageText, string AdditionalInformation = "", bool IsScreenshot = false)
        {
            Logger.Info(textInfo.ToTitleCase(MessageText + "\n" + AdditionalInformation));
            MediaEntityModelProvider provider = null;
            if (IsScreenshot)
            {
                provider = GetMediaEntityModelProvider();
            }
            Logger.Info(textInfo.ToTitleCase(MessageText + "\n" + AdditionalInformation));
            test.Info(textInfo.ToTitleCase(MessageText + "\n" + AdditionalInformation), provider);
        }

        public void Debug(string MessageText, string AdditionalInformation = "", bool IsScreenshot = false)
        {
            MediaEntityModelProvider provider = null;
            if (IsScreenshot)
            {
                provider = GetMediaEntityModelProvider();
            }
            Logger.Debug(textInfo.ToTitleCase(MessageText + "\n" + AdditionalInformation));
            test.Debug(textInfo.ToTitleCase(MessageText + "\n" + AdditionalInformation), provider);
        }

        public void Log(Status status, string MessageText, string AdditionalInformation = "", bool IsScreenshot = false)
        {
            MediaEntityModelProvider provider = null;
            if (IsScreenshot)
            {
                provider = GetMediaEntityModelProvider();
            }
            Logger.Info(textInfo.ToTitleCase(MessageText + "\n" + AdditionalInformation));
            test.Log(status, textInfo.ToTitleCase(MessageText + "\n" + AdditionalInformation), provider);
        }

    }
}
