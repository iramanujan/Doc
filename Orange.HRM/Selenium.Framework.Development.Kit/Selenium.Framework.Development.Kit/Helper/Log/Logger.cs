using log4net;
using System;
using System.Linq;

namespace Selenium.Framework.Development.Kit.Helper.Log
{
    public class Logger
    {
        private static readonly ILog log = LogManager.GetLogger(typeof(Logger));


        public static void Debug(string message, params object[] args)
        {
            var msg = args.Any() ? String.Format(message, args) : message;
            LogToConsoleWithTimeStamp("Debug: " + msg);
            log.Debug(msg);
        }

        public static void Error(string message, params object[] args)
        {
            var msg = args.Any() ? string.Format(message, args) : message;
            LogToConsoleWithTimeStamp("Error: " + msg);
            log.Error(msg);
        }

        public static void Fatal(string message, params object[] args)
        {
            var msg = string.Format(message, args);
            LogToConsoleWithTimeStamp("Fatal: " + msg);
            log.Fatal(msg);
        }

        public static void Info(string message, params object[] args)
        {
            var msg = string.Format(message, args);
            LogToConsoleWithTimeStamp("Info: " + msg);
            log.Info(msg);
        }

        public static void Warn(string message, params object[] args)
        {
            var msg = string.Format(message, args);
            LogToConsoleWithTimeStamp("Warn: " + msg);
            log.Warn(msg);
        }

        private static void LogToConsoleWithTimeStamp(string value)
        {
            Console.WriteLine("[{0}] {1}", DateTime.UtcNow, value);
        }

    }
}
