from typing import Union


def sum_all_lists(s: list) -> Union[int, float]:
    res = 0
    for i in s:
        if type(i) is list:
            res += sum_all_lists(i)
        else:
            res += i
    return res


def check_input(lst: list):
    try:
        check_err(lst)  # Переводим числа из строк в флоат и проверяем на ошибки
        int_float(lst)  # если ошибок нет, переводим числа в инт если надо
        print(sum_all_lists(lst))  # считаем числа
    except ValueError:
        print('В списке есть не только числа')


def check_err(lst: list):
    for i, v in enumerate(lst):
        if type(v) is list:
            check_err(v)
        else:
            lst[i] = float(v)


def int_float(s: list) -> list:
    for i, v in enumerate(s):
        if type(v) is list:
            int_float(v)
        else:
            if float(v) - int(v) == 0:
                s[i] = int(v)
    return s


n = int(input('Введите кол-во вложенных списков: '))
test = [[i for i in input('Введите элементы списка через запятую: ').split(',')] for _ in range(n)]
check_input(test)
