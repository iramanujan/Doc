using Selenium.Framework.Development.Kit.Helper.Report;

namespace Orange.HRM.TestHarness.Core
{

    public class BasePageValidator<TM> where TM : BasePageElementMap, new()
    {
        public Report ObjReport => Report.ReportInstance;
        protected TM Map
        {
            get
            {
                return new TM();
            }
        }
    }
}
