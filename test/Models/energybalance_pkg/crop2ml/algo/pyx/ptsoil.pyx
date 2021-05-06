cdef float AlphaE
if (tau < tauAlpha):
    AlphaE = 1.0
    
else :
        
    AlphaE = Alpha - ((Alpha - 1.0) * (1.0 - tau) / (1.0 - tauAlpha))
    
energyLimitedEvaporation= (evapoTranspirationPriestlyTaylor / Alpha) * AlphaE * tau

