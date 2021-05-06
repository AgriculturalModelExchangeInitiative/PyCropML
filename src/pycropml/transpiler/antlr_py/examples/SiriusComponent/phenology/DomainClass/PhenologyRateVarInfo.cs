
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualityPhenology.DomainClass
{
    public class PhenologyRateVarInfo : IVarInfoClass
    {

        static PhenologyRateVarInfo()
        {
            PhenologyRateVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "PhenologyRate Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "PhenologyRate";}
        }

        static void DescribeVariables()
        {
        }

    }
}