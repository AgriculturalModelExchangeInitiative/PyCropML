
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualityPhenology.DomainClass
{
    public class PhenologyAuxiliaryVarInfo : IVarInfoClass
    {
        static VarInfo _currentdate = new VarInfo();
        static VarInfo _cumulTT = new VarInfo();
        static VarInfo _dayLength = new VarInfo();
        static VarInfo _deltaTT = new VarInfo();
        static VarInfo _gAI = new VarInfo();
        static VarInfo _pAR = new VarInfo();
        static VarInfo _grainCumulTT = new VarInfo();
        static VarInfo _fixPhyll = new VarInfo();
        static VarInfo _cumulTTFromZC_39 = new VarInfo();
        static VarInfo _cumulTTFromZC_91 = new VarInfo();
        static VarInfo _cumulTTFromZC_65 = new VarInfo();

        static PhenologyAuxiliaryVarInfo()
        {
            PhenologyAuxiliaryVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "PhenologyAuxiliary Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "PhenologyAuxiliary";}
        }

        public static  VarInfo currentdate
        {
            get { return _currentdate;}
        }

        public static  VarInfo cumulTT
        {
            get { return _cumulTT;}
        }

        public static  VarInfo dayLength
        {
            get { return _dayLength;}
        }

        public static  VarInfo deltaTT
        {
            get { return _deltaTT;}
        }

        public static  VarInfo gAI
        {
            get { return _gAI;}
        }

        public static  VarInfo pAR
        {
            get { return _pAR;}
        }

        public static  VarInfo grainCumulTT
        {
            get { return _grainCumulTT;}
        }

        public static  VarInfo fixPhyll
        {
            get { return _fixPhyll;}
        }

        public static  VarInfo cumulTTFromZC_39
        {
            get { return _cumulTTFromZC_39;}
        }

        public static  VarInfo cumulTTFromZC_91
        {
            get { return _cumulTTFromZC_91;}
        }

        public static  VarInfo cumulTTFromZC_65
        {
            get { return _cumulTTFromZC_65;}
        }

        static void DescribeVariables()
        {
            _currentdate.Name = "currentdate";
            _currentdate.Description = "current date ";
            _currentdate.MaxValue = -1D;
            _currentdate.MinValue = -1D;
            _currentdate.DefaultValue = -1D;
            _currentdate.Units = "";
            _currentdate.ValueType = VarInfoValueTypes.GetInstanceForName("Date");

            _cumulTT.Name = "cumulTT";
            _cumulTT.Description = "cumul thermal times at currentdate";
            _cumulTT.MaxValue = 10000;
            _cumulTT.MinValue = -200;
            _cumulTT.DefaultValue = 112.330110409888;
            _cumulTT.Units = "°C d";
            _cumulTT.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _dayLength.Name = "dayLength";
            _dayLength.Description = "day length";
            _dayLength.MaxValue = 10000;
            _dayLength.MinValue = 0;
            _dayLength.DefaultValue = 12.3037621834005;
            _dayLength.Units = "mm2 m-2";
            _dayLength.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _deltaTT.Name = "deltaTT";
            _deltaTT.Description = "Thermal time increase of the day";
            _deltaTT.MaxValue = 100.0;
            _deltaTT.MinValue = 0.0;
            _deltaTT.DefaultValue = 0.0;
            _deltaTT.Units = "°C d";
            _deltaTT.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _gAI.Name = "gAI";
            _gAI.Description = "Green Area Index of the day";
            _gAI.MaxValue = 500.0;
            _gAI.MinValue = 0.0;
            _gAI.DefaultValue = 0.0;
            _gAI.Units = "m2 leaf m-2 ground";
            _gAI.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _pAR.Name = "pAR";
            _pAR.Description = "Daily Photosyntetically Active Radiation";
            _pAR.MaxValue = 10000.0;
            _pAR.MinValue = 0.0;
            _pAR.DefaultValue = 0.0;
            _pAR.Units = "MJ m² d";
            _pAR.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _grainCumulTT.Name = "grainCumulTT";
            _grainCumulTT.Description = "cumulTT used for the grain developpment";
            _grainCumulTT.MaxValue = 10000;
            _grainCumulTT.MinValue = 0;
            _grainCumulTT.DefaultValue = 0;
            _grainCumulTT.Units = "°C d";
            _grainCumulTT.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _fixPhyll.Name = "fixPhyll";
            _fixPhyll.Description = " Phyllochron Varietal parameter ";
            _fixPhyll.MaxValue = 1000;
            _fixPhyll.MinValue = 0;
            _fixPhyll.DefaultValue = -1D;
            _fixPhyll.Units = "°C d leaf-1";
            _fixPhyll.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _cumulTTFromZC_39.Name = "cumulTTFromZC_39";
            _cumulTTFromZC_39.Description = " cumul TT from FlagLeafLiguleJustVisible to current date ";
            _cumulTTFromZC_39.MaxValue = 5000;
            _cumulTTFromZC_39.MinValue = 0;
            _cumulTTFromZC_39.DefaultValue = -1D;
            _cumulTTFromZC_39.Units = "°C d";
            _cumulTTFromZC_39.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _cumulTTFromZC_91.Name = "cumulTTFromZC_91";
            _cumulTTFromZC_91.Description = " cumul TT from EndGrainFilling to current date ";
            _cumulTTFromZC_91.MaxValue = 4000D;
            _cumulTTFromZC_91.MinValue = 0;
            _cumulTTFromZC_91.DefaultValue = -1D;
            _cumulTTFromZC_91.Units = "°C d";
            _cumulTTFromZC_91.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

            _cumulTTFromZC_65.Name = "cumulTTFromZC_65";
            _cumulTTFromZC_65.Description = " cumul TT from Anthesis to current date ";
            _cumulTTFromZC_65.MaxValue = -5000D;
            _cumulTTFromZC_65.MinValue = 0;
            _cumulTTFromZC_65.DefaultValue = -1D;
            _cumulTTFromZC_65.Units = "°C d";
            _cumulTTFromZC_65.ValueType = VarInfoValueTypes.GetInstanceForName("Double");

        }

    }
}