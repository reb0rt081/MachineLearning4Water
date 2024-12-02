using MachineLearning4Water.Tools;

namespace MachineLearning4Water.Python.U.Test
{
    [TestClass]
    public class PythonTests
    {
        [TestMethod]
        public void ExecutePythonEmbeddedScriptSum()
        {
            Assert.AreEqual(3, PythonRunner.RunAsEmbeddedPythonMethod("BaseLib.py", "Sum", dyn => int.Parse(dyn.ToString()), 1, 2));
        }

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
            List<List<double>> solution = PythonRunner.RunPythonMethod("BaseLib.py", "MatrixSum", result => PythonHelper.ConvertDynamicToMatrix(result), matrix1, matrix2);

            // Solution:
            // | 6  8  |
            // | 10 12 |
            Assert.AreEqual(6, solution[0][0]);
            Assert.AreEqual(8, solution[0][1]);
            Assert.AreEqual(10, solution[1][0]);
            Assert.AreEqual(12, solution[1][1]);
        }

        [TestMethod]
        public void ExecutePythonScriptMatrixMult()
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
            List<List<double>> solution = PythonRunner.RunPythonMethod("BaseLib.py", "MatrixMult", result => PythonHelper.ConvertDynamicToMatrix(result), matrix1, matrix2);

            // Solution:
            // | 19 22 |
            // | 43 50 |
            Assert.AreEqual(19, solution[0][0]);
            Assert.AreEqual(22, solution[0][1]);
            Assert.AreEqual(43, solution[1][0]);
            Assert.AreEqual(50, solution[1][1]);
        }

        [TestMethod]
        public void ExecutePythonScriptMatrixDeterminant()
{
    // Define the 2x2 matrix
    var matrix2x2 = new List<List<double>> {
        new List<double> { 1, 2 },
        new List<double> { 3, 4 }
    };

    // Calculate determinant for 2x2 matrix
    int solution2x2 = PythonRunner.RunPythonMethod("BaseLib.py", "MatrixDeterminant", 
        dyn => int.Parse(dyn.ToString()), matrix2x2);

    // Validate the result
    Assert.AreEqual(-2, solution2x2);

    // Define the 3x3 matrix
    var matrix3x3 = new List<List<double>> {
        new List<double> { 6, 1, 1 },
        new List<double> { 4, -2, 5 },
        new List<double> { 2, 8, 7 }
    };

    // Calculate determinant for 3x3 matrix
    int solution3x3 = PythonRunner.RunPythonMethod("BaseLib.py", "MatrixDeterminant", 
        dyn => int.Parse(dyn.ToString()), matrix3x3);

    // Validate the result
    Assert.AreEqual(-306, solution3x3);

    // Define the pre-determined 10x10 matrix
    var matrix10x10 = new List<List<double>> {
        new List<double> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 },
        new List<double> { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 },
        new List<double> { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 },
        new List<double> { 11, 10, 9, 8, 7, 6, 5, 4, 3, 2 },
        new List<double> { 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 },
        new List<double> { 12, 11, 10, 9, 8, 7, 6, 5, 4, 3 },
        new List<double> { 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 },
        new List<double> { 13, 12, 11, 10, 9, 8, 7, 6, 5, 4 },
        new List<double> { 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 },
        new List<double> { 14, 13, 12, 11, 10, 9, 8, 7, 6, 5 }
    };

    // Calculate determinant for 10x10 matrix
    int solution10x10 = PythonRunner.RunPythonMethod("BaseLib.py", "MatrixDeterminant",
        dyn => int.Parse(dyn.ToString()), matrix10x10);

    // Validate the result (determinant is 0)
    Assert.AreEqual(0, solution10x10);
}
     
        //  TODO add a test for each new method: included the ones in MachineLearningTechni
    }
}
