def sum_col_dict(lst):  # считаем через словарь
    res_dict = {}
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j not in res_dict:
                res_dict[j] = lst[i][j]
            else:
                res_dict[j] += lst[i][j]
    int_or_float(res_dict)
    for key, value in res_dict.items():
        print(f'Сумма элементов в столбце №{key + 1}  = {value}')


def sum_col(lst):  # считаем через список
    res_list = lst[0]
    for i in range(1, len(lst)):
        for j in range(len(lst[0])):
            res_list[j] += lst[i][j]
    int_or_float(res_list)
    for x in range(len(res_list)):
        print(f'Сумма элементов в столбце №{x + 1}  = {res_list[x]}')


def check_list(lst):  # проверяем одинаковые ли по размеру вложенные списки
    for i in range(1, len(lst)):
        if len(lst[i]) != len(lst[0]):
            return sum_col_dict(lst)
    return sum_col(lst)


def int_or_float(lst):  # проверяем число целое или не очень, для более красивого вывода
    for j in range(len(lst)):
        if lst[j] - int(lst[j]) == 0:
            lst[j] = int(lst[j])
            

# конечно можно обойтись и без проверки на размер вложенных, и оставить подсчет только по словарю

n = int(input('Введите кол-во вложенных списков - '))
test = [[float(i) for i in input('Введите строку чисел через запятую - ').split(',')] for _ in range(n)]
check_list(test)
