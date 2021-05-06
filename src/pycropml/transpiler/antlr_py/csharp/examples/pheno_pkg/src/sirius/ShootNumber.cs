
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
    public class ShootNumber : IStrategySiriusQualityPhenology
    {
        public ShootNumber()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 288.0;
            v1.Description = "number of plant /m²";
            v1.Id = 0;
            v1.MaxValue = 500;
            v1.MinValue = 0;
            v1.Name = "sowingDensity";
            v1.Size = 1;
            v1.Units = "plant m-2";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v1);
            VarInfo v2 = new VarInfo();
            v2.DefaultValue = 600.0;
            v2.Description = "max value of shoot number for the canopy";
            v2.Id = 0;
            v2.MaxValue = 1000;
            v2.MinValue = 280;
            v2.Name = "targetFertileShoot";
            v2.Size = 1;
            v2.Units = "shoot";
            v2.URL = "";
            v2.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v2);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd1.PropertyName = "canopyShootNumber";
            pd1.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd2.PropertyName = "leafNumber";
            pd2.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd3.PropertyName = "tilleringProfile";
            pd3.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd4.PropertyName = "leafTillerNumberArray";
            pd4.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray);
            _inputs0_0.Add(pd4);
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd5.PropertyName = "numberTillerCohort";
            pd5.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.numberTillerCohort).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.numberTillerCohort);
            _inputs0_0.Add(pd5);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd6 = new PropertyDescription();
            pd6.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd6.PropertyName = "averageShootNumberPerPlant";
            pd6.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.averageShootNumberPerPlant).ValueType.TypeForCurrentValue;
            pd6.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.averageShootNumberPerPlant);
            _outputs0_0.Add(pd6);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd7 = new PropertyDescription();
            pd7.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd7.PropertyName = "canopyShootNumber";
            pd7.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber).ValueType.TypeForCurrentValue;
            pd7.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber);
            _outputs0_0.Add(pd7);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd8 = new PropertyDescription();
            pd8.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd8.PropertyName = "leafTillerNumberArray";
            pd8.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray).ValueType.TypeForCurrentValue;
            pd8.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray);
            _outputs0_0.Add(pd8);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd9 = new PropertyDescription();
            pd9.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd9.PropertyName = "tilleringProfile";
            pd9.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile).ValueType.TypeForCurrentValue;
            pd9.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile);
            _outputs0_0.Add(pd9);
            mo0_0.Outputs=_outputs0_0;PropertyDescription pd10 = new PropertyDescription();
            pd10.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd10.PropertyName = "numberTillerCohort";
            pd10.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.numberTillerCohort).ValueType.TypeForCurrentValue;
            pd10.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.numberTillerCohort);
            _outputs0_0.Add(pd10);
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
            get { return "calculate the shoot number and update the related variables if needed" ;}
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
            _pd.Add("Creator", "Pierre MARTRE");
            _pd.Add("Date", "");
            _pd.Add("Publisher", "INRA/LEPSE Montpellier");
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

        public double sowingDensity
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("sowingDensity");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'sowingDensity' not found (or found null) in strategy 'ShootNumber'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("sowingDensity");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'sowingDensity' not found in strategy 'ShootNumber'");
            }
        }
        public double targetFertileShoot
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("targetFertileShoot");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'targetFertileShoot' not found (or found null) in strategy 'ShootNumber'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("targetFertileShoot");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'targetFertileShoot' not found in strategy 'ShootNumber'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            sowingDensityVarInfo.Name = "sowingDensity";
            sowingDensityVarInfo.Description = "number of plant /m²";
            sowingDensityVarInfo.MaxValue = 500;
            sowingDensityVarInfo.MinValue = 0;
            sowingDensityVarInfo.DefaultValue = 288.0;
            sowingDensityVarInfo.Units = "plant m-2";
            sowingDensityVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            targetFertileShootVarInfo.Name = "targetFertileShoot";
            targetFertileShootVarInfo.Description = "max value of shoot number for the canopy";
            targetFertileShootVarInfo.MaxValue = 1000;
            targetFertileShootVarInfo.MinValue = 280;
            targetFertileShootVarInfo.DefaultValue = 600.0;
            targetFertileShootVarInfo.Units = "shoot";
            targetFertileShootVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
        }

        private static VarInfo _sowingDensityVarInfo = new VarInfo();
        public static VarInfo sowingDensityVarInfo
        {
            get { return _sowingDensityVarInfo;} 
        }

        private static VarInfo _targetFertileShootVarInfo = new VarInfo();
        public static VarInfo targetFertileShootVarInfo
        {
            get { return _targetFertileShootVarInfo;} 
        }

        public string TestPostConditions(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.averageShootNumberPerPlant.CurrentValue=s.averageShootNumberPerPlant;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber.CurrentValue=s.canopyShootNumber;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray.CurrentValue=s.leafTillerNumberArray;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile.CurrentValue=s.tilleringProfile;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.numberTillerCohort.CurrentValue=s.numberTillerCohort;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.averageShootNumberPerPlant);
                if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.averageShootNumberPerPlant.ValueType)){prc.AddCondition(r8);}
                RangeBasedCondition r9 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber);
                if(r9.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber.ValueType)){prc.AddCondition(r9);}
                RangeBasedCondition r10 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray);
                if(r10.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray.ValueType)){prc.AddCondition(r10);}
                RangeBasedCondition r11 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile);
                if(r11.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile.ValueType)){prc.AddCondition(r11);}
                RangeBasedCondition r12 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.numberTillerCohort);
                if(r12.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.numberTillerCohort.ValueType)){prc.AddCondition(r12);}
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
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber.CurrentValue=s.canopyShootNumber;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber.CurrentValue=s.leafNumber;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile.CurrentValue=s.tilleringProfile;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray.CurrentValue=s.leafTillerNumberArray;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.numberTillerCohort.CurrentValue=s.numberTillerCohort;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.canopyShootNumber.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.tilleringProfile.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafTillerNumberArray.ValueType)){prc.AddCondition(r4);}
                RangeBasedCondition r5 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.numberTillerCohort);
                if(r5.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.numberTillerCohort.ValueType)){prc.AddCondition(r5);}
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("sowingDensity")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("targetFertileShoot")));
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
            double canopyShootNumber_t1 = s1.canopyShootNumber;
            double leafNumber = s.leafNumber;
            List<double> tilleringProfile_t1 = s1.tilleringProfile;
            List<int> leafTillerNumberArray_t1 = s1.leafTillerNumberArray;
            int numberTillerCohort_t1 = s1.numberTillerCohort;
            double averageShootNumberPerPlant;
            double canopyShootNumber;
            List<int> leafTillerNumberArray = new List<int>();
            List<double> tilleringProfile = new List<double>();
            int numberTillerCohort;
            int emergedLeaves;
            int shoots;
            int i;
            List<int> lNumberArray_rate = new List<int>();
            emergedLeaves = Math.Max(1, (int) Math.Ceiling(leafNumber - 1.0d));
            shoots = fibonacci(emergedLeaves);
            canopyShootNumber = Math.Min(shoots * sowingDensity, targetFertileShoot);
            averageShootNumberPerPlant = canopyShootNumber / sowingDensity;
            tilleringProfile = new List<double>(tilleringProfile_t1);
            if (canopyShootNumber != canopyShootNumber_t1)
            {
                tilleringProfile.Add(canopyShootNumber - canopyShootNumber_t1);
            }
            numberTillerCohort = tilleringProfile.Count;
            for (i=leafTillerNumberArray_t1.Count ; i<(int) Math.Ceiling(leafNumber) ; i+=1)
            {
                lNumberArray_rate.Add(numberTillerCohort);
            }
            leafTillerNumberArray = new List<int>(leafTillerNumberArray_t1);
            leafTillerNumberArray.AddRange(lNumberArray_rate);
            s.averageShootNumberPerPlant= averageShootNumberPerPlant;
            s.canopyShootNumber= canopyShootNumber;
            s.leafTillerNumberArray= leafTillerNumberArray;
            s.tilleringProfile= tilleringProfile;
            s.numberTillerCohort= numberTillerCohort;
        }

        public static int fibonacci(int n)
        {
            if (n <= 1)
            {
                return n;
            }
            else
            {
                return fibonacci(n - 1) + fibonacci(n - 2);
            }
        }

        public void Init(SiriusQualityPhenology.DomainClass.PhenologyState s, SiriusQualityPhenology.DomainClass.PhenologyState s1, SiriusQualityPhenology.DomainClass.PhenologyRate r, SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a, SiriusQualityPhenology.DomainClass.PhenologyExogenous ex)
        {
            double canopyShootNumber_t1;
            double leafNumber;
            List<double> tilleringProfile_t1 = new List<double>();
            List<int> leafTillerNumberArray_t1 = new List<int>();
            int numberTillerCohort_t1;
            double averageShootNumberPerPlant;
            double canopyShootNumber;
            List<int> leafTillerNumberArray = new List<int>();
            List<double> tilleringProfile = new List<double>();
            int numberTillerCohort;
            canopyShootNumber = sowingDensity;
            averageShootNumberPerPlant = 1.0d;
            tilleringProfile.Add(sowingDensity);
            numberTillerCohort = 1;
            s.averageShootNumberPerPlant= averageShootNumberPerPlant;
            s.canopyShootNumber= canopyShootNumber;
            s.leafTillerNumberArray= leafTillerNumberArray;
            s.tilleringProfile= tilleringProfile;
            s.numberTillerCohort= numberTillerCohort;
        }

    }
}