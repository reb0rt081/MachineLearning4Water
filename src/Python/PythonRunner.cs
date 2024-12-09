using System;
using System.IO;
using System.Reflection;

using MachineLearning4Water.Tools;

namespace MachineLearning4Water.Python
{
    public class PythonRunner
    {
        public static TOut RunPythonMethod<TOut>(string pythonScriptName, string methodName, Func<dynamic, TOut> dataConversionResult, params object[] args)
        {
            return PythonHelper.ExecutePythonMethod($"./Scripts/{pythonScriptName}", methodName, dataConversionResult, args);
        }

        public static TOut RunAsEmbeddedPythonMethod<TOut>(string pythonScriptName, string methodName, Func<dynamic, TOut> dataConversionResult, params object[] args)
        {
            // Get the current assembly
            var assembly = Assembly.GetExecutingAssembly();

            var fullResourceName = Array.Find(
                assembly.GetManifestResourceNames(),
                name => name.EndsWith(pythonScriptName, StringComparison.OrdinalIgnoreCase));

            if (fullResourceName == null)
            {
                throw new FileNotFoundException($"Embedded resource '{pythonScriptName}' not found in assembly.");
            }
            string tempScriptPath = Path.Combine(Path.GetTempPath(), pythonScriptName);
            using (var resourceStream = assembly.GetManifestResourceStream(fullResourceName))
            using (var fileStream = new FileStream(tempScriptPath, FileMode.Create, FileAccess.Write))
            {
                resourceStream.CopyTo(fileStream);
            }

            return PythonHelper.ExecutePythonMethod(tempScriptPath, methodName, dataConversionResult, args);
        }
    }
}
