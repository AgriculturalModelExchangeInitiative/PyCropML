public class Energybalance
{
    
    public Energybalance()
    {
           
    }

    Netradiation _Netradiation = new Netradiation();
    Netradiationequivalentevaporation _Netradiationequivalentevaporation = new Netradiationequivalentevaporation();
    Priestlytaylor _Priestlytaylor = new Priestlytaylor();
    Conductance _Conductance = new Conductance();
    Diffusionlimitedevaporation _Diffusionlimitedevaporation = new Diffusionlimitedevaporation();
    Penman _Penman = new Penman();
    Ptsoil _Ptsoil = new Ptsoil();
    Soilevaporation _Soilevaporation = new Soilevaporation();
    Evapotranspiration _Evapotranspiration = new Evapotranspiration();
    Soilheatflux _Soilheatflux = new Soilheatflux();
    Potentialtranspiration _Potentialtranspiration = new Potentialtranspiration();
    Cropheatflux _Cropheatflux = new Cropheatflux();
    Canopytemperature _Canopytemperature = new Canopytemperature();

    public double getalbedoCoefficient()
    {
        return _Netradiation.getalbedoCoefficient();
    }
    public void setalbedoCoefficient(double albedoCoefficient)
    {
        _Netradiation.setalbedoCoefficient(albedoCoefficient);
    } 

    public double getstefanBoltzman()
    {
        return _Netradiation.getstefanBoltzman();
    }
    public void setstefanBoltzman(double stefanBoltzman)
    {
        _Netradiation.setstefanBoltzman(stefanBoltzman);
    } 

    public double getelevation()
    {
        return _Netradiation.getelevation();
    }
    public void setelevation(double elevation)
    {
        _Netradiation.setelevation(elevation);
    } 

    public double getlambdaV()
    {
        return _Netradiationequivalentevaporation.getlambdaV();
    }
    public void setlambdaV(double lambdaV)
    {
        _Netradiationequivalentevaporation.setlambdaV(lambdaV);
        _Penman.setlambdaV(lambdaV);
        _Canopytemperature.setlambdaV(lambdaV);
    } 

    public double getpsychrometricConstant()
    {
        return _Priestlytaylor.getpsychrometricConstant();
    }
    public void setpsychrometricConstant(double psychrometricConstant)
    {
        _Priestlytaylor.setpsychrometricConstant(psychrometricConstant);
        _Penman.setpsychrometricConstant(psychrometricConstant);
    } 

    public double getAlpha()
    {
        return _Priestlytaylor.getAlpha();
    }
    public void setAlpha(double Alpha)
    {
        _Priestlytaylor.setAlpha(Alpha);
        _Penman.setAlpha(Alpha);
        _Ptsoil.setAlpha(Alpha);
    } 

    public double getvonKarman()
    {
        return _Conductance.getvonKarman();
    }
    public void setvonKarman(double vonKarman)
    {
        _Conductance.setvonKarman(vonKarman);
    } 

    public double getheightWeatherMeasurements()
    {
        return _Conductance.getheightWeatherMeasurements();
    }
    public void setheightWeatherMeasurements(double heightWeatherMeasurements)
    {
        _Conductance.setheightWeatherMeasurements(heightWeatherMeasurements);
    } 

    public double getzm()
    {
        return _Conductance.getzm();
    }
    public void setzm(double zm)
    {
        _Conductance.setzm(zm);
    } 

    public double getd()
    {
        return _Conductance.getd();
    }
    public void setd(double d)
    {
        _Conductance.setd(d);
    } 

    public double getzh()
    {
        return _Conductance.getzh();
    }
    public void setzh(double zh)
    {
        _Conductance.setzh(zh);
    } 

    public double getsoilDiffusionConstant()
    {
        return _Diffusionlimitedevaporation.getsoilDiffusionConstant();
    }
    public void setsoilDiffusionConstant(double soilDiffusionConstant)
    {
        _Diffusionlimitedevaporation.setsoilDiffusionConstant(soilDiffusionConstant);
    } 

    public double getrhoDensityAir()
    {
        return _Penman.getrhoDensityAir();
    }
    public void setrhoDensityAir(double rhoDensityAir)
    {
        _Penman.setrhoDensityAir(rhoDensityAir);
        _Canopytemperature.setrhoDensityAir(rhoDensityAir);
    } 

    public double getspecificHeatCapacityAir()
    {
        return _Penman.getspecificHeatCapacityAir();
    }
    public void setspecificHeatCapacityAir(double specificHeatCapacityAir)
    {
        _Penman.setspecificHeatCapacityAir(specificHeatCapacityAir);
        _Canopytemperature.setspecificHeatCapacityAir(specificHeatCapacityAir);
    } 

    public double gettau()
    {
        return _Ptsoil.gettau();
    }
    public void settau(double tau)
    {
        _Ptsoil.settau(tau);
        _Soilheatflux.settau(tau);
        _Potentialtranspiration.settau(tau);
    } 

    public double gettauAlpha()
    {
        return _Ptsoil.gettauAlpha();
    }
    public void settauAlpha(double tauAlpha)
    {
        _Ptsoil.settauAlpha(tauAlpha);
    } 

    public int getisWindVpDefined()
    {
        return _Evapotranspiration.getisWindVpDefined();
    }
    public void setisWindVpDefined(int isWindVpDefined)
    {
        _Evapotranspiration.setisWindVpDefined(isWindVpDefined);
    } 
    public void  Calculate_energybalance(EnergybalanceState s, EnergybalanceRate r, EnergybalanceAuxiliary a)
    {
        _Diffusionlimitedevaporation.Calculate_diffusionlimitedevaporation(s, r, a);
        _Conductance.Calculate_conductance(s, r, a);
        _Netradiation.Calculate_netradiation(s, r, a);
        _Netradiationequivalentevaporation.Calculate_netradiationequivalentevaporation(s, r, a);
        _Priestlytaylor.Calculate_priestlytaylor(s, r, a);
        _Penman.Calculate_penman(s, r, a);
        _Evapotranspiration.Calculate_evapotranspiration(s, r, a);
        _Potentialtranspiration.Calculate_potentialtranspiration(s, r, a);
        _Ptsoil.Calculate_ptsoil(s, r, a);
        _Soilevaporation.Calculate_soilevaporation(s, r, a);
        _Soilheatflux.Calculate_soilheatflux(s, r, a);
        _Cropheatflux.Calculate_cropheatflux(s, r, a);
        _Canopytemperature.Calculate_canopytemperature(s, r, a);
    }
    private double albedoCoefficient;
    private double stefanBoltzman;
    private double elevation;
    private double lambdaV;
    private double psychrometricConstant;
    private double Alpha;
    private double vonKarman;
    private double heightWeatherMeasurements;
    private double zm;
    private double d;
    private double zh;
    private double soilDiffusionConstant;
    private double rhoDensityAir;
    private double specificHeatCapacityAir;
    private double tau;
    private double tauAlpha;
    private int isWindVpDefined;
    public Energybalance(Energybalance toCopy) // copy constructor 
    {
        this.albedoCoefficient = toCopy.getalbedoCoefficient();
        this.stefanBoltzman = toCopy.getstefanBoltzman();
        this.elevation = toCopy.getelevation();
        this.lambdaV = toCopy.getlambdaV();
        this.psychrometricConstant = toCopy.getpsychrometricConstant();
        this.Alpha = toCopy.getAlpha();
        this.vonKarman = toCopy.getvonKarman();
        this.heightWeatherMeasurements = toCopy.getheightWeatherMeasurements();
        this.zm = toCopy.getzm();
        this.d = toCopy.getd();
        this.zh = toCopy.getzh();
        this.soilDiffusionConstant = toCopy.getsoilDiffusionConstant();
        this.rhoDensityAir = toCopy.getrhoDensityAir();
        this.specificHeatCapacityAir = toCopy.getspecificHeatCapacityAir();
        this.tau = toCopy.gettau();
        this.tauAlpha = toCopy.gettauAlpha();
        this.isWindVpDefined = toCopy.getisWindVpDefined();

    }
}