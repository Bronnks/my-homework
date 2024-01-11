lst = [[i for i in range(1, 11)] for j in range(10)]

for i in range(len(lst)):
    lst[i][0] = lst[0][i]

i = 1  # строки
j = 1  # столбцы
while j < 10:
    while i < 10:
        lst[i][j] = (i + 1) * (j + 1)
        lst[j][i] = (i + 1) * (j + 1)
        i += 1
    j += 1
    i = j

for i in range(len(lst)):
    for j in range(len(lst)):
        print(str(lst[i][j]).center(4), end=' ')
    print()
