lst = [[i for i in range(1,11)] for j in range(1, 11)]
for row in lst[1:]:
    for cow in row:
        lst[i][j] = i*j
for row in lst:
    print(*row)