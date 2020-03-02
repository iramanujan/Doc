using System;

namespace Selenium.Framework.Development.Kit.Helper.Utils
{
    public class TimeUtil
    {
        public static TimeSpan GetCurrentTime()
        {
            return DateTime.Now.TimeOfDay;
        }

        public static int GetTimeDifferenceInSecond(TimeSpan StartTime, TimeSpan EndTime)
        {
            return EndTime.Seconds - StartTime.Seconds;
        }

        public static int GetTimeDifferenceInMinutes(TimeSpan StartTime, TimeSpan EndTime)
        {
            return EndTime.Minutes - StartTime.Minutes;
        }

        public static string GetTimeStamp()
        {
            return string.Format("{0:_yyyy_MM_dd_hh_mm_ss}", DateTime.Now);
        }
    }
}
