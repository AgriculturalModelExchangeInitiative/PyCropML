using System;
using CRA.AgroManagement;
using CRA.ModelLayer.Strategy;
namespace SiriusQualityPhenology.DomainClass
{
    public interface IStrategySiriusQualityPhenology : IStrategy
    {
        void Estimate( PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a, PhenologyExogenous ex);

        string TestPreConditions( PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a, PhenologyExogenous ex, string callID);

        string TestPostConditions( PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a, PhenologyExogenous ex, string callID);

        void SetParametersDefaultValue();
    }
}