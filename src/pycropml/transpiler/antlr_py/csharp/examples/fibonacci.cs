using System;
namespace LogicalPrograms
{
    using System.Math;
    public class Program
    {
        /*static void Main(string[] args)
        {
            Console.Write("Please enter the Nth number of the Fibonacci Series : ");
            int NthNumber = int.Parse(Console.ReadLine());
            Decrement the Nth Number by 1. This is because the series starts with 0
            NthNumber = NthNumber - 1;
            Console.Write(NthFibonacciNumber(NthNumber));
            Console.ReadKey();
        }*/
        private static int NthFibonacciNumber(int number)
        {
            //List<int[]> hh = new List<int[]>{5, 5};
            int[] array3;
            //Console.Write($"Please enter the Nth number of the Fibonacci Series : {number} ");
            array3 = new int[] { 1, 3, 5, 7, 9 };
            int firstNumber = 0;
            int secondNumber = 1; 
            int nextNumber = 0;
            // To return the first Fibonacci number  
            if (number == 0)
                return firstNumber;
            for (int i = 2; i < number; i+=1) // i++
            {
                int papa = 5;
                nextNumber = firstNumber + secondNumber;
                firstNumber = secondNumber;
                secondNumber = nextNumber;
            }
            return secondNumber;
        }
    }
}