using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp10
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Dustin Drix M. Narciso      BSCS 2B
            
            string[] list = new string[25]
            {
                "00", "01", "02", "03", "04",
                "10", "11", "12", "13", "14",
                "20", "21", "22", "23", "24",
                "30", "31", "32", "33", "34",
                "40", "41", "42", "43", "44",
            };

            Console.Write("Enter Something: ");
            string input = Console.ReadLine().ToUpper();
            string output = "";
             
            foreach (char x in input)
            {
                if (x == ' ')
                    output += " ";
                else if (x >= 'A' && x <= 'Y')
                    output += list[x - 'A'];
            }
     
            Console.WriteLine("Output: " + output);
            
            Console.ReadLine();
        }

    }
}
