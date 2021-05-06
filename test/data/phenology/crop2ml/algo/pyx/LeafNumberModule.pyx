
cdef float phyllochron_     
if (phase >= 1.0 and phase< 4.0):       
    if (hasFlagLeafLiguleAppeared==0):           
        if (phyllochron == 0.0):
            phyllochron_ = 0.0000001
        else: phyllochron_ = phyllochron
        leafNumber = leafNumber + min(deltaTT / phyllochron_, 0.999)