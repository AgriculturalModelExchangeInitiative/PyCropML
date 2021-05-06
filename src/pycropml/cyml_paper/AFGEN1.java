import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
public class AFGEN1
{
    public static double AFGEN(int n, Double [] xy, double t)
    {
        double x1;
        double x2;
        double y1;
        double y2;
        double res;
        int i;
        res = Double.NaN;
        if (n > 1)
        {
            i = 0;
            while ( i < n - 1 && t >= xy[i])
            {
                i = i + 2;
            }
            if (i == 0)
            {
                res = xy[1];
            }
            else if ( i > n - 2)
            {
                res = xy[i - 1];
            }
            else
            {
                x1 = xy[i - 2];
                x2 = xy[i];
                y1 = xy[i - 1];
                y2 = xy[i + 1];
                res = (y2 - y1) / (x2 - x1) * (t - x1) + y1;
            }
        }
        return res;
    }
    public static void main(String[] args) 
    {
        Double [] y = new Double[]{10.2,52.3,14.6,75.3,36.6,152.5,40.5,160.5,45.5,178.2};
        System.out.println(AFGEN1.AFGEN(10, y,12.2 ));

    }
}