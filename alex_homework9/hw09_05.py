from typing import Union


def sum_all_lists(s: list) -> Union[int, float]:
    res = 0
    for i in s:
        if type(i) is list:
            res += sum_all_lists(i)
        else:
            res += i
    return res


def int_float(s: list) -> list:
    for i, v in enumerate(s):
        if v - int(v) == 0:
            s[i] = int(v)
    return s


n = int(input('Введите кол-во вложенных списков'))
test = [[float(i) for i in input('Введите числа, через пробел:').split()] for _ in range(n)]
int_float(test)
print(sum_all_lists(test))
