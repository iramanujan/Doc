using System;
using System.Collections.Generic;
using System.Text;

namespace Selenium.Framework.Development.Kit.Helper.Utils
{
    public static class RandomUtils
    {
        private static Random rnd = new Random();
        private const string DefaultDomain = "dispostable.com";
        private const string DefaultEmailDomain = "gmail.com";


        public static T GetRandomValueFromEnum<T>() where T : struct, IConvertible
        {
            Array values = Enum.GetValues(typeof(T));
            return (T)values.GetValue(rnd.Next(values.Length));
        }

        public static decimal RandomDecimal(int min, int max)
        {
            var integerPart = (decimal)rnd.Next(min, max);
            var fractionPart = (decimal)rnd.Next(0, 99) / 100;
            return integerPart + fractionPart;
        }

        public static double RandomDouble(int min, int max)
        {
            var integerPart = (double)rnd.Next(min, max);
            var fractionPart = (double)rnd.Next(0, 99) / 100;
            return integerPart + fractionPart;
        }

        public static int RandomNumeric(int min, int max)
        {
            return rnd.Next(min, max);
        }

        public static string RandomizeNumericString(int size)
        {
            const string chars = "0123456789";
            string randomNumericString = RandomizeString(size, chars);

            while (randomNumericString.StartsWith("0", StringComparison.CurrentCultureIgnoreCase))
            {
                randomNumericString = randomNumericString.Replace("0", RandomizeString(1, chars));
            }

            return randomNumericString;
        }

        public static string RandomPhoneNumber()
        {
            return string.Format("{0}-{1}-{2:D4}", rnd.Next(200, 1000), rnd.Next(200, 1000), rnd.Next(0, 10000));
        }

        public static string RandomizeAlphabeticalString(int size)
        {
            const string chars = "abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
            return RandomizeString(size, chars);
        }

        public static string RandomizeAlphanumericString(int size)
        {
            const string chars = "abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            return RandomizeString(size, chars);
        }

        public static string RandomizeSpecialSymbolsString(int size)
        {
            const string chars = "~`@#$%^&*()_+!№;%:?*";
            return RandomizeString(size, chars);
        }

        public static string RandomizeNotEnglishString(int size)
        {
            const string chars =
                "¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýÿАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя";
            return RandomizeString(size, chars);
        }

        public static string RandomizeSpacesString(int size)
        {
            const string chars = " ";
            return RandomizeString(size, chars);
        }

        public static string RandomizeAlphabeticalString()
        {
            return RandomizeAlphabeticalString(RandomNumeric(4, 12));
        }

        public static string RandomDomain(int numberOfLevels)
        {
            var randomDomainName = new StringBuilder();

            for (int i = 0; i < numberOfLevels - 1; i++)
            {
                randomDomainName.AppendFormat("{0}.", RandomizeAlphabeticalString());
            }

            randomDomainName.Append(DefaultEmailDomain);

            return randomDomainName.ToString();
        }

        public static string RandomDefaultDomainEmail(string prefix)
        {
            var email = $"{prefix}-{RandomizeAlphabeticalString(7)}@{DefaultDomain}";

            return email;
        }

        public static string RandomEmail()
        {
            var randomEmail = $"{RandomizeAlphabeticalString()}@{RandomDomain(2)}";

            return randomEmail;
        }

        public static IEnumerable<string> MultipleRandomEmails(int count, string prefix = "test")
        {
            var randomEmails = new List<string>();
            for (var i = 0; i < count; i++)
            {
                randomEmails.Add(RandomDefaultDomainEmail(prefix));
            }

            return randomEmails;
        }

        public static bool RandomBool()
        {
            return rnd.NextDouble() > 0.5;
        }

        private static string RandomizeString(int size, string charsForRandom)
        {
            var buffer = new char[size];

            for (int i = 0; i < size; i++)
            {
                buffer[i] = charsForRandom[rnd.Next(charsForRandom.Length)];
            }
            return new string(buffer);
        }

        public static string RadomSentence(int? wordCount = null)
        {
            var lorem = new Bogus.DataSets.Lorem();

            return lorem.Sentence(wordCount);
        }

        public static String GetTimestamp()
        {
            return DateTime.Now.ToString("_yyyyMMddHHmmssffff");
        }
    }

}
