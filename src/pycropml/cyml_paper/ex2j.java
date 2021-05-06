
import  java.util.*;
public class ex2j
{
    public static List<Integer> select(List<Integer> x)
    {
        List<Integer> y = new ArrayList<>(Arrays.asList());
        int e;
        for(Integer e_cyml : x)
        {
            e = e_cyml;
            if (e != 0)
            {
                y.add(e);
            }
        }
        return y;
    }
    public static void main(String[] args) {
        List<Integer>y = new ArrayList <>(Arrays.asList(14, 25,0,0,1,0,5,10));
        for(Integer e_cyml : select(y))
        {
            System.out.println(e_cyml);
        }
    }

}
