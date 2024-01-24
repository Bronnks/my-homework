def sort_by_length(lst: list) -> list:
    return sorted(lst, key=len)


test = [i for i in input('Введите строки через запятую - ').split(',')]
print(sort_by_length(test))
