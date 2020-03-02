using NUnit.Framework;
using NUnit.Framework.Interfaces;
using NUnit.Framework.Internal;
using System;

namespace Selenium.Framework.Development.Kit.Helper.NUnit.Attributtes
{

    [AttributeUsage(AttributeTargets.Assembly | AttributeTargets.Class | AttributeTargets.Method, AllowMultiple = false,
        Inherited = true)]
    public sealed class ParallelizableInheritedAttribute : PropertyAttribute, IApplyToContext
    {
        private ParallelScope _scope;


        public ParallelizableInheritedAttribute() : this(ParallelScope.Self)
        {
        }

        public ParallelizableInheritedAttribute(ParallelScope scope) : base()
        {
            _scope = scope;
            Properties.Add(PropertyNames.ParallelScope, scope);
        }

        #region IApplyToContext Interface
        public void ApplyToContext(TestExecutionContext context)
        {
            context.ParallelScope = _scope & ~ParallelScope.Self;
        }

        #endregion
    }
}
