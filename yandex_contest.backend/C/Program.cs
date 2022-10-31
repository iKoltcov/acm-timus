using System;
using System.Linq;

namespace C
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine()?.Split(' ').Select(int.Parse).ToArray();
            var k = input[0];
            var n = input[1];

            var numbers = Console.ReadLine()?.Split(' ').Select(int.Parse).ToArray();

            var vasia = 0;
            var petya = 0;

            foreach (var number in numbers)
            {
                if (number % 5 == 0 && number % 3 != 0)
                {
                    vasia++;
                }

                if (number % 3 == 0 && number % 5 != 0)
                {
                    petya++;
                }

                if (vasia >= k && petya < k)
                {
                    Console.WriteLine("Vasya");
                    return;
                }

                if (petya >= k && vasia < k)
                {
                    Console.WriteLine("Petya");
                    return;
                }

                if (petya == k && vasia == k)
                {
                    Console.WriteLine("Draw");
                    return;
                }
            }

            if (petya == vasia)
            {
                Console.WriteLine("Draw");
            }
            else
            {
                Console.WriteLine( petya > vasia ? "Petya" : "Vasya" );
            }
        }
    }
}