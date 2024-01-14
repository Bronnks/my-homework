def check_height(lst):
    lst = check_input(lst)
    average = sum(lst) / len(lst)
    count = 0
    for i in lst:
        if i > average:
            count += 1
    print(f'В классе людей, чей рост выше среднего - {count} ')


def check_input(lst):
    norm_input = []
    for i in range(len(lst)):  # рост человека не может быть отрицательным
        if 0 < lst[i] <= 3:    # рост человека не может быть выше 3 метров
            norm_input.append(lst[i])
    return norm_input


test = [float(i) for i in input('Введите список с ростом учеников, в одну строчку через запятую - ').split(',')]
check_height(test)
