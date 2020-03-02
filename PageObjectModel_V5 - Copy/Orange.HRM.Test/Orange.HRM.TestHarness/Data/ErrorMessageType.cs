namespace Orange.HRM.TestHarness.Data
{
    public enum ErrorMessageType
    {
        [System.ComponentModel.Description("Username cannot be empty")]
        UserNameEmpty = 0,

        [System.ComponentModel.Description("Password cannot be empty")]
        PasswordEmpty = 1,

        [System.ComponentModel.Description("Invalid credentials")]
        InvalidCredentials = 2
    }
}
