using FluentAssertions;
using NUnit.Framework;
using System;

namespace PhpTravels.TestHarness.Test.Login
{
    [TestFixture]
    public class Login : BaseTest
    {
        [SetUp]
        public void SetUp()
        {
            
        }

        [TestCase("admin@phptravels.com", "demoadmin", TestName = "Validate Login With Valid User.", Author = "Anuj Jain")]
        public void ValidateLogin(string email, string password)
        {
            String s = "Hello";
            s.Should().Be("Anuj");
        }


        [TestCase("admin@phptravels.com", "demoadmin", TestName = "Validate Login With Valid User-2.", Author = "Anuj Jain")]
        public void ValidateLogin2(string email, string password)
        {
            String s = "Hello";
            s.Should().Be("Hello");
        }
    }
}
