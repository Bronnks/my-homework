def even_uneven(tpl):
    count = sum([i for i in tpl if i % 2 == 0])
    print(int(count))


test = tuple([float(i) for i in input('Введите строку чисел через запятую - ').split(',')])
even_uneven(test)
