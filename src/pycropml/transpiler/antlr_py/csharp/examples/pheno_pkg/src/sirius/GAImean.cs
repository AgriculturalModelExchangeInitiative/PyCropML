
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
    public class GAImean : IStrategySiriusQualityPhenology
    {
        public GAImean()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 0.0;
            v1.Description = "Thermal Time window for average";
            v1.Id = 0;
            v1.MaxValue = 5000.0;
            v1.MinValue = 0.0;
            v1.Name = "tTWindowForPTQ";
            v1.Size = 1;
            v1.Units = "°C d";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v1);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd1.PropertyName = "gAI";
            pd1.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.gAI).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.gAI);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd2.PropertyName = "deltaTT";
            pd2.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd3.PropertyName = "pastMaxAI";
            pd3.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd4.PropertyName = "listTTShootWindowForPTQ1";
            pd4.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1);
            _inputs0_0.Add(pd4);
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd5.PropertyName = "listGAITTWindowForPTQ";
            pd5.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ);
            _inputs0_0.Add(pd5);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd6.PropertyName = "gAImean";
            pd6.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.gAImean).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.gAImean);
            _outputs0_0.Add(pd6);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd7 = new PropertyDescription();
            pd7.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd7.PropertyName = "pastMaxAI";
            pd7.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI).ValueType.TypeForCurrentValue;
            pd7.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI);
            _outputs0_0.Add(pd7);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd8 = new PropertyDescription();
            pd8.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd8.PropertyName = "listTTShootWindowForPTQ1";
            pd8.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1).ValueType.TypeForCurrentValue;
            pd8.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1);
            _outputs0_0.Add(pd8);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd9 = new PropertyDescription();
            pd9.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd9.PropertyName = "listGAITTWindowForPTQ";
            pd9.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ).ValueType.TypeForCurrentValue;
            pd9.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ);
            _outputs0_0.Add(pd9);
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
            get { return "-" ;}
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
            _pd.Add("Creator", "Loïc Manceau");
            _pd.Add("Date", "");
            _pd.Add("Publisher", "INRA");
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
                else throw new Exception("Parameter 'tTWindowForPTQ' not found (or found null) in strategy 'GAImean'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("tTWindowForPTQ");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'tTWindowForPTQ' not found in strategy 'GAImean'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            tTWindowForPTQVarInfo.Name = "tTWindowForPTQ";
            tTWindowForPTQVarInfo.Description = "Thermal Time window for average";
            tTWindowForPTQVarInfo.MaxValue = 5000.0;
            tTWindowForPTQVarInfo.MinValue = 0.0;
            tTWindowForPTQVarInfo.DefaultValue = 0.0;
            tTWindowForPTQVarInfo.Units = "°C d";
            tTWindowForPTQVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
        }

        private static VarInfo _tTWindowForPTQVarInfo = new VarInfo();
        public static VarInfo tTWindowForPTQVarInfo
        {
            get { return _tTWindowForPTQVarInfo;} 
        }

        public string TestPostConditions(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.gAImean.CurrentValue=s.gAImean;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI.CurrentValue=s.pastMaxAI;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1.CurrentValue=s.listTTShootWindowForPTQ1;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ.CurrentValue=s.listGAITTWindowForPTQ;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r7 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.gAImean);
                if(r7.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.gAImean.ValueType)){prc.AddCondition(r7);}
                RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI);
                if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI.ValueType)){prc.AddCondition(r8);}
                RangeBasedCondition r9 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1);
                if(r9.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1.ValueType)){prc.AddCondition(r9);}
                RangeBasedCondition r10 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ);
                if(r10.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ.ValueType)){prc.AddCondition(r10);}
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
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.gAI.CurrentValue=a.gAI;
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT.CurrentValue=a.deltaTT;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI.CurrentValue=s.pastMaxAI;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1.CurrentValue=s.listTTShootWindowForPTQ1;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ.CurrentValue=s.listGAITTWindowForPTQ;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.gAI);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.gAI.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.deltaTT.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.pastMaxAI.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listTTShootWindowForPTQ1.ValueType)){prc.AddCondition(r4);}
                RangeBasedCondition r5 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ);
                if(r5.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.listGAITTWindowForPTQ.ValueType)){prc.AddCondition(r5);}
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("tTWindowForPTQ")));
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

        private void CalculateModel(SiriusQualityPhenology.DomainClass.PhenologyState s, SiriusQualityPhenology.DomainClass.PhenologyState s1, SiriusQualityPhenology.DomainClass.PhenologyRate r, SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a, SiriusQualityPhenology.DomainClass.PhenologyExogenous ex)
        {
            double gAI = a.gAI;
            double deltaTT = a.deltaTT;
            double pastMaxAI_t1 = s1.pastMaxAI;
            List<double> listTTShootWindowForPTQ1_t1 = s1.listTTShootWindowForPTQ1;
            List<double> listGAITTWindowForPTQ_t1 = s1.listGAITTWindowForPTQ;
            double gAImean;
            double pastMaxAI;
            List<double> listTTShootWindowForPTQ1 = new List<double>();
            List<double> listGAITTWindowForPTQ = new List<double>();
            List<double> TTList = new List<double>();
            List<double> GAIList = new List<double>();
            double SumTT;
            int count = 0;
            double gai_ = 0.0d;
            double gaiMean_ = 0.0d;
            int countGaiMean = 0;
            int i;
            for (i=0 ; i<listTTShootWindowForPTQ1_t1.Count ; i+=1)
            {
                TTList.Add(listTTShootWindowForPTQ1_t1[i]);
                GAIList.Add(listGAITTWindowForPTQ_t1[i]);
            }
            TTList.Add(deltaTT);
            GAIList.Add(gAI);
            SumTT = TTList.Sum();
            while ( SumTT > tTWindowForPTQ)
            {
                SumTT = SumTT - TTList[count];
                count = count + 1;
            }
            for (i=count ; i<TTList.Count ; i+=1)
            {
                listTTShootWindowForPTQ1.Add(TTList[i]);
                listGAITTWindowForPTQ.Add(GAIList[i]);
            }
            for (i=0 ; i<listGAITTWindowForPTQ.Count ; i+=1)
            {
                gaiMean_ = gaiMean_ + listGAITTWindowForPTQ[i];
                countGaiMean = countGaiMean + 1;
            }
            gaiMean_ = gaiMean_ / countGaiMean;
            gai_ = Math.Max(pastMaxAI_t1, gaiMean_);
            pastMaxAI = gai_;
            gAImean = gai_;
            s.gAImean= gAImean;
            s.pastMaxAI= pastMaxAI;
            s.listTTShootWindowForPTQ1= listTTShootWindowForPTQ1;
            s.listGAITTWindowForPTQ= listGAITTWindowForPTQ;
        }

    }
}