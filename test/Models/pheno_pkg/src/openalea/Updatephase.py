# coding: utf8
from copy import copy

import numpy
from math import *

def model_updatephase(cumulTT = 354.582294512,
         leafNumber_t1 = 4.62051162186,
         cumulTTFromZC_39 = 0.0,
         isMomentRegistredZC_39 = 0,
         gAI = 0.325519628514,
         grainCumulTT = 0.0,
         dayLength = 12.7433275303,
         vernaprog = 1.05325268296,
         minFinalNumber = 6.87941041399,
         fixPhyll = 91.2,
         isVernalizable = 1,
         dse = 105.0,
         pFLLAnth = 2.22,
         dcd = 100.0,
         dgf = 450.0,
         degfm = 0.0,
         maxDL = 15.0,
         sLDL = 0.85,
         ignoreGrainMaturation = False,
         pHEADANTH = 1.0,
         choosePhyllUse = "Default",
         p = 120.0,
         phase_t1 = 1.0,
         cumulTTFromZC_91 = 0.0,
         phyllochron = 91.2,
         hasLastPrimordiumAppeared_t1 = 0,
         finalLeafNumber_t1 = 0.0):
    """
     - Name: UpdatePhase -Version: 1.0, -Time step: 1
     - Description:
                 * Title: UpdatePhase Model
                 * Author: Pierre MARTRE
                 * Reference: Modeling development phase in the 
                     Wheat Simulation Model SiriusQuality.
                     See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
                 * Institution: INRA Montpellier
                 * Abstract: This strategy advances the phase and calculate the final leaf number
         	
     - inputs:
                 * name: cumulTT
                               ** min : -200
                               ** default : 354.582294511779
                               ** max : 10000
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : cumul thermal times at current date
                 * name: leafNumber_t1
                               ** min : 0
                               ** default :  4.620511621863958
                               ** max : 25
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : leaf
                               ** description : Actual number of phytomers
                 * name: cumulTTFromZC_39
                               ** min : 0
                               ** default : 0
                               ** max : 10000
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d-1
                               ** description : cumul of the thermal time ( DeltaTT) since the moment ZC_39
                 * name: isMomentRegistredZC_39
                               ** min : 0
                               ** default : 0
                               ** max : 1
                               ** variablecategory : state
                               ** datatype : INT
                               ** inputtype : variable
                               ** unit : 
                               ** description : true if ZC_39 is registered in the calendar
                 * name: gAI
                               ** min : 0
                               ** default : 0.3255196285135
                               ** max : 10000
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : 
                               ** description : used to calculate Terminal spikelet
                 * name: grainCumulTT
                               ** min : 0
                               ** default : 0
                               ** max : 10000
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : cumulTT used for the grain developpment
                 * name: dayLength
                               ** min : 0
                               ** default : 12.7433275303389
                               ** max : 24
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** inputtype : variable
                               ** unit : h
                               ** description : length of the day
                 * name: vernaprog
                               ** min : 0
                               ** default :  1.0532526829571554
                               ** max : 10
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : 
                               ** description : progression on a 0  to 1 scale of the vernalization
                 * name: minFinalNumber
                               ** min : 0
                               ** default : 6.879410413987549
                               ** max : 25
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : leaf
                               ** description : minimum final leaf number
                 * name: fixPhyll
                               ** min : 0
                               ** default : 91.2
                               ** max : 10000
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : Phyllochron with sowing date fix
                 * name: isVernalizable
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : INT
                               ** max : 1
                               ** default : 1
                               ** inputtype : parameter
                               ** unit : 
                               ** description : true if the plant is vernalizable
                 * name: dse
                               ** parametercategory : genotypic
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** default : 105
                               ** inputtype : parameter
                               ** unit : °C d
                               ** description : Thermal time from sowing to emergence
                 * name: pFLLAnth
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** default : 2.22
                               ** inputtype : parameter
                               ** unit : 
                               ** description : Phyllochronic duration of the period between flag leaf ligule appearance and anthesis
                 * name: dcd
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** default : 100
                               ** inputtype : parameter
                               ** unit : °C d
                               ** description : Duration of the endosperm cell division phase
                 * name: dgf
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** default : 450
                               ** inputtype : parameter
                               ** unit : °C d
                               ** description : Grain filling duration (from anthesis to physiological maturity)
                 * name: degfm
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 50
                               ** default : 0
                               ** inputtype : parameter
                               ** unit : °C d
                               ** description : Grain maturation duration (from physiological maturity to harvest ripeness)
                 * name: maxDL
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 24
                               ** default : 15
                               ** inputtype : parameter
                               ** unit : h
                               ** description : Saturating photoperiod above which final leaf number is not influenced by daylength
                 * name: sLDL
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1
                               ** default : 0.85
                               ** inputtype : parameter
                               ** unit : leaf h-1
                               ** description : Daylength response of leaf production
                 * name: ignoreGrainMaturation
                               ** parametercategory : species
                               ** default : FALSE
                               ** datatype : BOOLEAN
                               ** inputtype : parameter
                               ** unit : 
                               ** description : true to ignore grain maturation
                 * name: pHEADANTH
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** default : 1
                               ** inputtype : parameter
                               ** unit : 
                               ** description : Number of phyllochron between heading and anthesiss
                 * name: choosePhyllUse
                               ** parametercategory : species
                               ** default : Default
                               ** datatype : STRING
                               ** inputtype : parameter
                               ** unit : 
                               ** description : Switch to choose the type of phyllochron calculation to be used
                 * name: p
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** default : 120
                               ** inputtype : parameter
                               ** unit : °C d leaf-1
                               ** description : Phyllochron (Varietal parameter)
                 * name: phase_t1
                               ** min : 0
                               ** default : 1
                               ** max : 7
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : 
                               ** description :  the name of the phase
                 * name: cumulTTFromZC_91
                               ** min : 0
                               ** default : 0
                               ** max : 5000
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d-1
                               ** description : cumul of the thermal time (DeltaTT) since the moment ZC_91
                 * name: phyllochron
                               ** min : 0
                               ** default : 91.2
                               ** max : 1000
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d leaf-1
                               ** description : Phyllochron
                 * name: hasLastPrimordiumAppeared_t1
                               ** min : 0
                               ** default : 0
                               ** max : 1
                               ** variablecategory : state
                               ** datatype : INT
                               ** inputtype : variable
                               ** unit : 
                               ** description : if Last Primordium has Appeared
                 * name: finalLeafNumber_t1
                               ** min : 0
                               ** default : 0
                               ** max : 25
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : leaf
                               ** description : final leaf number
     - outputs:
                 * name: finalLeafNumber
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : state
                               ** max : 25
                               ** unit : leaf
                               ** description : final leaf number
                 * name: phase
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : state
                               ** max : 7
                               ** unit : 
                               ** description : the name of the phase
                 * name: hasLastPrimordiumAppeared
                               ** datatype : INT
                               ** min : 0
                               ** variablecategory : state
                               ** max : 1
                               ** unit : 
                               ** description : if Last Primordium has Appeared
    """

    hasLastPrimordiumAppeared = hasLastPrimordiumAppeared_t1
    finalLeafNumber = finalLeafNumber_t1
    phase = phase_t1
    if phase_t1 >= 0.0 and phase_t1 < 1.0:
        if cumulTT >= dse:
            phase = 1.0
        else:
            phase = phase_t1
    elif phase_t1 >= 1.0 and phase_t1 < 2.0:
        if isVernalizable == 1 and vernaprog >= 1.0 or isVernalizable == 0:
            if dayLength > maxDL:
                finalLeafNumber = minFinalNumber
                hasLastPrimordiumAppeared = 1
            else:
                appFLN = minFinalNumber + (sLDL * (maxDL - dayLength))
                if appFLN / 2.0 <= leafNumber_t1:
                    finalLeafNumber = appFLN
                    hasLastPrimordiumAppeared = 1
                else:
                    phase = phase_t1
            if hasLastPrimordiumAppeared == 1:
                phase = 2.0
        else:
            phase = phase_t1
    elif phase_t1 >= 2.0 and phase_t1 < 4.0:
        if isMomentRegistredZC_39 == 1:
            if phase_t1 < 3.0:
                ttFromLastLeafToHeading = 0.0
                if choosePhyllUse == "Default":
                    ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * fixPhyll
                elif choosePhyllUse == "PTQ":
                    ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * phyllochron
                elif choosePhyllUse == "Test":
                    ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * p
                if cumulTTFromZC_39 >= ttFromLastLeafToHeading:
                    phase = 3.0
                else:
                    phase = phase_t1
            else:
                phase = phase_t1
            ttFromLastLeafToAnthesis = 0.0
            if choosePhyllUse == "Default":
                ttFromLastLeafToAnthesis = pFLLAnth * fixPhyll
            elif choosePhyllUse == "PTQ":
                ttFromLastLeafToAnthesis = pFLLAnth * phyllochron
            elif choosePhyllUse == "Test":
                ttFromLastLeafToAnthesis = pFLLAnth * p
            if cumulTTFromZC_39 >= ttFromLastLeafToAnthesis:
                phase = 4.0
        else:
            phase = phase_t1
    elif phase_t1 == 4.0:
        if grainCumulTT >= dcd:
            phase = 4.5
        else:
            phase = phase_t1
    elif phase_t1 == 4.5:
        if grainCumulTT >= dgf or gAI <= 0.0:
            phase = 5.0
        else:
            phase = phase_t1
    elif phase_t1 >= 5.0 and phase_t1 < 6.0:
        localDegfm = degfm
        if ignoreGrainMaturation:
            localDegfm = -1.0
        if cumulTTFromZC_91 >= localDegfm:
            phase = 6.0
        else:
            phase = phase_t1
    elif phase_t1 >= 6.0 and phase_t1 < 7.0:
        phase = phase_t1
    return (finalLeafNumber, phase, hasLastPrimordiumAppeared)