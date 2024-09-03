def custom_write(file_name, strings):   #Создайте функцию custom_write(file_name, strings),
    # которая принимает аргументы file_name - название файла для записи, strings - список строк для записи.
    strings_positions = {}  #создаем пустой словарь

    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings):    #перебираем список
            start_position = file.tell()    # Возвращает текущую позицию указателя в файле относительно его начала
            file.write(string + '\n')   #Записываем в файл с новой строки
            strings_positions[(i + 1, start_position)] = string

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)