def minmax(lst):
    min_num = lst[0]
    max_num = lst[0]
    for i in lst[1:]:
        if i < min_num:
            min_num = i
        elif i > max_num:
            max_num = i
    res = (int_or_float(min_num), int_or_float(max_num))
    print(res)


def int_or_float(n):  # проверяем число целое или не очень, для более красивого вывода
    if n - int(n) == 0:
        n = int(n)
    return n


test = [float(i) for i in input('Введите список чисел через запятую - ').split(',')]
minmax(test)
