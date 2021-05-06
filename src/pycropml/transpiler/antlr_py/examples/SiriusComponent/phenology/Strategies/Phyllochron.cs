
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
    public class Phyllochron : IStrategySiriusQualityPhenology
    {
        public Phyllochron()
        {
            ModellingOptions mo0_0 = new ModellingOptions();
            //Parameters
            List<VarInfo> _parameters0_0 = new List<VarInfo>();
            VarInfo v1 = new VarInfo();
            v1.DefaultValue = 8.0;
            v1.Description = "Leaf number above which the phyllochron is increased by Pincr";
            v1.Id = 0;
            v1.MaxValue = 30.0;
            v1.MinValue = 0.0;
            v1.Name = "lincr";
            v1.Size = 1;
            v1.Units = "leaf";
            v1.URL = "";
            v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v1.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v1);
            VarInfo v2 = new VarInfo();
            v2.DefaultValue = 0.0;
            v2.Description = "Leaf number up to which the phyllochron is decreased by Pdecr";
            v2.Id = 0;
            v2.MaxValue = 100.0;
            v2.MinValue = 0.0;
            v2.Name = "ldecr";
            v2.Size = 1;
            v2.Units = "leaf";
            v2.URL = "";
            v2.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v2.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v2);
            VarInfo v3 = new VarInfo();
            v3.DefaultValue = 0.4;
            v3.Description = "Factor decreasing the phyllochron for leaf number less than Ldecr";
            v3.Id = 0;
            v3.MaxValue = 10.0;
            v3.MinValue = 0.0;
            v3.Name = "pdecr";
            v3.Size = 1;
            v3.Units = "-";
            v3.URL = "";
            v3.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v3.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v3);
            VarInfo v4 = new VarInfo();
            v4.DefaultValue = 1.5;
            v4.Description = "Factor increasing the phyllochron for leaf number higher than Lincr";
            v4.Id = 0;
            v4.MaxValue = 10.0;
            v4.MinValue = 0.0;
            v4.Name = "pincr";
            v4.Size = 1;
            v4.Units = "-";
            v4.URL = "";
            v4.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v4.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v4);
            VarInfo v5 = new VarInfo();
            v5.DefaultValue = 0.45;
            v5.Description = "Exctinction Coefficient";
            v5.Id = 0;
            v5.MaxValue = 50.0;
            v5.MinValue = 0.0;
            v5.Name = "kl";
            v5.Size = 1;
            v5.Units = "-";
            v5.URL = "";
            v5.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v5.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v5);
            VarInfo v6 = new VarInfo();
            v6.DefaultValue = 0.0;
            v6.Description = "Slope to intercept ratio for Phyllochron  parametrization with PhotoThermal Quotient";
            v6.Id = 0;
            v6.MaxValue = 1000.0;
            v6.MinValue = 0.0;
            v6.Name = "pTQhf";
            v6.Size = 1;
            v6.Units = "°C d leaf-1";
            v6.URL = "";
            v6.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v6.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v6);
            VarInfo v7 = new VarInfo();
            v7.DefaultValue = 20.0;
            v7.Description = "Phyllochron at PTQ equal 1";
            v7.Id = 0;
            v7.MaxValue = 1000.0;
            v7.MinValue = 0.0;
            v7.Name = "B";
            v7.Size = 1;
            v7.Units = "°C d leaf-1";
            v7.URL = "";
            v7.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v7.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v7);
            VarInfo v8 = new VarInfo();
            v8.DefaultValue = 120.0;
            v8.Description = "Phyllochron (Varietal parameter)";
            v8.Id = 0;
            v8.MaxValue = 1000.0;
            v8.MinValue = 0.0;
            v8.Name = "p";
            v8.Size = 1;
            v8.Units = "°C d leaf-1";
            v8.URL = "";
            v8.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v8.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v8);
            VarInfo v9 = new VarInfo();
            v9.DefaultValue = -1D;
            v9.Description = "Switch to choose the type of phyllochron calculation to be used";
            v9.Id = 0;
            v9.MaxValue = -1D;
            v9.MinValue = -1D;
            v9.Name = "choosePhyllUse";
            v9.Size = 1;
            v9.Units = "-";
            v9.URL = "";
            v9.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v9.ValueType = VarInfoValueTypes.GetInstanceForName("String");
            _parameters0_0.Add(v9);
            VarInfo v10 = new VarInfo();
            v10.DefaultValue = 0.0;
            v10.Description = " Area Leaf";
            v10.Id = 0;
            v10.MaxValue = 1000.0;
            v10.MinValue = 0.0;
            v10.Name = "areaSL";
            v10.Size = 1;
            v10.Units = "cm2";
            v10.URL = "";
            v10.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v10.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v10);
            VarInfo v11 = new VarInfo();
            v11.DefaultValue = 0.0;
            v11.Description = "Area Sheath";
            v11.Id = 0;
            v11.MaxValue = 1000.0;
            v11.MinValue = 0.0;
            v11.Name = "areaSS";
            v11.Size = 1;
            v11.Units = "cm2";
            v11.URL = "";
            v11.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v11.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v11);
            VarInfo v12 = new VarInfo();
            v12.DefaultValue = 0.0;
            v12.Description = "LAR minimum";
            v12.Id = 0;
            v12.MaxValue = 1000.0;
            v12.MinValue = 0.0;
            v12.Name = "lARmin";
            v12.Size = 1;
            v12.Units = "leaf-1 °C";
            v12.URL = "";
            v12.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v12.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v12);
            VarInfo v13 = new VarInfo();
            v13.DefaultValue = 0.0;
            v13.Description = "LAR maximum";
            v13.Id = 0;
            v13.MaxValue = 1000.0;
            v13.MinValue = 0.0;
            v13.Name = "lARmax";
            v13.Size = 1;
            v13.Units = "leaf-1 °C";
            v13.URL = "";
            v13.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v13.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v13);
            VarInfo v14 = new VarInfo();
            v14.DefaultValue = 0.0;
            v14.Description = "Sowing Density";
            v14.Id = 0;
            v14.MaxValue = 1000.0;
            v14.MinValue = 0.0;
            v14.Name = "sowingDensity";
            v14.Size = 1;
            v14.Units = "plant m-2";
            v14.URL = "";
            v14.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v14.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v14);
            VarInfo v15 = new VarInfo();
            v15.DefaultValue = 0.0;
            v15.Description = "Leaf Number efficace";
            v15.Id = 0;
            v15.MaxValue = 1000.0;
            v15.MinValue = 0.0;
            v15.Name = "lNeff";
            v15.Size = 1;
            v15.Units = "leaf";
            v15.URL = "";
            v15.VarType = CRA.ModelLayer.Core.VarInfo.Type.PARAMETER;
            v15.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
            _parameters0_0.Add(v15);
            mo0_0.Parameters=_parameters0_0;

            //Inputs
            List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd1 = new PropertyDescription();
            pd1.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyAuxiliary);
            pd1.PropertyName = "fixPhyll";
            pd1.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.fixPhyll).ValueType.TypeForCurrentValue;
            pd1.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.fixPhyll);
            _inputs0_0.Add(pd1);
            PropertyDescription pd2 = new PropertyDescription();
            pd2.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd2.PropertyName = "leafNumber";
            pd2.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber).ValueType.TypeForCurrentValue;
            pd2.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber);
            _inputs0_0.Add(pd2);
            PropertyDescription pd3 = new PropertyDescription();
            pd3.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd3.PropertyName = "ptq";
            pd3.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq).ValueType.TypeForCurrentValue;
            pd3.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq);
            _inputs0_0.Add(pd3);
            PropertyDescription pd4 = new PropertyDescription();
            pd4.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd4.PropertyName = "gAImean";
            pd4.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.gAImean).ValueType.TypeForCurrentValue;
            pd4.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.gAImean);
            _inputs0_0.Add(pd4);
            mo0_0.Inputs=_inputs0_0;

            //Outputs
            List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
            PropertyDescription pd5 = new PropertyDescription();
            pd5.DomainClassType = typeof(SiriusQualityPhenology.DomainClass.PhenologyState);
            pd5.PropertyName = "phyllochron";
            pd5.PropertyType = (SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron).ValueType.TypeForCurrentValue;
            pd5.PropertyVarInfo =(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron);
            _outputs0_0.Add(pd5);
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
            get { return "Calculate different types of phyllochron " ;}
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

        public double lincr
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("lincr");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'lincr' not found (or found null) in strategy 'Phyllochron'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("lincr");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'lincr' not found in strategy 'Phyllochron'");
            }
        }
        public double ldecr
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("ldecr");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'ldecr' not found (or found null) in strategy 'Phyllochron'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("ldecr");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'ldecr' not found in strategy 'Phyllochron'");
            }
        }
        public double pdecr
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("pdecr");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'pdecr' not found (or found null) in strategy 'Phyllochron'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("pdecr");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'pdecr' not found in strategy 'Phyllochron'");
            }
        }
        public double pincr
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("pincr");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'pincr' not found (or found null) in strategy 'Phyllochron'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("pincr");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'pincr' not found in strategy 'Phyllochron'");
            }
        }
        public double kl
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("kl");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'kl' not found (or found null) in strategy 'Phyllochron'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("kl");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'kl' not found in strategy 'Phyllochron'");
            }
        }
        public double pTQhf
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("pTQhf");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'pTQhf' not found (or found null) in strategy 'Phyllochron'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("pTQhf");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'pTQhf' not found in strategy 'Phyllochron'");
            }
        }
        public double B
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("B");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'B' not found (or found null) in strategy 'Phyllochron'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("B");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'B' not found in strategy 'Phyllochron'");
            }
        }
        public double p
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("p");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'p' not found (or found null) in strategy 'Phyllochron'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("p");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'p' not found in strategy 'Phyllochron'");
            }
        }
        public string choosePhyllUse
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("choosePhyllUse");
                if (vi != null && vi.CurrentValue!=null) return (string)vi.CurrentValue ;
                else throw new Exception("Parameter 'choosePhyllUse' not found (or found null) in strategy 'Phyllochron'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("choosePhyllUse");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'choosePhyllUse' not found in strategy 'Phyllochron'");
            }
        }
        public double areaSL
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("areaSL");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'areaSL' not found (or found null) in strategy 'Phyllochron'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("areaSL");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'areaSL' not found in strategy 'Phyllochron'");
            }
        }
        public double areaSS
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("areaSS");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'areaSS' not found (or found null) in strategy 'Phyllochron'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("areaSS");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'areaSS' not found in strategy 'Phyllochron'");
            }
        }
        public double lARmin
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("lARmin");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'lARmin' not found (or found null) in strategy 'Phyllochron'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("lARmin");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'lARmin' not found in strategy 'Phyllochron'");
            }
        }
        public double lARmax
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("lARmax");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'lARmax' not found (or found null) in strategy 'Phyllochron'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("lARmax");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'lARmax' not found in strategy 'Phyllochron'");
            }
        }
        public double sowingDensity
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("sowingDensity");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'sowingDensity' not found (or found null) in strategy 'Phyllochron'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("sowingDensity");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'sowingDensity' not found in strategy 'Phyllochron'");
            }
        }
        public double lNeff
        {
            get { 
                VarInfo vi= _modellingOptionsManager.GetParameterByName("lNeff");
                if (vi != null && vi.CurrentValue!=null) return (double)vi.CurrentValue ;
                else throw new Exception("Parameter 'lNeff' not found (or found null) in strategy 'Phyllochron'");
            } set {
                VarInfo vi = _modellingOptionsManager.GetParameterByName("lNeff");
                if (vi != null)  vi.CurrentValue=value;
                else throw new Exception("Parameter 'lNeff' not found in strategy 'Phyllochron'");
            }
        }

        public void SetParametersDefaultValue()
        {
            _modellingOptionsManager.SetParametersDefaultValue();
        }

        private static void SetStaticParametersVarInfoDefinitions()
        {

            lincrVarInfo.Name = "lincr";
            lincrVarInfo.Description = "Leaf number above which the phyllochron is increased by Pincr";
            lincrVarInfo.MaxValue = 30.0;
            lincrVarInfo.MinValue = 0.0;
            lincrVarInfo.DefaultValue = 8.0;
            lincrVarInfo.Units = "leaf";
            lincrVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            ldecrVarInfo.Name = "ldecr";
            ldecrVarInfo.Description = "Leaf number up to which the phyllochron is decreased by Pdecr";
            ldecrVarInfo.MaxValue = 100.0;
            ldecrVarInfo.MinValue = 0.0;
            ldecrVarInfo.DefaultValue = 0.0;
            ldecrVarInfo.Units = "leaf";
            ldecrVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            pdecrVarInfo.Name = "pdecr";
            pdecrVarInfo.Description = "Factor decreasing the phyllochron for leaf number less than Ldecr";
            pdecrVarInfo.MaxValue = 10.0;
            pdecrVarInfo.MinValue = 0.0;
            pdecrVarInfo.DefaultValue = 0.4;
            pdecrVarInfo.Units = "-";
            pdecrVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            pincrVarInfo.Name = "pincr";
            pincrVarInfo.Description = "Factor increasing the phyllochron for leaf number higher than Lincr";
            pincrVarInfo.MaxValue = 10.0;
            pincrVarInfo.MinValue = 0.0;
            pincrVarInfo.DefaultValue = 1.5;
            pincrVarInfo.Units = "-";
            pincrVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            klVarInfo.Name = "kl";
            klVarInfo.Description = "Exctinction Coefficient";
            klVarInfo.MaxValue = 50.0;
            klVarInfo.MinValue = 0.0;
            klVarInfo.DefaultValue = 0.45;
            klVarInfo.Units = "-";
            klVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            pTQhfVarInfo.Name = "pTQhf";
            pTQhfVarInfo.Description = "Slope to intercept ratio for Phyllochron  parametrization with PhotoThermal Quotient";
            pTQhfVarInfo.MaxValue = 1000.0;
            pTQhfVarInfo.MinValue = 0.0;
            pTQhfVarInfo.DefaultValue = 0.0;
            pTQhfVarInfo.Units = "°C d leaf-1";
            pTQhfVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            BVarInfo.Name = "B";
            BVarInfo.Description = "Phyllochron at PTQ equal 1";
            BVarInfo.MaxValue = 1000.0;
            BVarInfo.MinValue = 0.0;
            BVarInfo.DefaultValue = 20.0;
            BVarInfo.Units = "°C d leaf-1";
            BVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            pVarInfo.Name = "p";
            pVarInfo.Description = "Phyllochron (Varietal parameter)";
            pVarInfo.MaxValue = 1000.0;
            pVarInfo.MinValue = 0.0;
            pVarInfo.DefaultValue = 120.0;
            pVarInfo.Units = "°C d leaf-1";
            pVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            choosePhyllUseVarInfo.Name = "choosePhyllUse";
            choosePhyllUseVarInfo.Description = "Switch to choose the type of phyllochron calculation to be used";
            choosePhyllUseVarInfo.MaxValue = -1D;
            choosePhyllUseVarInfo.MinValue = -1D;
            choosePhyllUseVarInfo.DefaultValue = -1D;
            choosePhyllUseVarInfo.Units = "-";
            choosePhyllUseVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("String");

            areaSLVarInfo.Name = "areaSL";
            areaSLVarInfo.Description = " Area Leaf";
            areaSLVarInfo.MaxValue = 1000.0;
            areaSLVarInfo.MinValue = 0.0;
            areaSLVarInfo.DefaultValue = 0.0;
            areaSLVarInfo.Units = "cm2";
            areaSLVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            areaSSVarInfo.Name = "areaSS";
            areaSSVarInfo.Description = "Area Sheath";
            areaSSVarInfo.MaxValue = 1000.0;
            areaSSVarInfo.MinValue = 0.0;
            areaSSVarInfo.DefaultValue = 0.0;
            areaSSVarInfo.Units = "cm2";
            areaSSVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            lARminVarInfo.Name = "lARmin";
            lARminVarInfo.Description = "LAR minimum";
            lARminVarInfo.MaxValue = 1000.0;
            lARminVarInfo.MinValue = 0.0;
            lARminVarInfo.DefaultValue = 0.0;
            lARminVarInfo.Units = "leaf-1 °C";
            lARminVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            lARmaxVarInfo.Name = "lARmax";
            lARmaxVarInfo.Description = "LAR maximum";
            lARmaxVarInfo.MaxValue = 1000.0;
            lARmaxVarInfo.MinValue = 0.0;
            lARmaxVarInfo.DefaultValue = 0.0;
            lARmaxVarInfo.Units = "leaf-1 °C";
            lARmaxVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            sowingDensityVarInfo.Name = "sowingDensity";
            sowingDensityVarInfo.Description = "Sowing Density";
            sowingDensityVarInfo.MaxValue = 1000.0;
            sowingDensityVarInfo.MinValue = 0.0;
            sowingDensityVarInfo.DefaultValue = 0.0;
            sowingDensityVarInfo.Units = "plant m-2";
            sowingDensityVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            lNeffVarInfo.Name = "lNeff";
            lNeffVarInfo.Description = "Leaf Number efficace";
            lNeffVarInfo.MaxValue = 1000.0;
            lNeffVarInfo.MinValue = 0.0;
            lNeffVarInfo.DefaultValue = 0.0;
            lNeffVarInfo.Units = "leaf";
            lNeffVarInfo.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
        }

        private static VarInfo _lincrVarInfo = new VarInfo();
        public static VarInfo lincrVarInfo
        {
            get { return _lincrVarInfo;} 
        }

        private static VarInfo _ldecrVarInfo = new VarInfo();
        public static VarInfo ldecrVarInfo
        {
            get { return _ldecrVarInfo;} 
        }

        private static VarInfo _pdecrVarInfo = new VarInfo();
        public static VarInfo pdecrVarInfo
        {
            get { return _pdecrVarInfo;} 
        }

        private static VarInfo _pincrVarInfo = new VarInfo();
        public static VarInfo pincrVarInfo
        {
            get { return _pincrVarInfo;} 
        }

        private static VarInfo _klVarInfo = new VarInfo();
        public static VarInfo klVarInfo
        {
            get { return _klVarInfo;} 
        }

        private static VarInfo _pTQhfVarInfo = new VarInfo();
        public static VarInfo pTQhfVarInfo
        {
            get { return _pTQhfVarInfo;} 
        }

        private static VarInfo _BVarInfo = new VarInfo();
        public static VarInfo BVarInfo
        {
            get { return _BVarInfo;} 
        }

        private static VarInfo _pVarInfo = new VarInfo();
        public static VarInfo pVarInfo
        {
            get { return _pVarInfo;} 
        }

        private static VarInfo _choosePhyllUseVarInfo = new VarInfo();
        public static VarInfo choosePhyllUseVarInfo
        {
            get { return _choosePhyllUseVarInfo;} 
        }

        private static VarInfo _areaSLVarInfo = new VarInfo();
        public static VarInfo areaSLVarInfo
        {
            get { return _areaSLVarInfo;} 
        }

        private static VarInfo _areaSSVarInfo = new VarInfo();
        public static VarInfo areaSSVarInfo
        {
            get { return _areaSSVarInfo;} 
        }

        private static VarInfo _lARminVarInfo = new VarInfo();
        public static VarInfo lARminVarInfo
        {
            get { return _lARminVarInfo;} 
        }

        private static VarInfo _lARmaxVarInfo = new VarInfo();
        public static VarInfo lARmaxVarInfo
        {
            get { return _lARmaxVarInfo;} 
        }

        private static VarInfo _sowingDensityVarInfo = new VarInfo();
        public static VarInfo sowingDensityVarInfo
        {
            get { return _sowingDensityVarInfo;} 
        }

        private static VarInfo _lNeffVarInfo = new VarInfo();
        public static VarInfo lNeffVarInfo
        {
            get { return _lNeffVarInfo;} 
        }

        public string TestPostConditions(SiriusQualityPhenology.DomainClass.PhenologyState s,SiriusQualityPhenology.DomainClass.PhenologyState s1,SiriusQualityPhenology.DomainClass.PhenologyRate r,SiriusQualityPhenology.DomainClass.PhenologyAuxiliary a,SiriusQualityPhenology.DomainClass.PhenologyExogenous ex,string callID)
        {
            try
            {
                //Set current values of the outputs to the static VarInfo representing the output properties of the domain classes
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron.CurrentValue=s.phyllochron;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r20 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron);
                if(r20.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.phyllochron.ValueType)){prc.AddCondition(r20);}
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
                SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.fixPhyll.CurrentValue=a.fixPhyll;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber.CurrentValue=s.leafNumber;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq.CurrentValue=s.ptq;
                SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.gAImean.CurrentValue=s.gAImean;
                ConditionsCollection prc = new ConditionsCollection();
                Preconditions pre = new Preconditions(); 
                RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.fixPhyll);
                if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyAuxiliaryVarInfo.fixPhyll.ValueType)){prc.AddCondition(r1);}
                RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber);
                if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.leafNumber.ValueType)){prc.AddCondition(r2);}
                RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq);
                if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.ptq.ValueType)){prc.AddCondition(r3);}
                RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.gAImean);
                if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.DomainClass.PhenologyStateVarInfo.gAImean.ValueType)){prc.AddCondition(r4);}
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("lincr")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("ldecr")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("pdecr")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("pincr")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("kl")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("pTQhf")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("B")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("p")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("choosePhyllUse")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("areaSL")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("areaSS")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("lARmin")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("lARmax")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("sowingDensity")));
                prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("lNeff")));
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
            double fixPhyll = a.fixPhyll;
            double leafNumber = s.leafNumber;
            double ptq = s.ptq;
            double gAImean = s.gAImean;
            double phyllochron;
            double gaiLim;
            double LAR;
            phyllochron = 0.0d;
            LAR = 0.0d;
            gaiLim = lNeff * ((areaSL + areaSS) / 10000.0d) * sowingDensity;
            if (choosePhyllUse == "Default")
            {
                if (leafNumber < ldecr)
                {
                    phyllochron = fixPhyll * pdecr;
                }
                else if ( leafNumber >= ldecr && leafNumber < lincr)
                {
                    phyllochron = fixPhyll;
                }
                else
                {
                    phyllochron = fixPhyll * pincr;
                }
            }
            if (choosePhyllUse == "PTQ")
            {
                if (gAImean > gaiLim)
                {
                    LAR = (lARmin + ((lARmax - lARmin) * ptq / (pTQhf + ptq))) / (B * gAImean);
                }
                else
                {
                    LAR = (lARmin + ((lARmax - lARmin) * ptq / (pTQhf + ptq))) / (B * gaiLim);
                }
                phyllochron = 1.0d / LAR;
            }
            if (choosePhyllUse == "Test")
            {
                if (leafNumber < ldecr)
                {
                    phyllochron = p * pdecr;
                }
                else if ( leafNumber >= ldecr && leafNumber < lincr)
                {
                    phyllochron = p;
                }
                else
                {
                    phyllochron = p * pincr;
                }
            }
            s.phyllochron= phyllochron;
        }

    }
}