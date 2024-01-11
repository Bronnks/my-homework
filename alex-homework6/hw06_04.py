def int_or_float(lst):  # проверяем число целое или не очень, для более красивого вывода
    for j in range(len(lst)):
        if lst[j] - int(lst[j]) == 0:
            lst[j] = int(lst[j])


def max_in(lst):
    maxlst = []
    for x in lst:
        maxlst.append(max(x))
    int_or_float(maxlst)
    print(maxlst)


n = int(input('введите кол-во вложенных списков - '))
test = []
for i in range(n):
    test.append([float(i) for i in input('введите список чисел через запятую - ').split(',')])
max_in(test)
