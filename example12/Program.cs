class Programm
{
    static void Main()
    {
        Random random = new Random();
        int[] arr = new int[6];
        for (int i = 0; i < arr.Length; i++)
        {
            arr[i] = random.Next(1, 10);
            Console.WriteLine(arr[i]);
        }
        Console.Write("Введите сумму каких элементов хотите сложить: (1,2,3), или (3,4,5) или (4,5,6): ");
        string str = Console.ReadLine();
        int start_1 = 0, end_1 = 3;
        int start_2 = 2, end_2 = 5;
        int start_3 = 3, end_3 = 6;
        int number = Convert.ToInt32(str);
        if (number == 1)
        {
            var slice = arr[start_1..end_1];
            int sum = slice.Sum();
            Console.WriteLine("Сумма первого, второго и третьего элементов:");
            Console.WriteLine(sum);
        }
        else if (number == 2)
        {
            var slice = arr[start_2..end_2];
            int sum = slice.Sum();
            Console.WriteLine("Сумма третьего, четвертого и пятого элементов:");
            Console.WriteLine(sum);
        }
        else if (number == 3)
        {
            var slice = arr[start_3..end_3];
            int sum = slice.Sum();
            Console.WriteLine("Сумма четвертого, пятого и шестого элементов:");
            Console.WriteLine(sum);
        }
        else
        {
            Console.WriteLine("Ошибка, введите корректное значение(1, 2 или 3)");
        }
    }
}