using AutomationCommonDevelopmentKit.NUnit.Arguments;
using NUnit.Framework;
using System;
using System.Configuration;

namespace AutomationCommonDevelopmentKit.NUnit.Attributtes
{
    [AttributeUsage(AttributeTargets.Class, AllowMultiple = true, Inherited = true)]
    public class QTestFixtureAttribute : TestFixtureAttribute
    {
        private readonly ArgumentProcessorsContainer argumentProcessorsContainer = new ArgumentProcessorsContainer();


        public string AllowedEnvironments
        {
            get { throw new NotImplementedException(); }
            set
            {
                if (String.IsNullOrWhiteSpace(value)) return;
                if (!value.Contains(ConfigurationManager.AppSettings["Environment"]))
                {
                    IgnoreReason = $"Test is not allowed to run on current Environment. Allowed environments are: {value}";
                }
            }
        }

        public QTestFixtureAttribute()
        {
        }

        public QTestFixtureAttribute(params object[] arguments) : base(arguments)
        {
            argumentProcessorsContainer.ApplyProcessors(Arguments);
        }
    }
}
