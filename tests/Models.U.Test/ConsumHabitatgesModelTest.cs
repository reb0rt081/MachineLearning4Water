using MachineLearning4Water_Models;
using Microsoft.ML;
using System.Formats.Asn1;
using System.Globalization;
using System.IO;
using System.Reflection.PortableExecutable;
using System.Text;
using static Microsoft.FSharp.Core.ByRefKinds;
using static System.Net.Mime.MediaTypeNames;

namespace MachineLearning4Water.Models.U.Test
{
    [TestClass]
    public class ConsumHabitatgesModelTest
    {
        [TestMethod]
        public void SimplePrediction()
        {
            var input = new ConsumHabitatgesModel.ModelInput()
            {
                Persones_habitatge = 2,
                Tipus_habitatge = (float) ConsumHabitatgesModelEnums.TipusHabitatge.Pis,
                Lavabos_habitatge = 2,
                Rentavaixelles = 0,
                Us_banyera = (float) ConsumHabitatgesModelEnums.Banyera.TincBanyeraUtilitzoSovint,
                Wc_diari = 10,
                Dutxes_diari = 4,
                Tipus_caldera = (float) ConsumHabitatgesModelEnums.TipusCaldera.Caldera,
                //Instalacio_caldera = (float) ConsumHabitatgesModelEnums.InstalacioCaldera.Individual,
                //Potencia_caldera = 24,
                Antiguitat_caldera = 15,
                Caldera_antiga = (float) ConsumHabitatgesModelEnums.CalderaAntiga.Mes10Anys,
                Distancia_caldera_dutxa = 15,
                Temps_aigua_calenta = 40,
                //Clau_pas = 1,
                Tipus_descarrega = (float) ConsumHabitatgesModelEnums.TipusDescarrega.DobleDescarrega,
                //Cisterna_encastada = 1,
                //Cisterna_entrades = (float) ConsumHabitatgesModelEnums.CisternaEntrades.UnaEntrada,
                Cisterna_capacitat = 9,
                //Coneixement_sequera = 0,
                Seguiment_factura = 0,
                //Llar_concienciara = 0,
                Estalvies_aigua = 0,
                //Estalviaries_aigua = 0
            };
            var predEngine = ConsumHabitatgesModel.PredictEngine.Value;
            var result = predEngine.Predict(input);
            Console.WriteLine($"Prediction returns {result.Score} m3/month");
            Assert.IsTrue(result.Score > 0 && result.Score < 100);
        }

        [TestMethod]
        public void FullPrediction()
        {
            var inputFilePath = "Informacio_Habitatges_Data.csv";
            var outputFileOath = "ActualVsPredictedValues.csv";

            Dictionary<ConsumHabitatgesModel.ModelInput, float> modelInputOutputs = new Dictionary<ConsumHabitatgesModel.ModelInput, float>();
            using (var rd = new StreamReader(inputFilePath))
            {
                int line = 0;
                while (!rd.EndOfStream)
                {
                    line++;
                    var splits = rd.ReadLine().Split(',');
                    if (line == 1)
                    {
                        continue;
                    }

                    modelInputOutputs.Add(new ConsumHabitatgesModel.ModelInput()
                    {
                        Persones_habitatge = TryParseColumn(splits[1]),
                        Tipus_habitatge = TryParseColumn(splits[2]),
                        Lavabos_habitatge = TryParseColumn(splits[3]),
                        Rentavaixelles = TryParseColumn(splits[4]),
                        Us_banyera = TryParseColumn(splits[5]),
                        Wc_diari = TryParseColumn(splits[7]),
                        Dutxes_diari = TryParseColumn(splits[8]),
                        Tipus_caldera = TryParseColumn(splits[9]),
                        Instalacio_caldera = TryParseColumn(splits[10]),
                        Potencia_caldera = TryParseColumn(splits[11]),
                        Antiguitat_caldera = TryParseColumn(splits[12]),
                        Caldera_antiga = TryParseColumn(splits[13]),
                        Distancia_caldera_dutxa = TryParseColumn(splits[14]),
                        Temps_aigua_calenta = TryParseColumn(splits[15]),
                        Clau_pas = TryParseColumn(splits[16]),
                        Tipus_descarrega = TryParseColumn(splits[17]),
                        Cisterna_encastada = TryParseColumn(splits[18]),
                        Cisterna_entrades = TryParseColumn(splits[19]),
                        Cisterna_capacitat = TryParseColumn(splits[20]),
                        Coneixement_sequera = TryParseColumn(splits[21]),
                        Seguiment_factura = TryParseColumn(splits[22]),
                        Llar_concienciara = TryParseColumn(splits[23]),
                        Estalvies_aigua = TryParseColumn(splits[24]),
                        Estalviaries_aigua = TryParseColumn(splits[25])
                    }, TryParseColumn(splits[6]));
                }
            }

            List<(float, float)> results = new List<(float, float)>();
            foreach (var modelInputOutput in modelInputOutputs)
            {
                var predEngine = ConsumHabitatgesModel.PredictEngine.Value;
                var result = predEngine.Predict(modelInputOutput.Key);
                results.Add((modelInputOutput.Value, result.Score));
            }

            using (var streamWriter = new StreamWriter(outputFileOath))
            {
                var header = "Actual_value,Predicted_value";
                streamWriter.WriteLine(header);
                streamWriter.Flush();

                foreach (var result in results)
                {
                    var line = $"{result.Item1.ToString(CultureInfo.InvariantCulture)},{result.Item2.ToString(CultureInfo.InvariantCulture)}";
                    streamWriter.WriteLine(line);
                    streamWriter.Flush();
                }
            }
        }

        private float TryParseColumn(string columnValue)
        {
            if (string.IsNullOrEmpty(columnValue))
            {
                return 0;
            }

            return float.Parse(columnValue, CultureInfo.InvariantCulture);
        }
    }
}