static void Main(string[] args)
        {
            Console.Write("Enter your last name: ");
            string lName = Console.ReadLine();
            char[] letters = new char[lName.Length];

            for (int i = 0; i < lName.Length; i++)
            {
                letters[i] = lName[i];
            }

            Console.Write("Stored letters of last name: ");
            foreach (char letter in letters)
            {
                Console.Write(letter + " ");
            }
            Console.WriteLine();

            Console.Write("Enter first letter of your last name: ");
            string fLetter = Console.ReadLine();

            for (int i = 0; i < letters.Length; i++)
            {
                if (letters[i] == fLetter[0])
                {
                    Console.WriteLine("Found at Index " + i);
                    break;
                }
            }

            Console.ReadLine();
        }