def create_dict(lst):
    split_list(lst)
    dct = {i[0]: int(i[-1]) for i in lst}
    print(dct)


def split_list(lst):
    for i in range(len(lst)):
        lst[i] = lst[i].split()
    return lst


test = input('Введите список значений через запятую - ').split(',')
create_dict(test)
