class QHofstadter:  # Класс для реализации итератора для генерации последовательности Q Хофштадтера
    def __init__(self, s):
        self.s = s[:]
        if s != [1, 1]:  # добавил проверку
            raise StopIteration

    def __next__(self):
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self

    def current_state(self):
        return self.s


q = QHofstadter([1, 1])
print([next(q) for i in range(10)])