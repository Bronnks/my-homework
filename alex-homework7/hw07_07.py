def check_value(dct, key):
    if key in dct:
        print(f'Значение: {dct[key]}')
    else:
        print('Ключ не найден')


n = int(input('Введите количество элементов в словаре - '))
test = dict(input('Введите ключ и значение через пробел - ').split() for _ in range(n))
ind = input('Введите ключ для проверки - ')
check_value(test, ind)
