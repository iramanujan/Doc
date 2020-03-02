using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;

namespace Selenium.Framework.Development.Kit.Helper.Utils
{
    public class ZipUtils
    {
        public static List<String> GetContentFileNames(string pathToZip)
        {
            List<String> files = new List<String>();
            using (ZipArchive archive = ZipFile.OpenRead(pathToZip))
            {
                foreach (ZipArchiveEntry entry in archive.Entries)
                {
                    files.Add(entry.FullName);
                }
            }
            return files;
        }

        public static IList<String> GetEmptyFiles(string pathToZip)
        {
            List<String> emptyFiles = new List<string>();
            using (ZipArchive archive = ZipFile.OpenRead(pathToZip))
            {
                foreach (ZipArchiveEntry entry in archive.Entries)
                {
                    if (entry.Length == 0)
                    {
                        emptyFiles.Add(entry.Name);
                    }
                }
            }
            return emptyFiles;
        }

        public static void AddFile(string zipPath, string filePath, CompressionLevel compression = CompressionLevel.Optimal)
        {
            using (ZipArchive archive = ZipFile.Open(zipPath, ZipArchiveMode.Update))
            {
                archive.CreateEntryFromFile(filePath, Path.GetFileName(filePath), compression);
            }
        }
    }
}