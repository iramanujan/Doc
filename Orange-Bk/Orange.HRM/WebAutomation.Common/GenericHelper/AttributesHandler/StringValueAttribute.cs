using System;
using System.Linq.Expressions;

namespace WebAutomation.Common.GenericHelper.AttributesHandler
{
    [AttributeUsage(AttributeTargets.Field, AllowMultiple = true)]
    public sealed class StringValueAttribute : Attribute
    {

        public string Value { get; private set; }

        public StringValueAttribute(string value)
        {
            this.Value = value;
        }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1006:DoNotNestGenericTypesInMemberSignatures")]
        public static string Get<T>(Expression<Func<T>> propertyLambda)
        {
            return (string)AttributeHelper.Get(propertyLambda, typeof(StringValueAttribute), "Value");
        }

    }
}
