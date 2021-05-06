    
if (phase >= 1.0 and phase< 4.0):       
    if (hasFlagLeafLiguleAppeared==0):            
        if (phyllochron == 0.0):
            phyllochron = 0.0000001
        leafNumber = leafNumber + min(deltaTT / phyllochron, 0.999)

