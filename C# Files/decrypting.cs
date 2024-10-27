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
            
            Dictionary<char, string> list = new Dictionary<char, string>()
            {
                {'A', "00"}, {'B', "01"}, {'C', "02"}, {'D', "03"}, {'E', "04"},
                {'F', "10"}, {'G', "11"}, {'H', "12"}, {'I', "13"}, {'J', "14"},
                {'K', "20"}, {'L', "21"}, {'M', "22"}, {'N', "23"}, {'O', "24"},
                {'P', "30"}, {'Q', "31"}, {'R', "32"}, {'S', "33"}, {'T', "34"},
                {'U', "40"}, {'V', "41"}, {'W', "42"}, {'X', "43"}, {'Y', "44"}
            };


            Console.Write("Enter Something: ");
            string input = Console.ReadLine().ToUpper();
            string output = "";

            for (int i = 0; i < input.Length; i++)
            {
                if (input[i] == ' ')
                    output += " ";

                char character = input[i];
                if (list.ContainsKey(character))
                {
                    output += list[character];
                }
            }

            Console.WriteLine("Output: " + output);

            Console.ReadLine();
        }

    }
}
