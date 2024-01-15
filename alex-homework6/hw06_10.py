def check_brackets(line):
    if len(line) % 2 == 1:
        return print('Строка не допустимая')
    while any(('()' in line, '[]' in line, '{}' in line)):
        line = line.replace('()', '').replace('[]', '').replace('{}', '')
    if len(line) > 0:
        print('Строка не допустимая')
    else:
        print('Строка допустимая')


test = input('Введите строку со скобками - ')
check_brackets(test)
