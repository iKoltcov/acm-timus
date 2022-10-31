using System;
using System.Collections.Generic;
using System.Linq;

namespace B
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var firstLine = Console.ReadLine()?.Split(' ')
                .Select(int.Parse)
                .ToArray();

            var n = firstLine[0];
            var x = firstLine[1];
            var k = firstLine[2];
            var clocks = Console.ReadLine()?.Split(' ')
                .Select(int.Parse)
                .OrderBy(y => y)
                .ToArray();

            var current = new HashSet<int>(clocks);
            var i = 0;
            while (true)
            {
                i++;
                current.UnionWith(clocks.Select(y => y + x * i).ToArray());

                if (current.Count >= k)
                {
                    break;
                }
            }

            Console.WriteLine(current.Skip(k - 1).First());
        }
    }
}