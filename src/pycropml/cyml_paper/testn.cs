using System;
using System.Collections.Generic;
using System.Linq;
public class Test
{
    public static List<int> toto(int x, int y)
    {
        Dictionary<string,int>z = new Dictionary<string,int>{{"v", 1},{"h",6},};
        int a;
        int b;
        List<string> j = new List<string>();
        List<int> g = new List<int>();
        a = z.Count;
        b = z["v"];
        
        j = z.Keys.ToList();
        g = z.Values.ToList();
        Console.WriteLine(j[1]+'\n'+a);
        return g;
    }
}
Test.toto(5,4);