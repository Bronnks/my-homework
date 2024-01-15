def multiplication_elem(tpl1, tpl2):
    res = []
    for i in range(len(tpl1)):
        res.append(tpl1[i] * tpl2[i])
    int_or_float(res)
    print(tuple(res))


def int_or_float(lst):
    for i in range(len(lst)):
        if lst[i] - int(lst[i]) == 0:
            lst[i] = int(lst[i])
    return lst


test1 = tuple([float(i) for i in input('Введите первый кортеж, через запятую - ').split(',')])
test2 = tuple([float(i) for i in input('Введите второй кортеж, через запятую - ').split(',')])
multiplication_elem(test1, test2)
