
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
    public class PhylSowingDateCorrection : IStrategySiriusQualityPhenology
    {
        public PhylSowingDateCorrection()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 1;
            v1.Description = "Day of Year at sowing";
            v1.Id = 0;
            v1.MaxValue = 365;
            v1.MinValue = 1;
            v1.Name = "sowingDay";
            v1.Size = 1;
            v1.Units = "d";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");
            _parameters0_0.Add(v1);
            VarInfo v2 = new VarInfo();
            v2.DefaultValue = 0.0;
            v2.Description = "Latitude";
            v2.Id = 0;
            v2.MaxValue = 90;
            v2.MinValue = -90;
            v2.Name = "latitude";
            v2.Size = 1;
            v2.Units = "°";
            v2.URL = "";
            v2.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v2);
            VarInfo v3 = new VarInfo();
            v3.DefaultValue = 1.0;
            v3.Description = "Sowing date at which Phyllochrone is maximum in southern hemispher";
            v3.Id = 0;
            v3.MaxValue = 365;
            v3.MinValue = 1;
            v3.Name = "sDsa_sh";
            v3.Size = 1;
            v3.Units = "d";
            v3.URL = "";
            v3.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v3.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v3);
            VarInfo v4 = new VarInfo();
            v4.DefaultValue = 0;
            v4.Description = "Rate of change of Phyllochrone with sowing date";
            v4.Id = 0;
            v4.MaxValue = 365;
            v4.MinValue = 0;
            v4.Name = "rp";
            v4.Size = 1;
            v4.Units = "d-1";
            v4.URL = "";
            v4.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v4.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v4);
            VarInfo v5 = new VarInfo();
            v5.DefaultValue = 1;
            v5.Description = "Sowing date at which Phyllochrone is minimum";
            v5.Id = 0;
            v5.MaxValue = 365;
            v5.MinValue = 1;
            v5.Name = "sDws";
            v5.Size = 1;
            v5.Units = "d";
            v5.URL = "";
            v5.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v5.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");
            _parameters0_0.Add(v5);
            VarInfo v6 = new VarInfo();
            v6.DefaultValue = 1.0;
            v6.Description = "Sowing date at which Phyllochrone is maximum in northern hemispher";
            v6.Id = 0;
            v6.MaxValue = 365;
            v6.MinValue = 1;
            v6.Name = "sDsa_nh";
            v6.Size = 1;
            v6.Units = "d";
            v6.URL = "";
            v6.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v6.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v6);
            VarInfo v7 = new VarInfo();
            v7.DefaultValue = 120;
            v7.Description = "Phyllochron (Varietal parameter)";
            v7.Id = 0;
            v7.MaxValue = 1000;
            v7.MinValue = 0;
            v7.Name = "p";
            v7.Size = 1;
            v7.Units = "°C d leaf-1";
            v7.URL = "";
            v7.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v7.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v7);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd1.PropertyName = "fixPhyll";
            pd1.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.fixPhyll).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.fixPhyll);
            _outputs0_0.Add(pd1);
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
            get { return "Correction of the Phyllochron Varietal parameter according to sowing date " ;}
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
            _pd.Add("Creator", "Loic Manceau");
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

        public int sowingDay
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("sowingDay");
                if (vi != null && vi.CurrentValue!=null) return (int)vi.CurrentValue ;
                else throw new Exception("Parameter 'sowingDay' not found (or found null) in strategy 'PhylSowingDateCorrection'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("sowingDay");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'sowingDay' not found in strategy 'PhylSowingDateCorrection'");
            }
        }
        public double latitude
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("latitude");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'latitude' not found (or found null) in strategy 'PhylSowingDateCorrection'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("latitude");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'latitude' not found in strategy 'PhylSowingDateCorrection'");
            }
        }
        public double sDsa_sh
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("sDsa_sh");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'sDsa_sh' not found (or found null) in strategy 'PhylSowingDateCorrection'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("sDsa_sh");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'sDsa_sh' not found in strategy 'PhylSowingDateCorrection'");
            }
        }
        public double rp
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("rp");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'rp' not found (or found null) in strategy 'PhylSowingDateCorrection'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("rp");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'rp' not found in strategy 'PhylSowingDateCorrection'");
            }
        }
        public int sDws
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("sDws");
                if (vi != null && vi.CurrentValue!=null) return (int)vi.CurrentValue ;
                else throw new Exception("Parameter 'sDws' not found (or found null) in strategy 'PhylSowingDateCorrection'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("sDws");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'sDws' not found in strategy 'PhylSowingDateCorrection'");
            }
        }
        public double sDsa_nh
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("sDsa_nh");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'sDsa_nh' not found (or found null) in strategy 'PhylSowingDateCorrection'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("sDsa_nh");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'sDsa_nh' not found in strategy 'PhylSowingDateCorrection'");
            }
        }
        public double p
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("p");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'p' not found (or found null) in strategy 'PhylSowingDateCorrection'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("p");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'p' not found in strategy 'PhylSowingDateCorrection'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            sowingDayVarInfo.Name = "sowingDay";
            sowingDayVarInfo.Description = "Day of Year at sowing";
            sowingDayVarInfo.MaxValue = 365;
            sowingDayVarInfo.MinValue = 1;
            sowingDayVarInfo.DefaultValue = 1;
            sowingDayVarInfo.Units = "d";
            sowingDayVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            latitudeVarInfo.Name = "latitude";
            latitudeVarInfo.Description = "Latitude";
            latitudeVarInfo.MaxValue = 90;
            latitudeVarInfo.MinValue = -90;
            latitudeVarInfo.DefaultValue = 0.0;
            latitudeVarInfo.Units = "°";
            latitudeVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            sDsa_shVarInfo.Name = "sDsa_sh";
            sDsa_shVarInfo.Description = "Sowing date at which Phyllochrone is maximum in southern hemispher";
            sDsa_shVarInfo.MaxValue = 365;
            sDsa_shVarInfo.MinValue = 1;
            sDsa_shVarInfo.DefaultValue = 1.0;
            sDsa_shVarInfo.Units = "d";
            sDsa_shVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            rpVarInfo.Name = "rp";
            rpVarInfo.Description = "Rate of change of Phyllochrone with sowing date";
            rpVarInfo.MaxValue = 365;
            rpVarInfo.MinValue = 0;
            rpVarInfo.DefaultValue = 0;
            rpVarInfo.Units = "d-1";
            rpVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            sDwsVarInfo.Name = "sDws";
            sDwsVarInfo.Description = "Sowing date at which Phyllochrone is minimum";
            sDwsVarInfo.MaxValue = 365;
            sDwsVarInfo.MinValue = 1;
            sDwsVarInfo.DefaultValue = 1;
            sDwsVarInfo.Units = "d";
            sDwsVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Integer");

            sDsa_nhVarInfo.Name = "sDsa_nh";
            sDsa_nhVarInfo.Description = "Sowing date at which Phyllochrone is maximum in northern hemispher";
            sDsa_nhVarInfo.MaxValue = 365;
            sDsa_nhVarInfo.MinValue = 1;
            sDsa_nhVarInfo.DefaultValue = 1.0;
            sDsa_nhVarInfo.Units = "d";
            sDsa_nhVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            pVarInfo.Name = "p";
            pVarInfo.Description = "Phyllochron (Varietal parameter)";
            pVarInfo.MaxValue = 1000;
            pVarInfo.MinValue = 0;
            pVarInfo.DefaultValue = 120;
            pVarInfo.Units = "°C d leaf-1";
            pVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
        }

        private static VarInfo _sowingDayVarInfo = new VarInfo();
        public static VarInfo sowingDayVarInfo
        {
            get { return _sowingDayVarInfo;} 
        }

        private static VarInfo _latitudeVarInfo = new VarInfo();
        public static VarInfo latitudeVarInfo
        {
            get { return _latitudeVarInfo;} 
        }

        private static VarInfo _sDsa_shVarInfo = new VarInfo();
        public static VarInfo sDsa_shVarInfo
        {
            get { return _sDsa_shVarInfo;} 
        }

        private static VarInfo _rpVarInfo = new VarInfo();
        public static VarInfo rpVarInfo
        {
            get { return _rpVarInfo;} 
        }

        private static VarInfo _sDwsVarInfo = new VarInfo();
        public static VarInfo sDwsVarInfo
        {
            get { return _sDwsVarInfo;} 
        }

        private static VarInfo _sDsa_nhVarInfo = new VarInfo();
        public static VarInfo sDsa_nhVarInfo
        {
            get { return _sDsa_nhVarInfo;} 
        }

        private static VarInfo _pVarInfo = new VarInfo();
        public static VarInfo pVarInfo
        {
            get { return _pVarInfo;} 
        }

        public string TestPostConditions(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.fixPhyll.CurrentValue=a.fixPhyll;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.fixPhyll);
                if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.fixPhyll.ValueType)){prc.AddCondition(r8);}
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
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("sowingDay")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("latitude")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("sDsa_sh")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("rp")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("sDws")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("sDsa_nh")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("p")));
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
            double fixPhyll;
            if (latitude < 0.0d)
            {
                if (sowingDay > (int)(sDsa_sh))
                {
                    fixPhyll = p * (1 - (rp * Math.Min((sowingDay - sDsa_sh), sDws)));
                }
                else
                {
                    fixPhyll = p;
                }
            }
            else
            {
                if (sowingDay < (int)(sDsa_nh))
                {
                    fixPhyll = p * (1 - (rp * Math.Min(sowingDay, sDws)));
                }
                else
                {
                    fixPhyll = p;
                }
            }
            a.fixPhyll= fixPhyll;
        }

    }
}