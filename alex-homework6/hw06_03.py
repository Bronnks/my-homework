def max_min(lst):
    max_num = lst[0]
    min_num = lst[0]
    for i in range(1,len(lst)):
        if lst[i] > max_num:
            max_num = lst[i]
        elif lst[i] < min_num:
            min_num = lst[i]
    print(f'Минимальное = {min_num}, максимальное = {max_num}')

# когда вводится просто строка с числами
# test = list(map(float, input('Введите числа в одну строку через пробел - ').split()))

# когда вводится список со скобками
test = [float(i) for i in input()[1:-1].split(",")]
max_min(test)

