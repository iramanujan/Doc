using Automation.Common.Log;
using AventStack.ExtentReports;
using AventStack.ExtentReports.Reporter;
using AventStack.ExtentReports.Reporter.Configuration;
using NUnit.Framework;
using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Windows.Forms;
using WebAutomation.Common.AppConfigHandler;

namespace WebAutomation.Common.GenericHelper.ReportHandler
{
    public sealed class Report
    {
        public ExtentReports extentReports = null;
        public ExtentTest test = null;
        private static readonly ToolConfigMember appConfigMember = ToolConfigReader.GetToolConfig();

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
                extentReports.AddSystemInfo("User Name", Environment.UserName);
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

    }
}