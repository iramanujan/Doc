using System;
using System.Linq;
using NUnit.Framework.Interfaces;
using NUnit.Framework.Internal;
using Selenium.Framework.Development.Kit.Helper.NUnit.Arguments;

namespace Selenium.Framework.Development.Kit.Helper.NUnit.Attributtes
{
    public class QTestCaseData : TestCaseParameters
    {
        private readonly ArgumentProcessorsContainer _argumentProcessorsContainer =
            new ArgumentProcessorsContainer();
        /// <summary>
        /// Initializes a new instance of the <see cref="QTestCaseData"/> class.
        /// </summary>
        /// <param name="arg">The argument.</param>
        public QTestCaseData(object arg)
            : base(new[] { arg })
        {
            _argumentProcessorsContainer.ApplyProcessors(Arguments);

        }

        /// <summary>
        /// Initializes a new instance of the <see cref="QTestCaseData"/> class.
        /// </summary>
        /// <param name="arg1">The arg1.</param>
        /// <param name="arg2">The arg2.</param>
        public QTestCaseData(object arg1, object arg2)
            : base(new[] { arg1, arg2 })
        {
            _argumentProcessorsContainer.ApplyProcessors(Arguments);

        }

        /// <summary>
        /// Initializes a new instance of the <see cref="QTestCaseData"/> class.
        /// </summary>
        /// <param name="arg1">The arg1.</param>
        /// <param name="arg2">The arg2.</param>
        /// <param name="arg3">The arg3.</param>
        public QTestCaseData(object arg1, object arg2, object arg3)
            : base(new[] { arg1, arg2, arg3 })
        {
            _argumentProcessorsContainer.ApplyProcessors(Arguments);

        }

        /// <summary>
        /// Initializes a new instance of the <see cref="QTestCaseData"/> class.
        /// </summary>
        /// <param name="args">The arguments.</param>
        public QTestCaseData(params object[] args)
            : base(args ?? new object[] { null })
        {
            _argumentProcessorsContainer.ApplyProcessors(Arguments);

        }

        /// <summary>
        /// Sets the ticket.
        /// </summary>
        /// <param name="description">The description.</param>
        public QTestCaseData SetTicket(string description)
        {
            Properties.Set("Ticket", description);
            return this;
        }

        /// <summary>
        /// Sets the categories.
        /// </summary>
        /// <param name="categories">The categories.</param>
        public QTestCaseData SetCategories(params string[] categories)
        {
            foreach (var category in categories)
            {
                Properties.Add("Category", category);
            }
            return this;
        }

        /// <summary>
        /// Returnses the specified result.
        /// </summary>
        /// <param name="result">The result.</param>
        public QTestCaseData Returns(object result)
        {
            ExpectedResult = result;
            return this;
        }

        /// <summary>
        /// Sets the name.
        /// </summary>
        /// <param name="name">The name.</param>
        public QTestCaseData SetName(string name)
        {
            TestName = name;
            return this;
        }

        /// <summary>
        /// Sets the description.
        /// </summary>
        /// <param name="description">The description.</param>
        public QTestCaseData SetDescription(string description)
        {
            Properties.Set("Description", description);
            return this;
        }

        /// <summary>
        /// Sets the author.
        /// </summary>
        /// <param name="author">The author.</param>
        public QTestCaseData SetAuthor(string author)
        {
            Properties.Set("Author", author);
            return this;
        }

        /// <summary>
        /// Sets the property.
        /// </summary>
        /// <param name="propName">Name of the property.</param>
        /// <param name="propValue">The property value.</param>
        public QTestCaseData SetProperty(string propName, string propValue)
        {
            Properties.Add(propName, propValue);
            return this;
        }

        /// <summary>
        /// Sets the property.
        /// </summary>
        /// <param name="propName">Name of the property.</param>
        /// <param name="propValue">The property value.</param>
        public QTestCaseData SetProperty(string propName, int propValue)
        {
            Properties.Add(propName, propValue);
            return this;
        }

        /// <summary>
        /// Sets the property.
        /// </summary>
        /// <param name="propName">Name of the property.</param>
        /// <param name="propValue">The property value.</param>
        public QTestCaseData SetProperty(string propName, double propValue)
        {
            Properties.Add(propName, propValue);
            return this;
        }

        /// <summary>
        /// Explicits this instance.
        /// </summary>
        public QTestCaseData Explicit()
        {
            RunState = RunState.Explicit;
            return this;
        }

        /// <summary>
        /// Explicits the specified reason.
        /// </summary>
        /// <param name="reason">The reason.</param>
        public QTestCaseData Explicit(string reason)
        {
            RunState = RunState.Explicit;
            Properties.Set("_SKIPREASON", reason);
            return this;
        }

        /// <summary>
        /// Ignores the specified reason.
        /// </summary>
        /// <param name="reason">The reason.</param>
        public QTestCaseData Ignore(string reason)
        {
            RunState = RunState.Ignored;
            Properties.Set("_SKIPREASON", reason);
            return this;
        }

    }
}
