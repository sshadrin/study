class Program
{
    static void Main()
    {
        Random random = new Random();
        double[] array = new double[10];
        int x = 2;
        Console.WriteLine("Наш массив:");
        for (int i = 0; i < array.Length; i++)
        {
            array[i] = Convert.ToDouble(random.Next(-100, 100) / 10.0);
            Console.WriteLine(array[i]);
        }
        Console.WriteLine("Минимальный элемент:" + array.Min());
        Console.WriteLine("Максимальный элемент:" + array.Max());
        Console.WriteLine("Отсортированный массив, согласно заданию:");
        for (int i = 0; i < array.Length; i++)
        {
            if (array[i] >= 0) 
            {
                Console.WriteLine(Math.Round(array[i] * Math.Pow(array.Min(), x), 2));
            } else
            {
                Console.WriteLine(Math.Round(array[i] * Math.Pow(array.Max(), x), 2));
            }
        }
    }   
}