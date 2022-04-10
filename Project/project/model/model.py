import mysql.connector


class Facultet:
    def __init__(self, name=None, dekan_name=None, room_number=0, korpus_number=0, phone=0):
        self.name = name
        self.dekan_name = dekan_name
        self.room_number = room_number
        self.korpus_number = korpus_number
        self.phone = phone

    @property
    def info(self):
        return f'{self.name} | {self.dekan_name} | {self.room_number} | {self.korpus_number} | {self.phone}'

    @staticmethod
    def getmethod():
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        result = []
        for row in c.execute('select * from Facultet'):
            facultet = Facultet(row[0], row[1], row[2], row[3], row[4])
            result.append(facultet)
        c.close()
        conn.close()
        return result

    @staticmethod
    def addmethod(name, dekan_name, room_number, korpus_number, phone):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('INSERT into facultet values(%s, %s, %s, %s)',
                  (name, dekan_name, int(room_number), int(korpus_number), int(phone)))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def updatemethod(name, dekan_name, room_number, korpus_number, phone):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('UPDATE into facultet values(%s, %s, %s, %s)',
                  (name, dekan_name, int(room_number), int(korpus_number), int(phone)))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def deletemethod(name, dekan_name, room_number, korpus_number, phone):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('DELETE into facultet values(%s, %s, %s, %s)',
                  (name, dekan_name, int(room_number), int(korpus_number), int(phone)))
        conn.commit()
        c.close()
        conn.close()


class Kafedra:
    def __init__(self, name=None, boss_name=None, room_number=0, korpus_number=0, phone=0, teacher_number=0):
        self.name = name
        self.boss_name = boss_name
        self.room_number = room_number
        self.korpus_number = korpus_number
        self.phone = phone
        self.teacher_number = teacher_number

    @property
    def info(self):
        return f'{self.name} | {self.boss_name} | {self.room_number} | {self.korpus_number} | {self.phone} | ' \
               f'{self.teacher_number}'

    @staticmethod
    def getmethod():
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        result = []
        for row in c.execute('select * from Kafedra'):
            kafedra = Kafedra(row[0], row[1], row[2], row[3], row[4], row[5])
            result.append(kafedra)
        c.close()
        conn.close()
        return result

    @staticmethod
    def addmethod(name, boss_name, room_number, korpus_number, phone, teacher_number):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('INSERT into kafedra values(%s, %s, %s, %s)',
                  (name, boss_name, int(room_number), int(korpus_number), int(phone), int(teacher_number)))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def updatemethod(name, boss_name, room_number, korpus_number, phone, teacher_number):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('UPDATE into kafedra values(%s, %s, %s, %s)',
                  (name, boss_name, int(room_number), int(korpus_number), int(phone), int(teacher_number)))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def deletemethod(name, boss_name, room_number, korpus_number, phone, teacher_number):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('DELETE into kafedra values(%s, %s, %s, %s)',
                  (name, boss_name, int(room_number), int(korpus_number), int(phone), int(teacher_number)))
        conn.commit()
        c.close()
        conn.close()


class Teacher:
    def __init__(self, name_teacher=None, birth_year=0, kafedra=Kafedra, when_work_year=0, stashz=0, dolshznost=None,
                 sex=None, city=None):
        self.name_teacher = name_teacher
        self.birth_year = birth_year
        self.kafedra = Kafedra
        self.when_work_year = when_work_year
        self.stashz = stashz
        self.dolshznost = dolshznost
        self.sex = sex
        self.city = city

    @property
    def info(self):
        return f'{self.name_teacher} | {self.birth_year} | {self.kafedra} | {self.when_work_year} | {self.stashz} | ' \
               f'{self.dolshznost, self.sex, self.city}'

    @staticmethod
    def getmethod():
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        result = []
        for row in c.execute('select * from Teacher'):
            teacher = Teacher(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            result.append(teacher)
        c.close()
        conn.close()
        return result

    @staticmethod
    def addmethod(name_teacher, birth_year, Kafedra, when_work_year, stashz, dolshznost, sex, city):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('INSERT into teacher values(%s, %s, %s, %s)',
                  (name_teacher, int(birth_year), Kafedra, int(when_work_year), int(stashz), dolshznost, sex, city))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def updatemethod(name_teacher, birth_year, Kafedra, when_work_year, stashz, dolshznost, sex, city):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('UPDATE into teacher values(%s, %s, %s, %s)',
                  (name_teacher, int(birth_year), Kafedra, int(when_work_year), int(stashz), dolshznost, sex, city))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def deletemethod(name_teacher, birth_year, Kafedra, when_work_year, stashz, dolshznost, sex, city):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('DELETE into teacher values(%s, %s, %s, %s)',
                  (name_teacher, int(birth_year), Kafedra, int(when_work_year), int(stashz), dolshznost, sex, city))
        conn.commit()
        c.close()
        conn.close()


class Discipline:
    def __init__(self, name_discipline=None, hours=0, loop_discipline=None):
        self.name_discipline = name_discipline
        self.hours = hours
        self.loop_discipline = loop_discipline

    @property
    def info(self):
        return f'{self.name_discipline} | {self.hours} | {self.loop_discipline}'

    @staticmethod
    def getmethod():
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        result = []
        for row in c.execute('select * from Discipline'):
            discipline = Discipline(row[0], row[1], row[2])
            result.append(discipline)
        c.close()
        conn.close()
        return result

    @staticmethod
    def addmethod(name_discipline, hours, loop_discipline):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('INSERT into discipline values(%s, %s, %s, %s)',
                  (name_discipline, int(hours), loop_discipline))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def updatemethod(name_discipline, hours, loop_discipline):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('UPDATE into discipline values(%s, %s, %s, %s)',
                  (name_discipline, int(hours), loop_discipline))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def deletemethod(name_discipline, hours, loop_discipline):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('DELETE into discipline values(%s, %s, %s, %s)',
                  (name_discipline, int(hours), loop_discipline))
        conn.commit()
        c.close()
        conn.close()


class AcademicLoad:
    def __init__(self, teacher=Teacher, discipline=Discipline, academic_load=0, semestr=0, groups=0, students=0,
                 control=None):
        self.teacher = Teacher
        self.discipline = Discipline
        self.academic_load = academic_load
        self.semestr = semestr
        self.groups = groups
        self.students = students
        self.control = control

    @property
    def info(self):
        return f'{self.teacher} | {self.discipline} | {self.academic_load} | {self.semestr} | {self.groups} | ' \
               f'{self.students, self.control}'

    @staticmethod
    def getmethod():
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        result = []
        for row in c.execute('select * from AcademicLoad'):
            academicLoad = AcademicLoad(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            result.append(academicLoad)
        c.close()
        conn.close()
        return result

    @staticmethod
    def addmethod(Teacher, Discipline, academic_load, semestr, groups, students, control):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('INSERT into academicLoad values(%s, %s, %s, %s)',
                  (Teacher, Discipline, int(academic_load), int(semestr), int(groups), int(students), control))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def updatemethod(Teacher, Discipline, academic_load, semestr, groups, students, control):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('UPDATE into academicLoad values(%s, %s, %s, %s)',
                  (Teacher, Discipline, int(academic_load), int(semestr), int(groups), int(students), control))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def deletemethod(Teacher, Discipline, academic_load, semestr, groups, students, control):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('DELETE into academicLoad values(%s, %s, %s, %s)',
                  (Teacher, Discipline, int(academic_load), int(semestr), int(groups), int(students), control))
        conn.commit()
        c.close()
        conn.close()


class Account:
    def __init__(self, account_name=None, password=None):
        self.account_name = account_name
        self.password = password

    @property
    def info(self):
        return f'{self.account_name} | {self.password}'

    @staticmethod
    def getmethod():
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        result = []
        for row in c.execute('select * from Account'):
            account = Account(row[0], row[1])
            result.append(account)
        c.close()
        conn.close()
        return result

    @staticmethod
    def addmethod(account_name, password):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('INSERT into account values(%s, %s, %s, %s)',
                  (account_name, password))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def updatemethod(account_name, password):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('UPDATE into account values(%s, %s, %s, %s)',
                  (account_name, password))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def deletemethod(account_name, password):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('DELETE into account values(%s, %s, %s, %s)',
                  (account_name, password))
        conn.commit()
        c.close()
        conn.close()


class Autenfication:
    def __init__(self, account_name=None, password=None):
        self.account_name = account_name
        self.password = password

    @property
    def info(self):
        return f'{self.account_name} | {self.password}'

    @staticmethod
    def getmethod():
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        result = []
        for row in c.execute('select * from Autenfication'):
            autenfication = Autenfication(row[0], row[1])
            result.append(autenfication)
        c.close()
        conn.close()
        return result

    @staticmethod
    def addmethod(account_name, password):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('INSERT into autenfication values(%s, %s, %s, %s)',
                  (account_name, password))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def updatemethod(account_name, password):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('UPDATE into autenfication values(%s, %s, %s, %s)',
                  (account_name, password))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def deletemethod(account_name, password):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('DELETE into autenfication values(%s, %s, %s, %s)',
                  (account_name, password))
        conn.commit()
        c.close()
        conn.close()


class BackUp:
    def __init__(self, file=None):
        self.file = file

    @property
    def info(self):
        return f'{self.file}'

    @staticmethod
    def getmethod():
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        result = []
        for row in c.execute('select * from BackUp'):
            backUp = BackUp(row[0])
            result.append(backUp)
        c.close()
        conn.close()
        return result

    @staticmethod
    def addmethod(file):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('INSERT into BackUp values(%s, %s, %s, %s)',
                  file)
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def deletemethod(file):
        conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
        c = conn.cursor()
        c.execute('DELETE into BackUp values(%s, %s, %s, %s)',
                  file)
        conn.commit()
        c.close()
        conn.close()
