using MachineLearning4Water_Models;
using static Microsoft.FSharp.Core.ByRefKinds;

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
    }
}