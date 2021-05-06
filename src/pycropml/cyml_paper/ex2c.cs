using System;
using System.Collections.Generic;
using System.Linq;
public class Test
{
    public static List<int> select(List<int> x)
    {
        List<int> y = new List<int>();
        int e;
        foreach(int e_cyml in x)
        {
            e = e_cyml;
            if (e != 0)
            {
                y.Add(e);
            }
        }
        return y;
    }
}
List<int> v = new List<int>(){15,0,0,14,2,12};
foreach(int i in Test.select(v))
{
Console.WriteLine(i);
}