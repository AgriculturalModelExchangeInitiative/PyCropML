# coding: utf8
from pycropml.units import u
from copy import copy
from array import array

import numpy
from math import *

def model_ptq(tTWindowForPTQ = 70.0,
         kl = 0.45,
         listTTShootWindowForPTQ_t1 = [0.0],
         listPARTTWindowForPTQ_t1 = [0.0],
         listGAITTWindowForPTQ = [0.0, 5.2],
         pAR = 0.0,
         deltaTT = 0.0):
    """
     - Name: PTQ -Version: 1.0, -Time step: 1
     - Description:
                 * Title: Phyllochron Model
                 * Author: Pierre Martre
                 * Reference: Modeling development phase in the 
                     Wheat Simulation Model SiriusQuality.
                     See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
                 * Institution: INRA Montpellier
                 * Abstract: Calculate Photothermal Quaotient 
     - inputs:
                 * name: tTWindowForPTQ
                               ** description : Thermal time window in which averages are computed
                               ** parametercategory : species
                               ** datatype : DOUBLE
                               ** min : 0.0
                               ** max : 70000.0
                               ** default : 70.0
                               ** unit : °C d
                               ** uri : some url
                               ** inputtype : parameter
                 * name: kl
                               ** description : Exctinction Coefficient
                               ** parametercategory : species
                               ** datatype : DOUBLE
                               ** min : 0.0
                               ** max : 50.0
                               ** default : 0.45
                               ** unit : 
                               ** uri : some url
                               ** inputtype : parameter
                 * name: listTTShootWindowForPTQ_t1
                               ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** min : 
                               ** max : 
                               ** default : [0.0]
                               ** unit : °C d
                               ** uri : some url
                               ** inputtype : variable
                 * name: listPARTTWindowForPTQ_t1
                               ** description : List of Daily PAR during TTWindowForPTQ thermal time period
                               ** variablecategory : state
                               ** inputtype : variable
                               ** datatype : DOUBLELIST
                               ** min : 
                               ** max : 
                               ** default : [0.0]
                               ** unit : MJ m2 d
                               ** uri : some url
                 * name: listGAITTWindowForPTQ
                               ** description : List of daily GAI over TTWindowForPTQ thermal time period
                               ** variablecategory : state
                               ** inputtype : variable
                               ** datatype : DOUBLELIST
                               ** min : 
                               ** max : 
                               ** default : [0.0, 5.2]
                               ** unit : m2 m-2
                               ** uri : some url
                 * name: pAR
                               ** description : Daily Photosyntetically Active Radiation
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** min : 0.0
                               ** max : 10000.0
                               ** unit : MJ m² d
                               ** uri : some url
                               ** inputtype : variable
                 * name: deltaTT
                               ** description : daily delta TT 
                               ** variablecategory : auxiliary
                               ** inputtype : variable
                               ** datatype : DOUBLE
                               ** min : 0.0
                               ** max : 100.0
                               ** default : 0.0
                               ** unit : °C d
                               ** uri : some url
     - outputs:
                 * name: listPARTTWindowForPTQ
                               ** description :  List of Daily PAR during TTWindowForPTQ thermal time period
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** min : 
                               ** max : 
                               ** unit : MJ m2 d
                 * name: listTTShootWindowForPTQ
                               ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** min : 
                               ** max : 
                               ** unit : °C d
                 * name: ptq
                               ** description : Photothermal Quotient
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** unit : MJ °C-1 d m-2)
    """

    listPARTTWindowForPTQ = []
    listTTShootWindowForPTQ = []
    TTList = []
    PARList = []
    parInt = 0.0
    for i in range(0 , len(listTTShootWindowForPTQ_t1) , 1):
        TTList.append(listTTShootWindowForPTQ_t1[i])
        PARList.append(listPARTTWindowForPTQ_t1[i])
    TTList.append(deltaTT)
    PARList.append(pAR)
    SumTT = sum(TTList)
    count = 0
    while SumTT > tTWindowForPTQ:
        SumTT = SumTT - TTList[count]
        count = count + 1
    for i in range(count , len(TTList) , 1):
        listTTShootWindowForPTQ.append(TTList[i])
        listPARTTWindowForPTQ.append(PARList[i])
    for i in range(0 , len(listTTShootWindowForPTQ) , 1):
        parInt = parInt + (listPARTTWindowForPTQ[i] * (1 - exp(-kl * listGAITTWindowForPTQ[i])))
    TTShoot = sum(listTTShootWindowForPTQ)
    ptq = parInt / TTShoot
    return (listPARTTWindowForPTQ, listTTShootWindowForPTQ, ptq)