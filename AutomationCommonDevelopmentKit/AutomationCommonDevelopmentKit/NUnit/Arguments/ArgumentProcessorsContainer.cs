using System.Collections.Generic;

namespace AutomationCommonDevelopmentKit.NUnit.Arguments
{
    public class ArgumentProcessorsContainer
    {
        private readonly List<IArgumentsProcessor> _argumentsProcessors = new List<IArgumentsProcessor>();

        public ArgumentProcessorsContainer()
        {
            _argumentsProcessors.Add(new GuidProcessor());
        }

        public ArgumentProcessorsContainer(params IArgumentsProcessor[] argumentsProcessors)
        {
            this._argumentsProcessors.AddRange(argumentsProcessors);
        }

        public void ApplyProcessors(object[] arguments)
        {
            for (var i = 0; i < arguments.Length; i++)
            {
                foreach (var argumentReplacerAction in _argumentsProcessors)
                {
                    arguments[i] = argumentReplacerAction.Process(arguments[i]);
                }
            }
        }
    }
}
