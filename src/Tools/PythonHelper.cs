using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
using System;
using System.Collections.Generic;
using System.IO;

namespace MachineLearning4Water.Tools
{
    public class PythonHelper
    {
        public static TOut ExecutePythonMethod<TOut>(string pythonFilePath, string methodName, Func<dynamic, TOut> dataConversionResult, params object[] args)
        {
            //string fileName = @"C:\sample_script.py";

            // Create a Python engine
            ScriptEngine engine = Python.CreateEngine();

            // Load the Python script
            var scriptScope = engine.CreateScope();
            string script = File.ReadAllText(pythonFilePath);
            engine.Execute(script, scriptScope);

            // Get the Python function
            dynamic pythonFunction = scriptScope.GetVariable(methodName);

            // Call the Python function with unpacked arguments
            dynamic result = engine.Operations.Invoke(pythonFunction, args);

            return dataConversionResult(result);
        }

        public static List<List<double>> ConvertDynamicToMatrix(dynamic pythonResult)
        {
            var matrix = new List<List<double>>();

            foreach (var row in pythonResult)
            {
                var tempRow = new List<double>();

                foreach (var value in row)
                {
                    tempRow.Add((double)value); // Convert Python object to C# int
                }

                matrix.Add(tempRow);
            }

            return matrix;
        }
    }
}
