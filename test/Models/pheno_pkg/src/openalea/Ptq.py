# coding: utf8
from copy import copy

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
                               ** parametercategory : species
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 70000.0
                               ** uri : some url
                               ** default : 70.0
                               ** inputtype : parameter
                               ** unit : °C d
                               ** description : Thermal time window in which averages are computed
                 * name: kl
                               ** parametercategory : species
                               ** min : 0.0
                               ** datatype : DOUBLE
                               ** max : 50.0
                               ** uri : some url
                               ** default : 0.45
                               ** inputtype : parameter
                               ** unit : 
                               ** description : Exctinction Coefficient
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
                 * name: listGAITTWindowForPTQ
                               ** min : 
                               ** default : [0.0, 5.2]
                               ** max : 
                               ** uri : some url
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** inputtype : variable
                               ** unit : m2 m-2
                               ** description : List of daily GAI over TTWindowForPTQ thermal time period
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
                 * name: deltaTT
                               ** min : 0.0
                               ** default : 0.0
                               ** max : 100.0
                               ** uri : some url
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : °C d
                               ** description : daily delta TT 
     - outputs:
                 * name: listPARTTWindowForPTQ
                               ** datatype : DOUBLELIST
                               ** min : 
                               ** variablecategory : state
                               ** max : 
                               ** unit : MJ m2 d
                               ** description :  List of Daily PAR during TTWindowForPTQ thermal time period
                 * name: listTTShootWindowForPTQ
                               ** datatype : DOUBLELIST
                               ** min : 
                               ** variablecategory : state
                               ** max : 
                               ** unit : °C d
                               ** description : List of Daily Shoot thermal time during TTWindowForPTQ thermal time period
                 * name: ptq
                               ** datatype : DOUBLE
                               ** min : 0
                               ** variablecategory : state
                               ** max : 10000
                               ** unit : MJ °C-1 d m-2)
                               ** description : Photothermal Quotient
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