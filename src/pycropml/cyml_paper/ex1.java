import  java.io.*;
import  java.util.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
public class ex1
{
    public static int sum_(Integer[] x)
    {
        int i;
        int y = 0;
        for(Integer i_cyml : x)
        {
            i = i_cyml;
            y = y + i;
        }
        return y;
    }
    public static void main (String[] args)
    {
        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
        Date toto= new Date();
        try{
            toto = format.parse("2010-10-12");
        } catch (ParseException var4) {
            var4.printStackTrace();
        }
        Calendar c = Calendar.getInstance();  
        c.setTime(toto); 
        System.out.println(c.get(Calendar.YEAR));

    }


}
