using System.Drawing;
using XnaFan.ImageComparison;

namespace Selenium.Framework.Development.Kit.Helper.Utils
{
    public class ImageComparison
    {
        public static float CompareImages(string image1Path, Image image2, byte threshold = 3)
        {
            return image2.PercentageDifference(Image.FromFile(image1Path), threshold);
        }

        public static float CompareImages(string image1Path, string image2Path, byte threshold = 3)
        {
            return ImageTool.GetPercentageDifference(image1Path, image2Path, threshold);
        }

        public static float CompareImages(Image image1, Image image2, byte threshold = 3)
        {
            return image1.PercentageDifference(image2, threshold);
        }
    }
}
