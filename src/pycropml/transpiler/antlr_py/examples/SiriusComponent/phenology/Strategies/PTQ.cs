
using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml;
using CRA.ModelLayer.MetadataTypes;
using CRA.ModelLayer.Core;
using CRA.ModelLayer.Strategy;
using System.Reflection;
using VarInfo=CRA.ModelLayer.Core.VarInfo;
using Preconditions=CRA.ModelLayer.Core.Preconditions;
using CRA.AgroManagement;       
using SiriusQualityPhenology.DomainClass;
namespace SiriusQualityPhenology.Strategies
{
    public class PTQ : IStrategySiriusQualityPhenology
    {
        public PTQ()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 70.0;
            v1.Description = "Thermal time window in which averages are computed";
            v1.Id = 0;
            v1.MaxValue = 70000.0;
            v1.MinValue = 0.0;
            v1.Name = "tTWindowForPTQ";
            v1.Size = 1;
            v1.Units = "°C d";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v1);
            VarInfo v2 = new VarInfo();
            v2.DefaultValue = 0.45;
            v2.Description = "Exctinction Coefficient";
            v2.Id = 0;
            v2.MaxValue = 50.0;
            v2.MinValue = 0.0;
            v2.Name = "kl";
            v2.Size = 1;
            v2.Units = "";
            v2.URL = "";
            v2.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v2);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd1.PropertyName = "listTTShootWindowForPTQ";
            pd1.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd2.PropertyName = "listPARTTWindowForPTQ";
            pd2.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd3.PropertyName = "listGAITTWindowForPTQ";
            pd3.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd4.PropertyName = "pAR";
            pd4.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.pAR).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.pAR);
            _inputs0_0.Add(pd4);
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd5.PropertyName = "deltaTT";
            pd5.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT);
            _inputs0_0.Add(pd5);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd6.PropertyName = "listPARTTWindowForPTQ";
            pd6.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ);
            _outputs0_0.Add(pd6);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd7 = new PropertyDescription();
            pd7.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd7.PropertyName = "listTTShootWindowForPTQ";
            pd7.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ).ValueType.TypeForCurrentValue;
            pd7.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ);
            _outputs0_0.Add(pd7);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd8 = new PropertyDescription();
            pd8.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd8.PropertyName = "ptq";
            pd8.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq).ValueType.TypeForCurrentValue;
            pd8.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq);
            _outputs0_0.Add(pd8);
            mo0_0.Outputs=_outputs0_0;
            //Associated strategies
            List<string> lAssStrat0_0 = new List<string>();
            mo0_0.AssociatedStrategies = lAssStrat0_0;
            //Adding the modeling options to the modeling options manager
            _modellingOptionsManager = new ModellingOptionsManager(mo0_0);
            SetStaticParametersVarInfoDefinitions();
            SetPublisherData();

        }

        public string Description
        {
            get { return "Calculate Photothermal Quaotient " ;}
        }

        public string URL
        {
            get { return "" ;}
        }

        public string Domain
        {
            get { return "";}
        }

        public string ModelType
        {
            get { return "";}
        }

        public bool IsContext
        {
            get { return false;}
        }

        public IList<int> TimeStep
        {
            get
            {
                IList<int> ts = new List<int>();
                return ts;
            }
        }

        private  PublisherData _pd;
        public PublisherData PublisherData
        {
            get { return _pd;} 
        }

        private  void SetPublisherData()
        {
            _pd = new CRA.ModelLayer.MetadataTypes.PublisherData();
            _pd.Add("Creator", "Pierre Martre");
            _pd.Add("Date", "");
            _pd.Add("Publisher", "INRA Montpellier");
        }

        private ModellingOptionsManager _modellingOptionsManager;
        public ModellingOptionsManager ModellingOptionsManager
        {
            get { return _modellingOptionsManager; } 
        }

        public IEnumerable<Type> GetStrategyDomainClassesTypes()
        {
            return new List<Type>() {  typeof(SiriusQualityPhenology.DomainClass.PhenologyState),  typeof(SiriusQualityPhenology.DomainClass.PhenologyState), typeof(SiriusQualityPhenology.DomainClass.PhenologyRate), typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary), typeof(SiriusQualityPhenology.DomainClass.PhenologyExogenous)};
        }

        // Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.

        public double tTWindowForPTQ
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("tTWindowForPTQ");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'tTWindowForPTQ' not found (or found null) in strategy 'PTQ'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("tTWindowForPTQ");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'tTWindowForPTQ' not found in strategy 'PTQ'");
            }
        }
        public double kl
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("kl");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'kl' not found (or found null) in strategy 'PTQ'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("kl");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'kl' not found in strategy 'PTQ'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            tTWindowForPTQVarInfo.Name = "tTWindowForPTQ";
            tTWindowForPTQVarInfo.Description = "Thermal time window in which averages are computed";
            tTWindowForPTQVarInfo.MaxValue = 70000.0;
            tTWindowForPTQVarInfo.MinValue = 0.0;
            tTWindowForPTQVarInfo.DefaultValue = 70.0;
            tTWindowForPTQVarInfo.Units = "°C d";
            tTWindowForPTQVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            klVarInfo.Name = "kl";
            klVarInfo.Description = "Exctinction Coefficient";
            klVarInfo.MaxValue = 50.0;
            klVarInfo.MinValue = 0.0;
            klVarInfo.DefaultValue = 0.45;
            klVarInfo.Units = "";
            klVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
        }

        private static VarInfo _tTWindowForPTQVarInfo = new VarInfo();
        public static VarInfo tTWindowForPTQVarInfo
        {
            get { return _tTWindowForPTQVarInfo;} 
        }

        private static VarInfo _klVarInfo = new VarInfo();
        public static VarInfo klVarInfo
        {
            get { return _klVarInfo;} 
        }

        public string TestPostConditions(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ.CurrentValue=s.listPARTTWindowForPTQ;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ.CurrentValue=s.listTTShootWindowForPTQ;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq.CurrentValue=s.ptq;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ);
                if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ.ValueType)){prc.AddCondition(r8);}
                RangeBasedCondition r9 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ);
                if(r9.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ.ValueType)){prc.AddCondition(r9);}
                RangeBasedCondition r10 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq);
                if(r10.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq.ValueType)){prc.AddCondition(r10);}
                string postConditionsResult = pre.VerifyPostconditions(prc, callID); if (!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in strategy " + this.GetType().Name); } return postConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.Phenology, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public string TestPreConditions(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex,string callID)
        {
            try
            {
                //Set current values of the inputs to the static VarInfo representing the inputs properties of the domain classes
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ.CurrentValue=s.listTTShootWindowForPTQ;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ.CurrentValue=s.listPARTTWindowForPTQ;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ.CurrentValue=s.listGAITTWindowForPTQ;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.pAR.CurrentValue=a.pAR;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT.CurrentValue=a.deltaTT;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listPARTTWindowForPTQ.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.pAR);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.pAR.ValueType)){prc.AddCondition(r4);}
                RangeBasedCondition r5 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT);
                if(r5.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT.ValueType)){prc.AddCondition(r5);}
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("tTWindowForPTQ")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("kl")));
                string preConditionsResult = pre.VerifyPreconditions(prc, callID); if (!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in strategy " + this.GetType().Name); } return preConditionsResult;
            }
            catch (Exception exception)
            {
                string msg = "SiriusQuality.Phenology, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
                throw new Exception(msg, exception);
            }
        }

        public void Estimate(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex)
        {
            try
            {
                CalculateModel(s, s1, r, a, ex);
            }
            catch (Exception exception)
            {
                string msg = "Error in component SiriusQualityPhenology, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;
                throw new Exception(msg, exception);
            }
        }

        private void  CalculateModel(SiriusQualityPhenology.DomainClass.PhenologyState s, SiriusQualityPhenology.DomainClass.PhenologyState s1, SiriusQualityPhenology.DomainClass.PhenologyRate r, SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a, SiriusQualityPhenology.DomainClass.PhenologyExogenous ex)
        {
            List<double> listTTShootWindowForPTQ_t1 = s1.listTTShootWindowForPTQ;
            List<double> listPARTTWindowForPTQ_t1 = s1.listPARTTWindowForPTQ;
            List<double> listGAITTWindowForPTQ = s.listGAITTWindowForPTQ;
            double pAR = a.pAR;
            double deltaTT = a.deltaTT;
            List<double> listPARTTWindowForPTQ = new List<double>();
            List<double> listTTShootWindowForPTQ = new List<double>();
            double ptq;
            List<double> TTList = new List<double>();
            List<double> PARList = new List<double>();
            int i;
            int count;
            double SumTT;
            double parInt = 0.0d;
            double TTShoot;
            for (i=0 ; i<listTTShootWindowForPTQ_t1.Count ; i+=1)
            {
                TTList.Add(listTTShootWindowForPTQ_t1[i]);
                PARList.Add(listPARTTWindowForPTQ_t1[i]);
            }
            TTList.Add(deltaTT);
            PARList.Add(pAR);
            SumTT = TTList.Sum();
            count = 0;
            while ( SumTT > tTWindowForPTQ)
            {
                SumTT = SumTT - TTList[count];
                count = count + 1;
            }
            for (i=count ; i<TTList.Count ; i+=1)
            {
                listTTShootWindowForPTQ.Add(TTList[i]);
                listPARTTWindowForPTQ.Add(PARList[i]);
            }
            for (i=0 ; i<listTTShootWindowForPTQ.Count ; i+=1)
            {
                parInt = parInt + (listPARTTWindowForPTQ[i] * (1 - Math.Exp(-kl * listGAITTWindowForPTQ[i])));
            }
            TTShoot = listTTShootWindowForPTQ.Sum();
            ptq = parInt / TTShoot;
            s.listPARTTWindowForPTQ= listPARTTWindowForPTQ;
            s.listTTShootWindowForPTQ= listTTShootWindowForPTQ;
            s.ptq= ptq;
        }

    }
}