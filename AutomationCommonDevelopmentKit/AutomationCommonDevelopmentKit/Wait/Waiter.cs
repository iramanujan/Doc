using AutomationCommonDevelopmentKit.Configuration;
using System;
using System.Diagnostics;
using System.Threading;
using NInternal = NUnit.Framework.Internal;

namespace AutomationCommonDevelopmentKit.Wait
{
    public class Waiter
    {
        private static readonly AppConfigMember appConfigMember = AppConfigReader.GetToolConfig();
        private static Report.Report ObjReport => Report.Report.ReportInstance;
        #region Object
        private readonly TimeSpan _checkInterval;
        private readonly Stopwatch _stopwatch;
        private readonly TimeSpan _timeout;
        private Exception lastException;
        #endregion

        #region Constructors
        private Waiter() : this(TimeSpan.FromSeconds(appConfigMember.ObjectTimeout), TimeSpan.FromSeconds(appConfigMember.PollingInterval))
        {
        }

        private Waiter(TimeSpan timeout) : this(timeout, TimeSpan.FromSeconds(appConfigMember.PollingInterval))
        {
        }

        private Waiter(TimeSpan timeout, TimeSpan checkInterval)
        {
            this._timeout = timeout;
            this._checkInterval = checkInterval;
            this._stopwatch = Stopwatch.StartNew();
        }
        #endregion

        #region Public Properties
        public bool IsSatisfied { get; private set; } = true;
        #endregion

        #region Public Methods and Operators
        public static bool SpinWait(Func<bool> condition, TimeSpan? timeout = null)
        {
            timeout = timeout ?? TimeSpan.FromSeconds(1);
            return SpinWait(condition, (TimeSpan)timeout, TimeSpan.FromSeconds(1));
        }

        public static bool SpinWait(Func<bool> condition, TimeSpan timeout, TimeSpan pollingInterval)
        {
            return WithTimeout(timeout, pollingInterval).WaitFor(condition).IsSatisfied;
        }

        public static void SpinWaitEnsureSatisfied(Func<bool> condition, string exceptionMessage, int timeOutSeconds = 30, int pollIntervalSeconds = 1)
        {
            WithTimeout(TimeSpan.FromSeconds(timeOutSeconds), TimeSpan.FromSeconds(pollIntervalSeconds)).WaitFor(condition).EnsureSatisfied(exceptionMessage);
        }

        public static void SpinWaitEnsureSatisfied(Func<bool> condition, string passMessage, string failMessage, int timeOutSeconds = 30, int pollIntervalSeconds = 1)
        {
            WithTimeout(TimeSpan.FromSeconds(timeOutSeconds), TimeSpan.FromSeconds(pollIntervalSeconds)).WaitFor(condition).EnsureSatisfied(passMessage, failMessage);
        }

        public static void SpinWaitEnsureSatisfied(Func<bool> condition, TimeSpan timeout, TimeSpan pollingInterval, string exceptionMessage)
        {
            WithTimeout(timeout, pollingInterval).WaitFor(condition).EnsureSatisfied(exceptionMessage);
        }
        public static void SpinWaitEnsureSatisfied(Func<bool> condition, TimeSpan timeout, TimeSpan pollingInterval, string passMessage, string failMessage)
        {
            WithTimeout(timeout, pollingInterval).WaitFor(condition).EnsureSatisfied(passMessage, failMessage);
        }

        public static Waiter WithTimeout(TimeSpan timeout, TimeSpan pollingInterval)
        {
            return new Waiter(timeout, pollingInterval);
        }

        public static Waiter WithTimeout(TimeSpan timeout)
        {
            return new Waiter(timeout);
        }

        public void EnsureSatisfied()
        {
            if (!this.IsSatisfied)
            {
                string message = string.Empty;
                if (this.lastException != null)
                {
                    message = "Check inner waiter exception.";
                }
                throw new TimeoutException(message, this.lastException);
            }
        }

        public void EnsureSatisfied(string message)
        {
            if (!this.IsSatisfied)
            {
                if (this.lastException != null)
                {
                    message += " |Check inner waiter exception.";
                }
                throw new TimeoutException(message, this.lastException);
            }

        }


        public void EnsureSatisfied(string passMessage, string failMessage)
        {
            if (!this.IsSatisfied)
            {
                if (this.lastException != null)
                {
                    failMessage += "\n ***** Check inner waiter exception. *****\n";
                }
                //ObjReport.Error(failMessage, new TimeoutException(failMessage, this.lastException).Message);
                throw new TimeoutException(failMessage, this.lastException);
            }
            else
            {
                ObjReport.Pass(passMessage);
            }

        }
        public static void Wait(TimeSpan timeSpan)
        {
            Thread.Sleep(timeSpan);
        }


        public Waiter WaitFor(Func<bool> condition)
        {
            using (new NInternal.TestExecutionContext.IsolatedContext())
            {
                if (!this.IsSatisfied)
                {
                    return this;
                }

                while (!this.Try(condition))
                {
                    var sleepAmount = Min(this._timeout - this._stopwatch.Elapsed, this._checkInterval);

                    if (sleepAmount < TimeSpan.Zero)
                    {
                        this.IsSatisfied = false;
                        break;
                    }
                    Thread.Sleep(sleepAmount);
                }

                return this;
            }
        }

        private bool Try(Func<bool> condition)
        {
            try
            {
                return condition();
            }
            catch (Exception ex)
            {
                this.lastException = ex;
                return false;
            }
        }

        private static T Min<T>(T left, T right) where T : IComparable<T>
        {
            return left.CompareTo(right) < 0 ? left : right;
        }

        #endregion
    }
}
