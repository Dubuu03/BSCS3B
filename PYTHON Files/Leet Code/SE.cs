using System;

namespace MaintainabilityExample
{
    class Program
    {
        static void Main()
        {
            int score = 85;
            string grade = DetermineLetterGrade(score);

            Console.WriteLine("Letter Grade: " + grade);
       }
        static string DetermineLetterGrade(int score)
        {
            if (score >= 90)
            {
                return "A";
            }
            else if (score >= 80)
            {
                return "B";
            }
            else if (score >= 70)
            {
                return "C";
            }
            else if (score >= 60)
            {
                return "D";
            }
            else
            {
                return "F";
            }
        }
    }
}