lst = [[i for i in range(1, 11)] for j in range(10)]  # создаем матрицу 10х10 с уже заполненной верхней строкой

for i in range(len(lst)):  # заполняем первый столбец
    lst[i][0] = lst[0][i]

for i in range(1, len(lst)):  # заполняем остальные ячейки
    for j in range(i, len(lst)):
        lst[i][j] = (i + 1) * (j + 1)
        lst[j][i] = (i + 1) * (j + 1)

for i in range(len(lst)):  # красиво выводим таблицу умноржени
    for j in range(len(lst)):
        print(str(lst[i][j]).center(4), end=' ')
    print()
