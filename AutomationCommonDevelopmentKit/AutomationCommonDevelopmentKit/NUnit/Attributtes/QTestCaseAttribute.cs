using AutomationCommonDevelopmentKit.NUnit.Arguments;
using NUnit.Framework;
using NUnit.Framework.Interfaces;
using System;

namespace AutomationCommonDevelopmentKit.NUnit.Attributtes
{
    [AttributeUsage(AttributeTargets.Method, AllowMultiple = true, Inherited = false)]
    public class QTestCaseAttribute : TestCaseAttribute, ITestAction
    {
        private readonly ArgumentProcessorsContainer argumentProcessorsContainer = new ArgumentProcessorsContainer();

        public string SkipClientLogOutput
        {
            get
            {
                return this.Properties.Get("SkipClientLogOutput") as string;
            }
            set
            {
                this.Properties.Set("SkipClientLogOutput", (object)value);
            }
        }
        public string Ticket
        {
            get
            {
                return this.Properties.Get("Ticket") as string;
            }
            set
            {
                this.Properties.Set("Ticket", (object)value);
            }
        }

        public string IssueId
        {
            get
            {
                return this.Properties.Get("IssueId") as string;
            }
            set
            {
                this.Properties.Set("IssueId", (object)value);
            }
        }

        public string IssueLink
        {
            get
            {
                return this.Properties.Get("IssueLink") as string;
            }
            set
            {
                this.Properties.Set("IssueLink", (object)value);
            }
        }

        public string TestCategory
        {
            get
            {
                return this.Properties.Get("TestCategory") as string;
            }
            set
            {
                this.Properties.Set("TestCategory", (object)value);
            }
        }

        public string PageCategory
        {
            get
            {
                return this.Properties.Get("PageCategory") as string;
            }
            set
            {
                this.Properties.Set("PageCategory", (object)value);
            }
        }

        public string ModuleCategory
        {
            get
            {
                return this.Properties.Get("ModuleCategory") as string;
            }
            set
            {
                this.Properties.Set("ModuleCategory", (object)value);
            }
        }

        public ActionTargets Targets => ActionTargets.Test;

        public QTestCaseAttribute(): base(new object[0])
        {
        }

        public QTestCaseAttribute(params object[] arguments) : base(arguments)
        {
            argumentProcessorsContainer.ApplyProcessors(Arguments);
        }

        public QTestCaseAttribute(object arg) : base(arg)
        {
            argumentProcessorsContainer.ApplyProcessors(Arguments);
        }

        public QTestCaseAttribute(object arg1, object arg2) : base(arg1, arg2)
        {
            argumentProcessorsContainer.ApplyProcessors(Arguments);
        }

        public QTestCaseAttribute(object arg1, object arg2, object arg3) : base(arg1, arg2, arg3)
        {
        }

        public void BeforeTest(ITest test)
        {
            //
        }

        public void AfterTest(ITest test)
        {
            //
        }
    }
}
