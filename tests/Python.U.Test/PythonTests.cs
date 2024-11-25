using MachineLearning4Water.Tools;

namespace MachineLearning4Water.Python.U.Test
{
    [TestClass]
    public class PythonTests
    {
        [TestMethod]
        public void ExecutePythonScriptSum()
        {
            Assert.AreEqual(3, PythonRunner.RunPythonMethod("BaseLib.py", "Sum", dyn => int.Parse(dyn.ToString()), 1, 2));
        }

        [TestMethod]
        public void ExecutePythonScriptMatrixSum()
        {
            // Define the matrices
            // | 1 2 |
            // | 3 4 |
            var matrix1 = new List<List<double>> {
                new List<double> { 1, 2 },
                new List<double> { 3, 4 }
            };

            // | 5 6 |
            // | 7 8 |
            var matrix2 = new List<List<double>> {
                new List<double> { 5, 6 },
                new List<double> { 7, 8 }
            };
            List<List<double>> solution = new List<List<double>>();
            PythonRunner.RunPythonMethod("BaseLib.py", "MatrixSum", result => solution = PythonHelper.ConvertDynamicToMatrix(result), matrix1, matrix2);

            // Solution:
            // | 6  8  |
            // | 10 12 |
            Assert.AreEqual(6, solution[0][0]);
            Assert.AreEqual(8, solution[0][1]);
            Assert.AreEqual(10, solution[1][0]);
            Assert.AreEqual(12, solution[1][1]);
        }
    }
}