# coding: utf8
from copy import copy

import numpy
from math import *

def model_phyllochron(fixPhyll = 5.0,
         leafNumber = 0.0,
         lincr = 8.0,
         ldecr = 0.0,
         pdecr = 0.4,
         pincr = 1.5,
         ptq = 0.0,
         gAImean = 0.0,
         kl = 0.45,
         pTQhf = 0.0,
         B = 20.0,
         p = 120.0,
         choosePhyllUse = "Default",
         areaSL = 0.0,
         areaSS = 0.0,
         lARmin = 0.0,
         lARmax = 0.0,
         sowingDensity = 0.0,
         lNeff = 0.0):
    """
     - Name: Phyllochron -Version: 1.0, -Time step: 1
     - Description:
                 * Title: Phyllochron Model
                 * Author: Pierre Martre
                 * Reference: Modeling development phase in the 
                     Wheat Simulation Model SiriusQuality.
                     See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
                 * Institution: INRA Montpellier
                 * Abstract: Calculate different types of phyllochron 
     - inputs:
                 * name: fixPhyll
                               ** min : 0.0
                               ** default : 5.0
                               ** max : 10000.0
                               ** uri : some url
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d leaf-1
                               ** description : Sowing date corrected Phyllochron
                 * name: leafNumber
                               ** min : 0.0
                               ** default : 0.0
                               ** max : 25.0
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : leaf
                               ** description : Actual number of phytomers
                 * name: lincr
                               ** parametercategory : species
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 30.0
                               ** uri : some url
                               ** default : 8.0
                               ** inputtype : parameter
                               ** unit : leaf
                               ** description : Leaf number above which the phyllochron is increased by Pincr
                 * name: ldecr
                               ** parametercategory : species
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 100.0
                               ** uri : some url
                               ** default : 0.0
                               ** inputtype : parameter
                               ** unit : leaf
                               ** description : Leaf number up to which the phyllochron is decreased by Pdecr
                 * name: pdecr
                               ** parametercategory : species
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 10.0
                               ** uri : some url
                               ** default : 0.4
                               ** inputtype : parameter
                               ** unit : -
                               ** description : Factor decreasing the phyllochron for leaf number less than Ldecr
                 * name: pincr
                               ** parametercategory : species
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 10.0
                               ** uri : some url
                               ** default : 1.5
                               ** inputtype : parameter
                               ** unit : -
                               ** description : Factor increasing the phyllochron for leaf number higher than Lincr
                 * name: ptq
                               ** min : 0.0
                               ** default : 0.0
                               ** max : 10000.0
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : MJ °C-1 d-1 m-2)
                               ** description : Photothermal quotient 
                 * name: gAImean
                               ** min : 0.0
                               ** default : 0.0
                               ** max : 10000.0
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : m2 m-2
                               ** description : Green Area Index
                 * name: kl
                               ** parametercategory : species
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 50.0
                               ** uri : some url
                               ** default : 0.45
                               ** inputtype : parameter
                               ** unit : -
                               ** description : Exctinction Coefficient
                 * name: pTQhf
                               ** parametercategory : genotypic
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** uri : some url
                               ** default : 0.0
                               ** inputtype : parameter
                               ** unit : °C d leaf-1
                               ** description : Slope to intercept ratio for Phyllochron  parametrization with PhotoThermal Quotient
                 * name: B
                               ** parametercategory : species
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** uri : some url
                               ** default : 20.0
                               ** inputtype : parameter
                               ** unit : °C d leaf-1
                               ** description : Phyllochron at PTQ equal 1
                 * name: p
                               ** parametercategory : species
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** uri : some url
                               ** default : 120.0
                               ** inputtype : parameter
                               ** unit : °C d leaf-1
                               ** description : Phyllochron (Varietal parameter)
                 * name: choosePhyllUse
                               ** parametercategory : species
                               ** min : 
                               ** datatype : STRING
                               ** max : 
                               ** uri : some url
                               ** default : Default
                               ** inputtype : parameter
                               ** unit : -
                               ** description : Switch to choose the type of phyllochron calculation to be used
                 * name: areaSL
                               ** parametercategory : genotypic
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** uri : some url
                               ** default : 0.0
                               ** inputtype : parameter
                               ** unit : cm2
                               ** description :  Area Leaf
                 * name: areaSS
                               ** parametercategory : genotypic
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** uri : some url
                               ** default : 0.0
                               ** inputtype : parameter
                               ** unit : cm2
                               ** description : Area Sheath
                 * name: lARmin
                               ** parametercategory : genotypic
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** uri : some url
                               ** default : 0.0
                               ** inputtype : parameter
                               ** unit : leaf-1 °C
                               ** description : LAR minimum
                 * name: lARmax
                               ** parametercategory : genotypic
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** uri : some url
                               ** default : 0.0
                               ** inputtype : parameter
                               ** unit : leaf-1 °C
                               ** description : LAR maximum
                 * name: sowingDensity
                               ** parametercategory : genotypic
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** uri : some url
                               ** default : 0.0
                               ** inputtype : parameter
                               ** unit : plant m-2
                               ** description : Sowing Density
                 * name: lNeff
                               ** parametercategory : genotypic
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 1000.0
                               ** uri : some url
                               ** default : 0.0
                               ** inputtype : parameter
                               ** unit : leaf
                               ** description : Leaf Number efficace
     - outputs:
                 * name: phyllochron
                               ** min : 0
                               ** variablecategory : state
                               ** max : 1000
                               ** uri : some url
                               ** datatype : DOUBLE
                               ** unit :  °C d leaf-1
                               ** description :  the rate of leaf appearance 
    """

    phyllochron = 0.0
    LAR = 0.0
    gaiLim = lNeff * ((areaSL + areaSS) / 10000.0) * sowingDensity
    if choosePhyllUse == "Default":
        if leafNumber < ldecr:
            phyllochron = fixPhyll * pdecr
        elif leafNumber >= ldecr and leafNumber < lincr:
            phyllochron = fixPhyll
        else:
            phyllochron = fixPhyll * pincr
    if choosePhyllUse == "PTQ":
        if gAImean > gaiLim:
            LAR = (lARmin + ((lARmax - lARmin) * ptq / (pTQhf + ptq))) / (B * gAImean)
        else:
            LAR = (lARmin + ((lARmax - lARmin) * ptq / (pTQhf + ptq))) / (B * gaiLim)
        phyllochron = 1.0 / LAR
    if choosePhyllUse == "Test":
        if leafNumber < ldecr:
            phyllochron = p * pdecr
        elif leafNumber >= ldecr and leafNumber < lincr:
            phyllochron = p
        else:
            phyllochron = p * pincr
    return phyllochron