﻿using Microsoft.VisualBasic.FileIO;
using Selenium.Framework.Development.Kit.Helper.Wait;
using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;

namespace Selenium.Framework.Development.Kit.Helper.Utils
{
    public class FileUtils
    {
        public static void WaitForFileCreated(string path, TimeSpan timeSpan)
        {
            Waiter.SpinWait(() => File.Exists(path), timeSpan);
        }

        public static void WaitForFileCreated(string path)
        {
            WaitForFileCreated(path, TimeSpan.FromMinutes(3));
        }

        public static void WaitForFileReachSize(string path, long size, TimeSpan timeSpan)
        {
            WaitForFileCreated(path);
            Waiter.SpinWait(() => new FileInfo(path).Length == size, timeSpan);
        }

        public static void WaitForFileReachSize(string path, long size)
        {
            WaitForFileReachSize(path, size, TimeSpan.FromMinutes(10));
        }

        public static string GetCurrentlyExecutingDirectory()
        {
            return Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location) + Path.DirectorySeparatorChar;
        }

        public static IEnumerable<string[]> GetCsvFields(string path)
        {
            WaitForFileCreated(path);

            using (TextFieldParser parser = new TextFieldParser(path))
            {
                parser.TextFieldType = FieldType.Delimited;
                parser.SetDelimiters(",");
                while (!parser.EndOfData)
                {
                    yield return parser.ReadFields();
                }
            }
        }
    }
}
