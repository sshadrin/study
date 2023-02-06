class Humans
{
    public string name;
    public int age;
    public enum social
    {
        student,
        employ
    }

    public void Age_1(int age_1)
    {
        Console.WriteLine("Предполагаемый возраст: " + age_1);
        if (age_1 > age)
        {
            Console.WriteLine("Предполагаемый возраст больше возраста " + name + "на " + (age_1 - age) + " лет!");
        } else if (age_1 == age) {
            Console.WriteLine("Возраст сотрудника и предполагаемый равны!");
        } else
        {
            Console.WriteLine("Возраст " + name + " больше предполагаемого на " + (age - age_1) + " лет!");
        }
    }
    public void ChangeHumans(ref Humans humans, int age_2)
    {
        if (age_2 < age)
        {
            Console.WriteLine("Сотрудник 1 старше!");
        } else if (age_2 == age)
        {
            Console.WriteLine("Сотрудники ровесники!");
        } else
        {
            Console.WriteLine("Сотрудник 2 старше!");
        }
    }
}
class Programm
{
    static void Main(string[] args)
    {
        Humans human = new Humans { name = "Jonny", age = 25 };
        Console.WriteLine("Имя: " + human.name);
        Console.WriteLine("Возраст: " + human.age);
        human.Age_1(25);
        Console.WriteLine("Второй сотрудник:");
        Humans human_1 = new Humans { name = "Jacky", age = 25 };
        Console.WriteLine("Имя: " + human_1.name);
        Console.WriteLine("Возраст: " + human_1.age);
        human.ChangeHumans(ref human, human_1.age);
    }
}