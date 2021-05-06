
using System;
using System.Collections.Generic;
using CRA.ModelLayer.Core;
using System.Reflection;
using CRA.ModelLayer.ParametersManagement;   

namespace SiriusQualityPhenology.DomainClass
{
    public class PhenologyExogenousVarInfo : IVarInfoClass
    {

        static PhenologyExogenousVarInfo()
        {
            PhenologyExogenousVarInfo.DescribeVariables();
        }

        public virtual string Description
        {
            get { return "PhenologyExogenous Domain class of the component";}
        }

        public string URL
        {
            get { return "http://" ;}
        }

        public string DomainClassOfReference
        {
            get { return "PhenologyExogenous";}
        }

        static void DescribeVariables()
        {
        }

    }
}