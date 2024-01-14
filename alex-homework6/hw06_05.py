import copy

def transpor_massive(lst):
    lst2 = copy.deepcopy(lst)
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            lst2[i][j] = lst[j][i]
    for row in lst2:
        print(*row)


n = int(input('введите кол-во вложенных списков - '))
test = []
for _ in range(n):
    test.append([i for i in input('введите список чисел через запятую - ').split(',')])
transpor_massive(test)
