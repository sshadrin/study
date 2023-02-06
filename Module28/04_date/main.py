class Date:
    """Реализуем класс Date для проверки чисел даты на корректность и конвертирования
     строки даты в объект класса Date, состоящий из соответствующих числовых значений дня, месяца и года."""
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        """Реализуем конструктор со значениями день, месяц, год"""
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        """Вывод результата в заданной форме"""
        return "День: {d}\tМесяц: {m}\tГод: {y}.".format(d=self.day, m=self.month, y=self.year)

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        """Реализуем метод для валидации даты, используем декоратор classmethod"""
        day, month, year = map(int, date.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        """Реализуем метод для конвертирования строки даты в объект класса"""
        day, month, year = map(int, date.split('-'))
        day_object = cls(day, month, year)
        return day_object


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))