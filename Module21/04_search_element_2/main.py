site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search_element(data, tag):
    result = None
    if tag in data:
        return data[tag]
    for key, value in data.items():
        if isinstance(value, dict):
            result = search_element(value, tag)
            if result:
                return result
    return result


def find_key(struct, key, depth):
    if key in struct:
        return struct[key]
    if depth > 1:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key, depth - 1)
                if result:
                    break
        else:
            result = None
        return result


user_key = input('Введите искомый ключ:')
deep = input('Хотите ввести максимальную глубину? Y/N:')
if deep == 'n':
    value = search_element(site, user_key)
    if value:
        print("Значение:", value)
    else:
        print("Такого ключа в структуре сайта нет.")
elif deep == 'y':
    search_depth = int(input('Введите глубину поиска: '))
    value = find_key(site, user_key, search_depth)
    if value:
        print(value)
    else:
        print('Такого ключа в структуре сайта нет.')
else:
    print('error')