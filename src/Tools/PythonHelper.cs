using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
using System;
using System.IO;

namespace MachineLearning4Water.Tools
{
    public class PythonHelper
    {
        public static TOut ExecutePythonMethod<TOut>(string pythonFilePath, string methodName, Func<string, TOut> dataConversionResult, params object[] args)
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

            return dataConversionResult((result as object)?.ToString() ?? string.Empty);
        }
    }
}
