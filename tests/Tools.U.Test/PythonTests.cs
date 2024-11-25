using Community.CsharpSqlite;

namespace MachineLearning4Water.Tools.U.Test
{
    [TestClass]
    public class PythonTests
    {
        [TestMethod]
        public void ExecutePythonScript()
        {
            Assert.AreEqual(3, PythonHelper.ExecutePythonMethod(@"C:\Users\rbo\Documents\GIT\MachineLearning4Water\src\Python\BaseLib.py", "Sum", int.Parse, 1, 2));
        }
    }
}