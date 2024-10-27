// Dusin Drix M. Narciso   BSCS-2B

internal class Program
{
    static void Main(string[] args)
    {
        int[] arr = { 5, 3, 2, 10, 6 };

        for (int i = arr.Length-2; i >= 0; i--)
        {
            int key = arr[i];
            int x = i+1;

            while (x < arr.Length && arr[x] < key)
            {
                arr[x - 1] = arr[x];
                x++;
                arr[x - 1] = key;
            }
        }

        foreach (var num in arr)
        {
            Console.Write(num + " ");
        }

        Console.ReadKey();
    }
}