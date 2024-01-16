def union_dict(dct1, dct2):
    for k in dct2.keys():
        dct1[k] = dct2[k]
    print(dct1)


def create_dict():
    n = int(input('Введите количество элементов в словаре - '))
    test = dict(input('Введите ключ и значение через пробел - ').split() for _ in range(n))
    return test


test1 = create_dict()
test2 = create_dict()

union_dict(test1, test2)
