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


def union_dict(s1, s2):
    print(f'Объединение: {s1 | s2}')


def intersection_dict(s1, s2):
    print(f'Пересечение: {s1 & s2}')


def difference_dict(s1, s2):
    print(f'Разность: {s1 - s2}')


def sym_diff(s1, s2):
    print(f'Симметричная разность: {s1 ^ s2}')


def operations_with_2_sets(s1, s2):
    union_dict(s1, s2)
    intersection_dict(s1, s2)
    difference_dict(s1, s2)
    sym_diff(s1, s2)


test1 = create_set()
test2 = create_set()
operations_with_2_sets(test1, test2)
