def create_set():
    test = set(map(int_float_str, input('Введите элементы множества через пробел - ').split()))
    return test


def int_float_str(s):  # определяем тип данных в множестве, для красивого отображения
    if s.isalpha():
        return s
    elif s.replace('-', '').isdigit():
        return int(s)
    else:
        return float(s)


def subset(s1, s2):
    if s1.issubset(s2) or s2.issubset(s1):
        print('Да')
    else:
        print('Нет')


test1 = create_set()
test2 = create_set()
subset(test1, test2)
