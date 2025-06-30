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
                Codi_postal = 08020,
                Persones_habitatge = 2,
                Tipus_habitatge = (float) ConsumHabitatgesModelEnums.TipusHabitatge.Pis,
                Lavabos_habitatge = 2,
                Rentavaixelles = 0,
                Us_banyera = (float) ConsumHabitatgesModelEnums.Banyera.NoTincBanyera,
                Wc_diari = 10,
                Dutxes_diari = 1,
                Tipus_caldera = (float) ConsumHabitatgesModelEnums.TipusCaldera.Caldera,
                Instalacio_caldera = (float) ConsumHabitatgesModelEnums.InstalacioCaldera.Individual,
                Potencia_caldera = 24,
                Antiguitat_caldera = 15,
                Caldera_antiga = (float) ConsumHabitatgesModelEnums.CalderaAntiga.Mes10Anys,
                Distancia_caldera_dutxa = 15,
                Temps_aigua_calenta = 40,
                Clau_pas = 1,
                Tipus_descàrrega = (float) ConsumHabitatgesModelEnums.TipusDescarrega.DobleDescarrega,
                Cisterna_encastada = 1,
                Cisterna_entrades = (float) ConsumHabitatgesModelEnums.CisternaEntrades.UnaEntrada,
                Cisterna_capacitat = 9,
                Coneixement_sequera = 1,
                Seguiment_factura = 1,
                Llar_concienciara = 1,
                Estalvies_aigua = 1,
                Estalviaries_aigua = 1
            };
            var predEngine = ConsumHabitatgesModel.PredictEngine.Value;
            var result = predEngine.Predict(input);
            Assert.IsTrue(result.Score > 0 && result.Score < 100);
        }
    }
}