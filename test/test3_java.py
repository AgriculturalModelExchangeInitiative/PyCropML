""" Read xml representation of a component.

"""
from path import Path

from pycropml import pparse
import javalang

# Fix pb in tlocal path
cwd = Path.getcwd()
if (cwd/'data').isdir():
    data = cwd/'data'/'java'
elif (cwd/'test'/'data'/'java').isdir():
    data = cwd/'test'/'data'/'java'
else:
    print('Data directory not found')

xmls = data.glob('*.xml')



##############################################################################
# Test on Example

def java_algorithm():
    return u"""
public class Main {
    public static void foo(boolean firstcall) {
        if (firstcall)
        {
            Double[] Z = cSoilLayerDepth;
            Double firstDayMeanTemp = cFirstDayMeanTemp;
            Double[] _profiledepth = Z[Z.length - 1];
            Double additionalDepth = cDampingDepth - _profiledepth;
            Double firstAdditionalLayerHight = additionalDepth - floor(additionalDepth);
            Integer layers = (int)(abs(ceil(additionalDepth)))+Z.length;
            Double[] SoilTempArray = new Double[layers];
            Double[] tz = new Double[layers];
            for (int i = 0; i < SoilTempArray.length; i++)
            {
                double depth;
                if (i < Z.length)
                    depth = Z[i];
                else //first additional layer might be smaller than 1 m
                    depth = _profiledepth + firstAdditionalLayerHight + i - Z.length;
                tz[i] = depth;
                SoilTempArray[i] = (firstDayMeanTemp * (cDampingDepth - depth) + cAVT * depth) / cDampingDepth; //set linear aproximation to the soil temperature as
                //initial value
            }
            _z = tz;
        }
        double XLAG =.8; //XLAG = LAG = Coefficient for weighting yesterday's soil temperature
        double XLG1 = 1 - XLAG; //XLG1 = Inverse
        //of coefficient for weighting yesterday's soil temperature
        double DP = (1 + 2.5 * cABD / (cABD + exp(6.53 -5.63 * cABD))); //DP= Maximum damping depth (m)
        double WC = 0.001*iSoilWaterContent/((.356 -.144 * cABD) * _profiledepth); //WC seems to be a water content related
        // factor [cm3/g] to modify the damping depth ?
        double DD = exp(log(0.5/DP)*((1 - WC)/(1 + WC)) * 2) * DP;
        // DD(t)= Damping depth (m), multiplied by 2 (20110628 TG) to increase damping depth
        // DD could be also calculated from d = (2Dh /w )^0.5 (easy soilT, Nofziger et al.), where w = 2Pi/365 (d^-1)
        //and Dh is the thermal diffusivity (m^2 s^-l) with ( Dh= K/Cs, Cs = volumetric heat capacity in J m^-3 K^-1, K=??)

        double Z1 = 0; //Z1=Depth of the bottom of the previous soil layer, initialized with 0 (m)
        for (int i = 0; i < SoilTempArray.length; i++)
        {
            double ZD = 0.5*(Z1 + _z[i])/DD;
            //Factor of the depth in soil: Middle of depth of layer divided by damping depth
            double RATE = ZD / (ZD + exp(-.8669 - 2.0775 * ZD)) * (cAVT - iSoilSurfaceTemperature); //RATE = Rate of change of STMP(ISL) (C)
            SoilTempArray[i] = XLAG * SoilTempArray[i] + XLG1 * (RATE + iSoilSurfaceTemperature);
            Z1 = _z[i];
        }
    }
}
    """

def test1():
    code = java_algorithm()
    tree = javalang.parse.parse(code)
    return tree