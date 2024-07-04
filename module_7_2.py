def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as f:
        strings_positions = {}
        # Запись каждой строки в файл и обновление словаря позиций
        for i, s in enumerate(strings):
            f.write(s + '\n')
            strings_positions[(i + 1, f.tell() - len(s))] = s
        # Закрытие файла
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