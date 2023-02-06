students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    interes = [students[i_interes]['interests'] for i_interes in students]
    interes = sum(interes, [])
    interes = ', '.join(interes)
    interes = '{' + interes + '}'
    surname = [students[i_surname]['surname'] for i_surname in students]
    surname = ''.join(surname)
    return interes, len(surname)


id = list(students)
age = [students[i_age]['age'] for i_age in students]
id = list(zip(id, age))
print('Список пар "ID студента — возраст":{id}'.format(id=id))
print('Полный список интересов всех студентов:', f(students)[0])
print('Общая длина всех фамилий студентов:', f(students)[1])
