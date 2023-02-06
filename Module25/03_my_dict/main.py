class MyDict(dict):

    def get(self, key, default=0):
        return super().get(key, default)


dictionary = {'1': 'python', '2': 'C', '3': 'php', '4': 'C#'}
a = MyDict(dictionary)
print(a.get('1'))
print(a.get('5'))


