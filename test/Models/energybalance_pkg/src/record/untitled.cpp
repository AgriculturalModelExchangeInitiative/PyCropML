// @@tagdynamic@@
// @@tagdepends: vle.discrete-time @@endtagdepends



    Penman(const vd::DynamicsInit& atom, 
           const vd::InitEventList& events) : DiscreteTimeDyn(atom, events)
    {
        // Ces parametres ont une valeur par defaut utilisee si la condition n'est pas definie
        //...
        rhoDensityAir = (events.exist("rhoDensityAir")) ? vv::toDouble(events.get("rhoDensityAir")) : 1.225;
        //...
    }

private:

    //Model parameters
    /**
    * @brief Density of air (kg/m**3)
    */
    double rhoDensityAir;
    //...

    virtual void compute(const vd::Time& /*time*/)
    {
        evapoTranspirationPenman = evapoTranspirationPriestlyTaylor() / Alpha + 
            (1000.0d * (rhoDensityAir * specificHeatCapacityAir * VPDair() 
            * conductance() / (lambdaV * (hslope() + psychrometricConstant))));
    }


