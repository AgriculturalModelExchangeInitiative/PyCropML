# coding: utf8
from copy import copy

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
                               ** min : 0.0
                               ** default : 0.0
                               ** max : 500.0
                               ** uri : 
                               ** variablecategory : auxiliary
                               ** datatype : DOUBLE
                               ** inputtype : variable
                               ** unit : m2 leaf m-2 ground
                               ** description : Green Area Index of the day
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
     - outputs:
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
                 * name: listTTShootWindowForPTQ1
                               ** min : 
                               ** variablecategory : state
                               ** max : 
                               ** uri : 
                               ** datatype : DOUBLELIST
                               ** unit : °C d
                               ** description : List of daily shoot thermal time in the window dedicated to average
                 * name: listGAITTWindowForPTQ
                               ** min : 
                               ** variablecategory : state
                               ** max : 
                               ** uri : 
                               ** datatype : DOUBLELIST
                               ** unit : m2 leaf m-2 ground
                               ** description : List of daily Green Area Index in the window dedicated to average
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