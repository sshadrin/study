import mysql.connector
from model import*
import unittest


def check_count():
    conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
    c = conn.cursor()
    res = c.execute('select count(*) from Facultet').fetchone()
    c.close()
    conn.close()
    return res


class TestFacultet(unittest.TestCase):

    def test_getmethod(self):
        self.assertEqual(12, len(Facultet.getmethod()))

    def test_addmethod(self):
        c = check_count()
        Facultet.addmethod("IT", 'Ivanov', '20', '2', 8 - 911 - 000 - 00 - 00)
        self.assertGreater(check_count(), c)

    def test_updatemethod(self):
        c = check_count()
        Facultet.updatemethod("IT", 'Petrov', '20', '2', 8 - 911 - 111 - 11 - 11)
        self.assertGreater(check_count(), c)

    def test_deletemethod(self):
        c = check_count()
        Facultet.deletemethod("IT", 'Petrov', '20', '2', 8 - 911 - 111 - 11 - 11)
        self.assertGreater(check_count(), c)


if __name__ == '__main__':
    unittest.main()


def check_count():
    conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
    c = conn.cursor()
    res = c.execute('select count(*) from Kafedra').fetchone()
    c.close()
    conn.close()
    return res


class TestKafedra(unittest.TestCase):

    def test_getmethod(self):
        self.assertEqual(12, len(Kafedra.getmethod()))

    def test_addmethod(self):
        c = check_count()
        Kafedra.addmethod("WEB", 'Petrov', '20', '2', 8-911-000-00-00, 8-911-000-22-22)
        self.assertGreater(check_count(), c)

    def test_updatemethod(self):
        c = check_count()
        Kafedra.updatemethod("WEB", 'Sidorov', '20', '2', 8-911-000-00-00, 8-911-000-33-33)
        self.assertGreater(check_count(), c)

    def test_deletemethod(self):
        c = check_count()
        Kafedra.deletemethod("WEB", 'Petrov', '20', '2', 8-911-000-00-00, 8-911-000-22-22)
        self.assertGreater(check_count(), c)


if __name__ == '__main__':
    unittest.main()


def check_count():
    conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
    c = conn.cursor()
    res = c.execute('select count(*) from Teacher').fetchone()
    c.close()
    conn.close()
    return res


class TestTeacher(unittest.TestCase):

    def test_getmethod(self):
        self.assertEqual(12, len(Teacher.getmethod()))

    def test_addmethod(self):
        c = check_count()
        Teacher.addmethod("Sokolov", 1980-4-26, Kafedra, 2005, 17, "docent", "male", "Archangelsk")
        self.assertGreater(check_count(), c)

    def test_updatemethod(self):
        c = check_count()
        Teacher.updatemethod("Ivanova", 1988-2-3, Kafedra, 2015, 7, "teacher", "female", "Novodvinsk")
        self.assertGreater(check_count(), c)

    def test_deletemethod(self):
        c = check_count()
        Teacher.deletemethod("Sokolov", 1980-4-26, Kafedra, 2005, 17, "docent", "male", "Archangelsk")
        self.assertGreater(check_count(), c)


if __name__ == '__main__':
    unittest.main()


def check_count():
    conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
    c = conn.cursor()
    res = c.execute('select count(*) from Discipline').fetchone()
    c.close()
    conn.close()
    return res


class TestDiscipline(unittest.TestCase):

    def test_getmethod(self):
        self.assertEqual(12, len(Discipline.getmethod()))

    def test_addmethod(self):
        c = check_count()
        Discipline.addmethod("Architecture of information system", 300, "Computer science")
        self.assertGreater(check_count(), c)

    def test_updatemethod(self):
        c = check_count()
        Discipline.updatemethod("Discrete mathematics", 200, "mathematics")
        self.assertGreater(check_count(), c)

    def test_deletemethod(self):
        c = check_count()
        Discipline.deletemethod("Architecture of information system", 300, "Computer science")
        self.assertGreater(check_count(), c)


if __name__ == '__main__':
    unittest.main()


def check_count():
    conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
    c = conn.cursor()
    res = c.execute('select count(*) from AcademicLoad').fetchone()
    c.close()
    conn.close()
    return res


class TestAcademicLoad(unittest.TestCase):

    def test_getmethod(self):
        self.assertEqual(12, len(AcademicLoad.getmethod()))

    def test_addmethod(self):
        c = check_count()
        AcademicLoad.addmethod(Teacher, Discipline, 300, 1, 5, 150, "exam")
        self.assertGreater(check_count(), c)

    def test_updatemethod(self):
        c = check_count()
        AcademicLoad.updatemethod(Teacher, Discipline, 300, 2, 3, 90, "exam")
        self.assertGreater(check_count(), c)

    def test_deletemethod(self):
        c = check_count()
        AcademicLoad.deletemethod(Teacher, Discipline, 300, 1, 5, 150, "exam")
        self.assertGreater(check_count(), c)


if __name__ == '__main__':
    unittest.main()


def check_count():
    conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
    c = conn.cursor()
    res = c.execute('select count(*) from Account').fetchone()
    c.close()
    conn.close()
    return res


class TestAccount(unittest.TestCase):

    def test_getmethod(self):
        self.assertEqual(12, len(Account.getmethod()))

    def test_addmethod(self):
        c = check_count()
        Account.addmethod("name", "pass")
        self.assertGreater(check_count(), c)

    def test_updatemethod(self):
        c = check_count()
        Account.updatemethod("name", "pass")
        self.assertGreater(check_count(), c)

    def test_deletemethod(self):
        c = check_count()
        Account.deletemethod("name", "pass")
        self.assertGreater(check_count(), c)


if __name__ == '__main__':
    unittest.main()


def check_count():
    conn = mysql.connector.connect(user='u01', password='u01', host='root', database='lab4')
    c = conn.cursor()
    res = c.execute('select count(*) from Account').fetchone()
    c.close()
    conn.close()
    return res


class TestAccount(unittest.TestCase):

    def test_getmethod(self):
        self.assertEqual(12, len(Autenfication.getmethod()))

    def test_addmethod(self):
        c = check_count()
        Autenfication.addmethod("name", "pass")
        self.assertGreater(check_count(), c)

    def test_updatemethod(self):
        c = check_count()
        Autenfication.updatemethod("name", "pass")
        self.assertGreater(check_count(), c)

    def test_deletemethod(self):
        c = check_count()
        Autenfication.deletemethod("name", "pass")
        self.assertGreater(check_count(), c)


if __name__ == '__main__':
    unittest.main()


class TestBackUp(unittest.TestCase):

    def test_getmethod(self):
        self.assertEqual(12, len(BackUp.getmethod()))

    def test_addmethod(self):
        c = check_count()
        BackUp.addmethod("file")
        self.assertGreater(check_count(), c)

    def test_deletemethod(self):
        c = check_count()
        BackUp.deletemethod("file")
        self.assertGreater(check_count(), c)


if __name__ == '__main__':
    unittest.main()
