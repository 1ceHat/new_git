def custom_write(file_name, strings):
    dict_write = {}
    file = open(file_name, 'w', encoding='utf-8')
    i = 0
    for string in strings:
        i += 1
        current_pos = file.tell()
        dict_write[(i, current_pos)] = string
        file.write(string+'\n')
    file.close()
    return dict_write


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
