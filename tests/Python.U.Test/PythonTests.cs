namespace MachineLearning4Water.Python.U.Test
{
    [TestClass]
    public class PythonTests
    {
        [TestMethod]
        public void ExecutePythonScript()
        {
            Assert.AreEqual(3, PythonRunner.RunPythonMethod("BaseLib.py", "Sum", int.Parse, 1, 2));
        }
    }
}