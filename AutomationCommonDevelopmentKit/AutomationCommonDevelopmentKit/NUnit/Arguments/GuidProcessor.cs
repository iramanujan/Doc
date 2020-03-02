using System;

namespace AutomationCommonDevelopmentKit.NUnit.Arguments
{
    public class GuidProcessor : IArgumentsProcessor
    {
        private Lazy<string> guidLazy = new Lazy<string>(Guid.NewGuid().ToString);
        private const string GUIDPLACE_HOLDER_CACHED = "$$GUID$$";
        private const string GUIDPLACE_HOLDER_NEW = "$$GUIDNEW$$";

        public object Process(object argument)
        {
            var stringArgument = argument as string;
            if (stringArgument == null) return argument;
            if (stringArgument.Contains(GUIDPLACE_HOLDER_CACHED))
            {
                return argument.ToString().Replace(GUIDPLACE_HOLDER_CACHED, guidLazy.Value);
            }
            if (stringArgument.Contains(GUIDPLACE_HOLDER_NEW))
            {
                return argument.ToString().Replace(GUIDPLACE_HOLDER_NEW, Guid.NewGuid().ToString());
            }
            return argument;
        }
    }
}
