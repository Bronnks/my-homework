def map_square(lst: list) -> list:
    res = list(map(lambda x: x * x, lst))
    return res


def int_float(s: list) -> list:
    for i, v in enumerate(s):
        if v - int(v) == 0:
            s[i] = int(v)
    return s

test = [float(i) for i in input('Введите числа через запятую - ').split(',')]
int_float(test)
print(map_square(test))
