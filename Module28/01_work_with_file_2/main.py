import os


class Files:
    """Создаем контекст-менеджер для работы с файлами"""
    def __init__(self, file_name: str) -> None:
        """При создании объекта вводим необходимое имя файла"""
        self.file_name = file_name

    def __enter__(self) -> 'Files':
        """Метод для проверки существует ли указанный нами файл, если отсутствует создаем новый в режиме write"""
        path = os.path.exists(self.file_name)
        if path is not True:
            with open(self.file_name, 'w', encoding='utf-8') as file:
                write = input("Что вы хотите записать в файл? ")
                write = write.replace("\\n", '\n')  # для возможности переноса строки на новую, добавляем
                # небольшую правку
                file.write(write)
                return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Если файл уже существует, выводим его, игнорируя все возможные ошибки"""
        with open(self.file_name, 'r', encoding='utf-8') as file:
            print(file.read())
        if exc_type is Exception or exc_val is Exception or exc_tb is Exception:
            return True


with Files('test.txt') as f:
    """Между enter и exit, выводим сообщение для пользователя с информацией о программе"""
    print('Проверяем наличие файла.\nЕсли файл отсутствует, наша программа его создаст, '
          'запишити в него необходимые данные!\nЕсли файл существует он откроется для чтения!\n')