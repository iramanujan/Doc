using System;
using System.Linq.Expressions;

namespace Selenium.Framework.Development.Kit.Helper.Attributes
{
    [AttributeUsage(AttributeTargets.Field, AllowMultiple = true)]
    public sealed class StringValueAttribute : Attribute
    {
        #region - Properties -
        public string Value { get; private set; }
        #endregion

        #region - Constructors -
        public StringValueAttribute(string value)
        {
            this.Value = value;
        }

        #endregion

        #region - Methods -
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1006:DoNotNestGenericTypesInMemberSignatures")]
        public static string Get<T>(Expression<Func<T>> propertyLambda)
        {
            return (string)AttributeUtils.Get(propertyLambda, typeof(StringValueAttribute), "Value");
        }

        #endregion
    }
}
