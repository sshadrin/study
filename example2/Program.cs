using System.Text.RegularExpressions;

class Programm
{
    static void Main()
    {
        string new_string = "";  //объявляем строковую переменную, в которую будет считываться весь текст из файла 
        StreamReader reader = new StreamReader("test.txt", System.Text.Encoding.UTF8, true);  //чтение файлов     
        if (reader.EndOfStream != true)  // цикл
        {
            new_string = reader.ReadToEnd();
        }
        Console.WriteLine(new_string);
        string onlyLetters = new string(new_string.Where(char.IsLetter).ToArray());  // считываем все буквы
        Console.WriteLine("Количество букв:" + onlyLetters.Length);  // выводим количество букв
        string numbers = Regex.Replace(new_string, @"\D", "");  // "\D" - символы не цифры заменяем на ""
        Console.WriteLine("Количество цифр:" + numbers.Length);  // выводим количество цифр
        if (onlyLetters.Length > numbers.Length)  // условный оператор, если бкув больше выводим в консоль
        {
            Console.WriteLine("Букв в тексте больше!");
        } else
        {
            Console.WriteLine("Цифр в тексте больше!");
        }
        reader.Close();
        Console.ReadLine();
    }
}