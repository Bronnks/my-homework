lst = [[i for i in range(1, 11)] for j in range(10)]

for i in range(len(lst)):
    lst[i][0] = lst[0][i]

for i in range(1, len(lst)):
    for j in range(i, len(lst)):
        lst[i][j] = (i + 1) * (j + 1)
        lst[j][i] = (i + 1) * (j + 1)

for i in range(len(lst)):
    for j in range(len(lst)):
        print(str(lst[i][j]).center(4), end=' ')
    print()
