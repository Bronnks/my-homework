def int_or_float(lst):  # проверяем число целое или не очень, для более красивого вывода
    for j in range(len(lst)):
        if lst[j] - int(lst[j]) == 0:
            lst[j] = int(lst[j])


test1 = [float(i) for i in input('Введите первый список чисел через запятую - ').split(',')]
test2 = [float(i) for i in input('Введите второй список чисел через запятую - ').split(',')]
res = sorted(test1 + test2)
int_or_float(res)
print('Отсортированные два списка')
print(*res)
print('Отсортированные два списка, без повторяющихся чисел')
print(*sorted(set(res)))
