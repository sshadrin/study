import random

class Student:
    spisok = dict()
    grade = dict()

    def __init__(self, id, name, group_number, a):
        self.id = id
        self.name = name
        self.group_number = group_number
        self.a = []
        for i in range(5):
            self.a.append(random.randint(2, 5))

    def add_spisok(self):
        self.spisok = {self.id: {'Имя': self.name, 'Номер группы': self.group_number, 'Список оценок': self.a}}

    def middle_grade(self):
        sum_grade = sum(self.spisok[self.id]['Список оценок']) / 5
        self.spisok[self.id]['Средний балл'] = float(sum_grade)

    def info(self):
        for i_id, j_info in self.spisok.items():
            print('Студент №:{i}:{j}'.format(i=i_id, j=j_info))


student_1 = Student(1, 'Sergey', 353015, [])
student_1.add_spisok()
student_1.middle_grade()
student_2 = Student(2, 'Alexandr', 353015, [])
student_2.add_spisok()
student_2.middle_grade()
student_1.spisok.update(student_2.spisok)
student_3 = Student(3, 'Anna', 353015, [])
student_3.add_spisok()
student_3.middle_grade()
student_1.spisok.update(student_3.spisok)
student_4 = Student(4, 'Vasiliy', 353015, [])
student_4.add_spisok()
student_4.middle_grade()
student_1.spisok.update(student_4.spisok)
student_5 = Student(5, 'Ivan', 353015, [])
student_5.add_spisok()
student_5.middle_grade()
student_1.spisok.update(student_5.spisok)
student_6 = Student(6, 'Dasha', 353015, [])
student_6.add_spisok()
student_6.middle_grade()
student_1.spisok.update(student_6.spisok)
student_7 = Student(7, 'Petr', 353015, [])
student_7.add_spisok()
student_7.middle_grade()
student_1.spisok.update(student_7.spisok)
student_8 = Student(8, 'Olga', 353015, [])
student_8.add_spisok()
student_8.middle_grade()
student_1.spisok.update(student_8.spisok)
student_9 = Student(9, 'Nikita', 353015, [])
student_9.add_spisok()
student_9.middle_grade()
student_1.spisok.update(student_9.spisok)
student_10 = Student(10, 'Mariya', 353015, [])
student_10.add_spisok()
student_10.middle_grade()
student_1.spisok.update(student_10.spisok)
print('Информация о студентах:')
student_1.info()
print('Информация о студентах по успеваемости:')
spisok = list(student_1.spisok.values())
sort = sorted(spisok, key=lambda x: x['Средний балл'])
for i_grade in enumerate(sort, start=1):
    print(i_grade)
