    public HashMap<String, FWSimVariable<?>> createVariables()
    {
        addVariable(FWSimVariable.createSimVariable("rhoDensityAir", 
                                                    "Density of air", DATA_TYPE.DOUBLE, 
                                                    CONTENT_TYPE.constant,
                                                    " ", 
                                                    0, 10000, 1.225, this));
        
        //...
        
        return iFieldMap;
    }

