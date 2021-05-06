
using System;
public class Test
{

    public static int sum_(int[] x)
    {
        int i;
        int y = 0;
        foreach(int i_cyml in x)
        {
            i = i_cyml;
            y = y + i;
        }
        return y;
    }   
    public static void Main()
    {
        int[] v ={15,20,13};
        // Display the number of command line arguments.
        Console.WriteLine(sum_(v));
    }
}
int[] v ={15,20,13};
Console.WriteLine(Test.sum_(v));