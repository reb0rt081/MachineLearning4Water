using System;

using MachineLearning4Water.Tools;

namespace MachineLearning4Water.Python
{
    public class PythonRunner
    {
        public static TOut RunPythonMethod<TOut>(string pythonScriptName, string methodName, Func<dynamic, TOut> dataConversionResult, params object[] args)
        {
            return PythonHelper.ExecutePythonMethod($"./Scripts/{pythonScriptName}", methodName, dataConversionResult, args);
        }
    }
}
