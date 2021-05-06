# coding: utf8
from pycropml.units import u
from copy import copy
from array import array

from datetime import datetime
from math import *
from Phyllochron import model_phyllochron
from Phylsowingdatecorrection import model_phylsowingdatecorrection
from Shootnumber import model_shootnumber
from Updateleafflag import model_updateleafflag
from Updatephase import model_updatephase
from Leafnumber import model_leafnumber
from Vernalizationprogress import model_vernalizationprogress
from Ismomentregistredzc_39 import model_ismomentregistredzc_39
from Cumulttfrom import model_cumulttfrom
from Updatecalendar import model_updatecalendar
from Registerzadok import model_registerzadok
from Ptq import model_ptq
from Gaimean import model_gaimean

def model_phenology(phyllochron_t1 = 0.0,
         minFinalNumber_t1 = 5.5,
         aMXLFNO = 24.0,
         currentdate = datetime(2007, 3, 27),
         cumulTT = 112.33011041,
         pNini = 4.0,
         sDsa_sh = 1.0,
         latitude = 0.0,
         kl = 0.45,
         calendarDates_t1 = [datetime(2007, 3, 21)],
         calendarMoments_t1 = ["Sowing"],
         lincr = 8.0,
         ldecr = 0.0,
         pincr = 1.5,
         ptq = 0.0,
         pTQhf = 0.0,
         B = 20.0,
         areaSL = 0.0,
         areaSS = 0.0,
         lARmin = 0.0,
         sowingDensity = 0.0,
         lARmax = 0.0,
         lNeff = 0.0,
         rp = 0.0,
         p = 120.0,
         pdecr = 0.4,
         leafNumber_t1 = 0.0,
         maxTvern = 23.0,
         dayLength = 12.3037621834,
         deltaTT = 0.0,
         pastMaxAI_t1 = 0.0,
         tTWindowForPTQ = 0.0,
         listGAITTWindowForPTQ_t1 = [0.0],
         gAI = 0.0,
         pAR = 0.0,
         listPARTTWindowForPTQ_t1 = [0.0],
         listTTShootWindowForPTQ1_t1 = [0.0],
         listTTShootWindowForPTQ_t1 = [0.0],
         vBEE = 0.01,
         calendarCumuls_t1 = [0.0],
         isVernalizable = 1,
         vernaprog_t1 = 0.551725418738,
         minTvern = 0.0,
         intTvern = 11.0,
         vAI = 0.015,
         maxDL = 15.0,
         choosePhyllUse = "Default",
         minDL = 8.0,
         hasLastPrimordiumAppeared_t1 = 0,
         phase_t1 = 1.0,
         pFLLAnth = 2.22,
         dcd = 100.0,
         dgf = 450.0,
         degfm = 0.0,
         ignoreGrainMaturation = False,
         pHEADANTH = 1.0,
         finalLeafNumber_t1 = 0.0,
         sLDL = 0.85,
         grainCumulTT = 0.0,
         sowingDay = 1,
         hasZadokStageChanged_t1 = 0,
         currentZadokStage = "MainShootPlus1Tiller",
         sowingDate = datetime(2007, 3, 21),
         sDws = 1,
         sDsa_nh = 1.0,
         hasFlagLeafLiguleAppeared = 0,
         der = 300.0,
         hasFlagLeafLiguleAppeared_t1 = 1,
         tilleringProfile_t1 = [288.0],
         targetFertileShoot = 600.0,
         leafTillerNumberArray_t1 = [1, 1, 1],
         dse = 105.0,
         slopeTSFLN = 0.9,
         intTSFLN = 0.9,
         canopyShootNumber_t1 = 288.0):
    """
     - Name: Phenology -Version: 001, -Time step: 1
     - Description:
                 * Title: Phenology
                 * Author: Pierre MARTRE
                 * Reference: Modeling development phase in the 
                     Wheat Simulation Model SiriusQuality.
                     See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
                 * Institution: INRA/LEPSE
                 * Abstract: see documentation
     - inputs:
                 * name: phyllochron_t1
                               ** min : 0
                               ** default : 0
                               ** max : 1000
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d leaf-1
                               ** description : phyllochron
                 * name: minFinalNumber_t1
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 25
                               ** default : 5.5
                               ** variablecategory : state
                               ** inputtype : variable
                               ** unit : leaf
                               ** description : minimum final leaf number
                 * name: aMXLFNO
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 25
                               ** default : 24.0
                               ** inputtype : parameter
                               ** unit : leaf
                               ** description : Absolute maximum leaf number
                 * name: currentdate
                               ** variablecategory : auxiliary
                               ** datatype : DATE
                               ** default : 2007/3/27
                               ** inputtype : variable
                               ** unit : 
                               ** description : current date 
                 * name: cumulTT
                               ** min : -200
                               ** default : 112.330110409888
                               ** max : 10000
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : cumul thermal times at currentdate
                 * name: pNini
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 24
                               ** default : 4.0
                               ** inputtype : parameter
                               ** unit : primordia
                               ** description : Number of primorida in the apex at emergence
                 * name: sDsa_sh
                               ** parametercategory : species
                               ** min : 1
                               ** datatype : DOUBLE
                               ** max : 365
                               ** uri : some url
                               ** default : 1.0
                               ** inputtype : parameter
                               ** unit : d
                               ** description : Sowing date at which Phyllochrone is maximum in southern hemispher
                 * name: latitude
                               ** parametercategory : soil
                               ** min : -90
                               ** datatype : DOUBLE
                               ** max : 90
                               ** uri : some url
                               ** default : 0.0
                               ** inputtype : parameter
                               ** unit : °
                               ** description : Latitude
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
                 * name: calendarDates_t1
                               ** variablecategory : state
                               ** datatype : DATELIST
                               ** default : ['2007/3/21']
                               ** inputtype : variable
                               ** unit : 
                               ** description : List containing  the dates of the wheat developmental phases
                 * name: calendarMoments_t1
                               ** variablecategory : state
                               ** datatype : STRINGLIST
                               ** default : ['Sowing']
                               ** inputtype : variable
                               ** unit : 
                               ** description : List containing appearance of each stage at previous day
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
                 * name: rp
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 365
                               ** uri : some url
                               ** default : 0
                               ** inputtype : parameter
                               ** unit : d-1
                               ** description : Rate of change of Phyllochrone with sowing date
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
                 * name: leafNumber_t1
                               ** min : 0
                               ** default : 0
                               ** max : 25
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : leaf
                               ** description : Actual number of phytomers
                 * name: maxTvern
                               ** parametercategory : species
                               ** min : -20
                               ** datatype : DOUBLE
                               ** max : 60
                               ** default :  23.0
                               ** inputtype : parameter
                               ** unit : °C
                               ** description : Maximum temperature for vernalization to occur
                 * name: dayLength
                               ** min : 0
                               ** default : 12.3037621834005
                               ** max : 10000
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : mm2 m-2
                               ** description : day length
                 * name: deltaTT
                               ** min : 0.0
                               ** default : 0.0
                               ** max : 100.0
                               ** uri : 
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : Thermal time increase of the day
                 * name: pastMaxAI_t1
                               ** min : 0.0
                               ** default : 0.0
                               ** max : 5000.0
                               ** uri : 
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : m2 leaf m-2 ground
                               ** description : Maximum Leaf Area Index reached the current day
                 * name: tTWindowForPTQ
                               ** parametercategory : constant
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 5000.0
                               ** uri : 
                               ** default : 0.0
                               ** inputtype : parameter
                               ** unit : °C d
                               ** description : Thermal Time window for average
                 * name: listGAITTWindowForPTQ_t1
                               ** min : 
                               ** default : [0.0]
                               ** max : 
                               ** uri : 
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** inputtype : variable
                               ** unit : m2 leaf m-2 ground
                               ** description : List of daily Green Area Index in the window dedicated to average
                 * name: gAI
                               ** min : 0.0
                               ** default : 0.0
                               ** max : 500.0
                               ** uri : 
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : m2 leaf m-2 ground
                               ** description : Green Area Index of the day
                 * name: pAR
                               ** min : 0.0
                               ** default : 0.0
                               ** max : 10000.0
                               ** uri : some url
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : MJ m² d
                               ** description : Daily Photosyntetically Active Radiation
                 * name: listPARTTWindowForPTQ_t1
                               ** min : 
                               ** default : [0.0]
                               ** max : 
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** inputtype : variable
                               ** unit : MJ m2 d
                               ** description : List of Daily PAR during TTWindowForPTQ thermal time period
                 * name: listTTShootWindowForPTQ1_t1
                               ** min : 
                               ** default : [0.0]
                               ** max : 
                               ** uri : 
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : List of daily shoot thermal time in the window dedicated to average
                 * name: listTTShootWindowForPTQ_t1
                               ** min : 
                               ** default : [0.0]
                               ** max : 
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
                 * name: vBEE
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1
                               ** default : 0.01
                               ** inputtype : parameter
                               ** unit : d-1
                               ** description : Vernalization rate at 0°C
                 * name: calendarCumuls_t1
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** default : [0.0]
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : list containing for each stage occured its cumulated thermal times at previous day
                 * name: isVernalizable
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : INT
                               ** max : 1
                               ** default : 1
                               ** inputtype : parameter
                               ** unit : 
                               ** description : true if the plant is vernalizable
                 * name: vernaprog_t1
                               ** min : 0
                               ** default :  0.5517254187376879
                               ** max : 1
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : 
                               ** description : progression on a 0  to 1 scale of the vernalization
                 * name: minTvern
                               ** parametercategory : species
                               ** min : -20
                               ** datatype : DOUBLE
                               ** max : 60
                               ** default : 0.0
                               ** inputtype : parameter
                               ** unit : °C
                               ** description : Minimum temperature for vernalization to occur
                 * name: intTvern
                               ** parametercategory : species
                               ** min : -20
                               ** datatype : DOUBLE
                               ** max : 60
                               ** default :  11.0
                               ** inputtype : parameter
                               ** unit : °C
                               ** description : Intermediate temperature for vernalization to occur
                 * name: vAI
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1
                               ** default :  0.015
                               ** inputtype : parameter
                               ** unit : d-1 °C-1
                               ** description : Response of vernalization rate to temperature
                 * name: maxDL
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 24
                               ** default : 15.0
                               ** inputtype : parameter
                               ** unit : h
                               ** description : Saturating photoperiod above which final leaf number is not influenced by daylength
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
                 * name: minDL
                               ** parametercategory : species
                               ** min : 12
                               ** datatype : DOUBLE
                               ** max : 24
                               ** default : 8.0
                               ** inputtype : parameter
                               ** unit : h
                               ** description : Threshold daylength below which it does influence vernalization rate
                 * name: hasLastPrimordiumAppeared_t1
                               ** min : 0
                               ** default : 0
                               ** max : 1
                               ** variablecategory : state
                               ** datatype : INT
                               ** inputtype : variable
                               ** unit : 
                               ** description : if Last Primordium has Appeared
                 * name: phase_t1
                               ** min : 0
                               ** default : 1
                               ** max : 7
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : 
                               ** description :  the name of the phase
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
                 * name: finalLeafNumber_t1
                               ** min : 0
                               ** default : 0
                               ** max : 25
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : leaf
                               ** description : final leaf number
                 * name: sLDL
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1
                               ** default : 0.85
                               ** inputtype : parameter
                               ** unit : leaf h-1
                               ** description : Daylength response of leaf production
                 * name: grainCumulTT
                               ** min : 0
                               ** default : 0
                               ** max : 10000
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : cumulTT used for the grain developpment
                 * name: sowingDay
                               ** parametercategory : species
                               ** min : 1
                               ** datatype : INT
                               ** max : 365
                               ** uri : some url
                               ** default : 1
                               ** inputtype : parameter
                               ** unit : d
                               ** description : Day of Year at sowing
                 * name: hasZadokStageChanged_t1
                               ** min : 0
                               ** default : 0
                               ** max : 1
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : INT
                               ** inputtype : variable
                               ** unit : 
                               ** description : true if the zadok stage has changed this time step
                 * name: currentZadokStage
                               ** min : 
                               ** default : MainShootPlus1Tiller
                               ** max : 
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : STRING
                               ** inputtype : variable
                               ** unit : 
                               ** description : current zadok stage
                 * name: sowingDate
                               ** parametercategory : constant
                               ** min : 
                               ** datatype : DATE
                               ** max : 
                               ** default : 2007/3/21
                               ** inputtype : parameter
                               ** unit : 
                               ** description :  Date of Sowing
                 * name: sDws
                               ** parametercategory : species
                               ** min : 1
                               ** datatype : INT
                               ** max : 365
                               ** uri : some url
                               ** default : 1
                               ** inputtype : parameter
                               ** unit : d
                               ** description : Sowing date at which Phyllochrone is minimum
                 * name: sDsa_nh
                               ** parametercategory : species
                               ** min : 1
                               ** datatype : DOUBLE
                               ** max : 365
                               ** uri : some url
                               ** default : 1.0
                               ** inputtype : parameter
                               ** unit : d
                               ** description : Sowing date at which Phyllochrone is maximum in northern hemispher
                 * name: hasFlagLeafLiguleAppeared
                               ** min : 0
                               ** default : 0
                               ** max : 1
                               ** variablecategory : state
                               ** datatype : INT
                               ** inputtype : variable
                               ** unit : 
                               ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
                 * name: der
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** uri : some url
                               ** default : 300.0
                               ** inputtype : parameter
                               ** unit : °C d
                               ** description : Duration of the endosperm endoreduplication phase
                 * name: hasFlagLeafLiguleAppeared_t1
                               ** min : 0
                               ** default : 1
                               ** max : 1
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : INT
                               ** inputtype : variable
                               ** unit : 
                               ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
                 * name: tilleringProfile_t1
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** default : [288.0]
                               ** inputtype : variable
                               ** unit : 
                               ** description :  store the amount of new tiller created at each time a new tiller appears
                 * name: targetFertileShoot
                               ** parametercategory : species
                               ** min : 280
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** default : 600.0
                               ** inputtype : variable
                               ** unit : shoot
                               ** description : max value of shoot number for the canopy
                 * name: leafTillerNumberArray_t1
                               ** variablecategory : state
                               ** datatype : INTLIST
                               ** default : [1, 1, 1]
                               ** inputtype : variable
                               ** unit : leaf
                               ** description : store the number of tiller for each leaf layer
                 * name: dse
                               ** parametercategory : genotypic
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 1000
                               ** default : 105
                               ** inputtype : parameter
                               ** unit : °C d
                               ** description : Thermal time from sowing to emergence
                 * name: slopeTSFLN
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** uri : some url
                               ** default : 0.9
                               ** inputtype : parameter
                               ** unit : 
                               ** description : used to calculate Terminal spikelet
                 * name: intTSFLN
                               ** parametercategory : species
                               ** min : 0
                               ** datatype : DOUBLE
                               ** max : 10000
                               ** uri : some url
                               ** default : 0.9
                               ** inputtype : parameter
                               ** unit : 
                               ** description : used to calculate Terminal spikelet
                 * name: canopyShootNumber_t1
                               ** min : 0
                               ** default : 288.0
                               ** max : 10000
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : shoot m-2
                               ** description : shoot number for the whole canopy
     - outputs:
                 * name: currentZadokStage
                               ** datatype : STRING
                               ** variablecategory : state
                               ** uri : some url
                               ** unit :  
                               ** description : current zadok stage
                 * name: hasZadokStageChanged
                               ** min : 0
                               ** variablecategory : state
                               ** max : 1
                               ** uri : some url
                               ** datatype : INT
                               ** unit : 
                               ** description : true if the zadok stage has changed this time step
                 * name: hasFlagLeafLiguleAppeared
                               ** min : 0
                               ** variablecategory : state
                               ** max : 1
                               ** uri : some url
                               ** datatype : INT
                               ** unit : 
                               ** description : true if flag leaf has appeared (leafnumber reached finalLeafNumber)
                 * name: listPARTTWindowForPTQ
                               ** datatype : DOUBLELIST
                               ** min : 
                               ** variablecategory : state
                               ** max : 
                               ** unit : MJ m2 d
                               ** description :  List of Daily PAR during TTWindowForPTQ thermal time period
                 * name: hasLastPrimordiumAppeared
                               ** datatype : INT
                               ** min : 0
                               ** variablecategory : state
                               ** max : 1
                               ** unit : 
                               ** description : if Last Primordium has Appeared
                 * name: listTTShootWindowForPTQ
                               ** datatype : DOUBLELIST
                               ** min : 
                               ** variablecategory : state
                               ** max : 
                               ** unit : °C d
                               ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
                 * name: listTTShootWindowForPTQ1
                               ** min : 
                               ** variablecategory : state
                               ** max : 
                               ** uri : 
                               ** datatype : DOUBLELIST
                               ** unit : °C d
                               ** description : List of daily shoot thermal time in the window dedicated to average
                 * name: ptq
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : state
                               ** max : 10000
                               ** unit : MJ °C-1 d m-2)
                               ** description : Photothermal Quotient
                 * name: calendarMoments
                               ** variablecategory : state
                               ** datatype : STRINGLIST
                               ** unit : 
                               ** description :  List containing apparition of each stage
                 * name: canopyShootNumber
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : state
                               ** max : 10000
                               ** unit : shoot m-2
                               ** description : shoot number for the whole canopy
                 * name: calendarDates
                               ** variablecategory : state
                               ** datatype : DATELIST
                               ** unit : 
                               ** description :  List containing  the dates of the wheat developmental phases
                 * name: leafTillerNumberArray
                               ** variablecategory : state
                               ** datatype : INTLIST
                               ** unit : leaf
                               ** description : store the number of tiller for each leaf layer
                 * name: vernaprog
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : state
                               ** max : 10000
                               ** unit : 
                               ** description : progression on a 0  to 1 scale of the vernalization
                 * name: phyllochron
                               ** min : 0
                               ** variablecategory : state
                               ** max : 1000
                               ** uri : some url
                               ** datatype : DOUBLE
                               ** unit :  °C d leaf-1
                               ** description :  the rate of leaf appearance 
                 * name: leafNumber
                               ** min : 0
                               ** variablecategory : state
                               ** max : 10000
                               ** uri : some url
                               ** datatype : DOUBLE
                               ** unit : leaf
                               ** description : Actual number of phytomers
                 * name: numberTillerCohort
                               ** datatype : INT
                               ** min : 0
                               ** variablecategory : state
                               ** max : 10000
                               ** unit : dimensionless
                               ** description : Number of tiller which appears
                 * name: tilleringProfile
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** unit : dimensionless
                               ** description :  store the amount of new tiller created at each time a new tiller appears
                 * name: averageShootNumberPerPlant
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : state
                               ** max : 10000
                               ** unit : shoot m-2
                               ** description : average shoot number per plant in the canopy
                 * name: minFinalNumber
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : state
                               ** max : 10000
                               ** unit : leaf
                               ** description : minimum final leaf number
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
                 * name: listGAITTWindowForPTQ
                               ** min : 
                               ** variablecategory : state
                               ** max : 
                               ** uri : 
                               ** datatype : DOUBLELIST
                               ** unit : m2 leaf m-2 ground
                               ** description : List of daily Green Area Index in the window dedicated to average
                 * name: calendarCumuls
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** unit : °C d
                               ** description :  list containing for each stage occured its cumulated thermal times
                 * name: gAImean
                               ** min : 0.0
                               ** variablecategory : state
                               ** max : 500.0
                               ** uri : 
                               ** datatype : DOUBLE
                               ** unit : m2 leaf m-2 ground
                               ** description : Mean Green Area Index
                 * name: pastMaxAI
                               ** min : 0.0
                               ** variablecategory : state
                               ** max : 5000.0
                               ** uri : 
                               ** datatype : DOUBLE
                               ** unit : m2 leaf m-2 ground
                               ** description : Maximum Leaf Area Index reached the current day
    """

    leafTillerNumberArray = []
    tilleringProfile = []
    listTTShootWindowForPTQ1 = []
    listGAITTWindowForPTQ = []
    listPARTTWindowForPTQ = []
    listTTShootWindowForPTQ = []
    calendarMoments = []
    calendarDates = []
    calendarCumuls = []
    fixPhyll = model_phylsowingdatecorrection(sowingDay, latitude, sDsa_sh, rp, sDws, sDsa_nh, p)
    (cumulTTFromZC_65, cumulTTFromZC_39, cumulTTFromZC_91) = model_cumulttfrom(calendarMoments_t1, calendarCumuls_t1, cumulTT)
    (vernaprog, minFinalNumber, calendarMoments, calendarDates, calendarCumuls) = model_vernalizationprogress(dayLength, deltaTT, cumulTT, leafNumber_t1, calendarMoments_t1, calendarDates_t1, calendarCumuls_t1, minTvern, intTvern, vAI, vBEE, minDL, maxDL, maxTvern, pNini, aMXLFNO, vernaprog_t1, currentdate, isVernalizable, minFinalNumber_t1)
    isMomentRegistredZC_39 = model_ismomentregistredzc_39(calendarMoments_t1)
    (finalLeafNumber, phase, hasLastPrimordiumAppeared) = model_updatephase(cumulTT, leafNumber_t1, cumulTTFromZC_39, isMomentRegistredZC_39, gAI, grainCumulTT, dayLength, vernaprog, minFinalNumber, fixPhyll, isVernalizable, dse, pFLLAnth, dcd, dgf, degfm, maxDL, sLDL, ignoreGrainMaturation, pHEADANTH, choosePhyllUse, p, phase_t1, cumulTTFromZC_91, phyllochron, hasLastPrimordiumAppeared_t1, finalLeafNumber_t1)
    leafNumber = model_leafnumber(deltaTT, phyllochron_t1, hasFlagLeafLiguleAppeared, leafNumber_t1, phase)
    (hasFlagLeafLiguleAppeared, calendarMoments, calendarDates, calendarCumuls) = model_updateleafflag(cumulTT, leafNumber, calendarMoments, calendarDates, calendarCumuls, currentdate, finalLeafNumber, hasFlagLeafLiguleAppeared_t1, phase)
    (hasZadokStageChanged, currentZadokStage, calendarMoments, calendarDates, calendarCumuls) = model_registerzadok(cumulTT, phase, leafNumber, calendarMoments, calendarDates, calendarCumuls, cumulTTFromZC_65, currentdate, der, slopeTSFLN, intTSFLN, finalLeafNumber, currentZadokStage, hasZadokStageChanged_t1, sowingDate)
    (calendarMoments, calendarDates, calendarCumuls) = model_updatecalendar(cumulTT, calendarMoments, calendarDates, calendarCumuls, currentdate, phase)
    (averageShootNumberPerPlant, canopyShootNumber, leafTillerNumberArray, tilleringProfile, numberTillerCohort) = model_shootnumber(canopyShootNumber_t1, leafNumber, sowingDensity, targetFertileShoot, tilleringProfile_t1, leafTillerNumberArray_t1, numberTillerCohort_t1)
    (gAImean, pastMaxAI, listTTShootWindowForPTQ1, listGAITTWindowForPTQ) = model_gaimean(gAI, tTWindowForPTQ, deltaTT, pastMaxAI_t1, listTTShootWindowForPTQ1_t1, listGAITTWindowForPTQ_t1)
    (listPARTTWindowForPTQ, listTTShootWindowForPTQ, ptq) = model_ptq(tTWindowForPTQ, kl, listTTShootWindowForPTQ_t1, listPARTTWindowForPTQ_t1, listGAITTWindowForPTQ, pAR, deltaTT)
    phyllochron = model_phyllochron(fixPhyll, leafNumber, lincr, ldecr, pdecr, pincr, ptq, gAImean, kl, pTQhf, B, p, choosePhyllUse, areaSL, areaSS, lARmin, lARmax, sowingDensity, lNeff)
    return (currentZadokStage, hasZadokStageChanged, hasFlagLeafLiguleAppeared, listPARTTWindowForPTQ, hasLastPrimordiumAppeared, listTTShootWindowForPTQ, listTTShootWindowForPTQ1, ptq, calendarMoments, canopyShootNumber, calendarDates, leafTillerNumberArray, vernaprog, phyllochron, leafNumber, numberTillerCohort, tilleringProfile, averageShootNumberPerPlant, minFinalNumber, finalLeafNumber, phase, listGAITTWindowForPTQ, calendarCumuls, gAImean, pastMaxAI)

def init_phenology(aMXLFNO = 24.0,
         currentdate = datetime(2007, 3, 27),
         cumulTT = 112.33011041,
         pNini = 4.0,
         sDsa_sh = 1.0,
         latitude = 0.0,
         kl = 0.45,
         lincr = 8.0,
         ldecr = 0.0,
         pincr = 1.5,
         pTQhf = 0.0,
         B = 20.0,
         areaSL = 0.0,
         areaSS = 0.0,
         lARmin = 0.0,
         sowingDensity = 0.0,
         lARmax = 0.0,
         lNeff = 0.0,
         rp = 0.0,
         p = 120.0,
         pdecr = 0.4,
         maxTvern = 23.0,
         dayLength = 12.3037621834,
         deltaTT = 0.0,
         tTWindowForPTQ = 0.0,
         gAI = 0.0,
         pAR = 0.0,
         vBEE = 0.01,
         isVernalizable = 1,
         minTvern = 0.0,
         intTvern = 11.0,
         vAI = 0.015,
         maxDL = 15.0,
         choosePhyllUse = "Default",
         minDL = 8.0,
         pFLLAnth = 2.22,
         dcd = 100.0,
         dgf = 450.0,
         degfm = 0.0,
         ignoreGrainMaturation = False,
         pHEADANTH = 1.0,
         sLDL = 0.85,
         grainCumulTT = 0.0,
         sowingDay = 1,
         sowingDate = datetime(2007, 3, 21),
         sDws = 1,
         sDsa_nh = 1.0,
         der = 300.0,
         targetFertileShoot = 600.0,
         dse = 105.0,
         slopeTSFLN = 0.9,
         intTSFLN = 0.9):
    currentZadokStage = ''
    hasZadokStageChanged = 0
    hasFlagLeafLiguleAppeared = 0
    listPARTTWindowForPTQ = []
    hasLastPrimordiumAppeared = 0
    listTTShootWindowForPTQ = []
    listTTShootWindowForPTQ1 = []
    ptq = 0.0
    calendarMoments = []
    canopyShootNumber = 0.0
    calendarDates = []
    leafTillerNumberArray = []
    vernaprog = 0.0
    phyllochron = 0.0
    leafNumber = 0.0
    numberTillerCohort = 0
    tilleringProfile = []
    averageShootNumberPerPlant = 0.0
    minFinalNumber = 0.0
    finalLeafNumber = 0.0
    phase = 0.0
    listGAITTWindowForPTQ = []
    calendarCumuls = []
    gAImean = 0.0
    pastMaxAI = 0.0
    calendarMoments.append("Sowing")
    calendarCumuls.append(0.0)
    calendarDates.append(sowingDate)
    minFinalNumber = 5.5
    return (currentZadokStage, hasZadokStageChanged, hasFlagLeafLiguleAppeared, listPARTTWindowForPTQ, hasLastPrimordiumAppeared, listTTShootWindowForPTQ, listTTShootWindowForPTQ1, ptq, calendarMoments, canopyShootNumber, calendarDates, leafTillerNumberArray, vernaprog, phyllochron, leafNumber, numberTillerCohort, tilleringProfile, averageShootNumberPerPlant, minFinalNumber, finalLeafNumber, phase, listGAITTWindowForPTQ, calendarCumuls, gAImean, pastMaxAI)