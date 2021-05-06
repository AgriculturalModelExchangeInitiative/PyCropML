# coding: utf8
from pycropml.units import u
from copy import copy
from array import array

import numpy
from math import *

def model_gaimean(gAI = 0.0,
         tTWindowForPTQ = 0.0,
         deltaTT = 0.0,
         pastMaxAI_t1 = 0.0,
         listTTShootWindowForPTQ1_t1 = [0.0],
         listGAITTWindowForPTQ_t1 = [0.0]):
    """
     - Name: GAImean -Version: 1.0, -Time step: 1
     - Description:
                 * Title: Average GAI on a specific thermal time window
                 * Author: Loïc Manceau
                 * Reference: -
                 * Institution: INRA
                 * Abstract: -
     - inputs:
                 * name: gAI
                               ** description : Green Area Index of the day
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** min : 0.0
                               ** max : 500.0
                               ** unit : m2 leaf m-2 ground
                               ** uri : 
                 * name: tTWindowForPTQ
                               ** description : Thermal Time window for average
                               ** inputtype : parameter
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** min : 0.0
                               ** max : 5000.0
                               ** unit : °C d
                               ** uri : 
                 * name: deltaTT
                               ** description : Thermal time increase of the day
                               ** inputtype : variable
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** min : 0.0
                               ** max : 100.0
                               ** unit : °C d
                               ** uri : 
                 * name: pastMaxAI_t1
                               ** description : Maximum Leaf Area Index reached the current day
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** default : 0.0
                               ** min : 0.0
                               ** max : 5000.0
                               ** unit : m2 leaf m-2 ground
                               ** uri : 
                 * name: listTTShootWindowForPTQ1_t1
                               ** description : List of daily shoot thermal time in the window dedicated to average
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** default : [0.0]
                               ** min : 
                               ** max : 
                               ** unit : °C d
                               ** uri : 
                 * name: listGAITTWindowForPTQ_t1
                               ** description : List of daily Green Area Index in the window dedicated to average
                               ** inputtype : variable
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** default : [0.0]
                               ** min : 
                               ** max : 
                               ** unit : m2 leaf m-2 ground
                               ** uri : 
     - outputs:
                 * name: gAImean
                               ** description : Mean Green Area Index
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** min : 0.0
                               ** max : 500.0
                               ** unit : m2 leaf m-2 ground
                               ** uri : 
                 * name: pastMaxAI
                               ** description : Maximum Leaf Area Index reached the current day
                               ** variablecategory : state
                               ** datatype : DOUBLE
                               ** min : 0.0
                               ** max : 5000.0
                               ** unit : m2 leaf m-2 ground
                               ** uri : 
                 * name: listTTShootWindowForPTQ1
                               ** description : List of daily shoot thermal time in the window dedicated to average
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** min : 
                               ** max : 
                               ** unit : °C d
                               ** uri : 
                 * name: listGAITTWindowForPTQ
                               ** description : List of daily Green Area Index in the window dedicated to average
                               ** variablecategory : state
                               ** datatype : DOUBLELIST
                               ** min : 
                               ** max : 
                               ** unit : m2 leaf m-2 ground
                               ** uri : 
    """

    listTTShootWindowForPTQ1 = []
    listGAITTWindowForPTQ = []
    TTList = []
    GAIList = []
    count = 0
    gai_ = 0.0
    gaiMean_ = 0.0
    countGaiMean = 0
    for i in range(0 , len(listTTShootWindowForPTQ1_t1) , 1):
        TTList.append(listTTShootWindowForPTQ1_t1[i])
        GAIList.append(listGAITTWindowForPTQ_t1[i])
    TTList.append(deltaTT)
    GAIList.append(gAI)
    SumTT = sum(TTList)
    while SumTT > tTWindowForPTQ:
        SumTT = SumTT - TTList[count]
        count = count + 1
    for i in range(count , len(TTList) , 1):
        listTTShootWindowForPTQ1.append(TTList[i])
        listGAITTWindowForPTQ.append(GAIList[i])
    for i in range(0 , len(listGAITTWindowForPTQ) , 1):
        gaiMean_ = gaiMean_ + listGAITTWindowForPTQ[i]
        countGaiMean = countGaiMean + 1
    gaiMean_ = gaiMean_ / countGaiMean
    gai_ = max(pastMaxAI_t1, gaiMean_)
    pastMaxAI = gai_
    gAImean = gai_
    return (gAImean, pastMaxAI, listTTShootWindowForPTQ1, listGAITTWindowForPTQ)