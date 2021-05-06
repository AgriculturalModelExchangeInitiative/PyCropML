using System;

public class Test
{
    public static double test(double b)
    {
        int[] k = {2,2};
        List<int> hh = new List<int>{2, 2};
        //b = test2(10.5d);
        if(b>-10.2d) 
        {
               b=-2.3D;
        }
        while (b<10.3d)
        {
            b = k[1];
        }
        foreach (int element in k)
        {
            b = 2;
        }

        return b;
    }

}
//Console.WriteLine(Test.test(10));