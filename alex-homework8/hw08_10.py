def create_set():
    res = set(map(int, input('Введите элементы множества через пробел - ').split()))
    return res


def sub(subs, el):               # проходимся по элементу и добавляем в список подмножество(список)
    for i in range(len(el)):
        x = el[:i] + el[i + 1:]  # тот самый список-подмножество
        if x not in subs:
            subs.append(x)


def gen2(test_set):
    subsets = [list(test_set)]
    for elem in subsets:
        sub(subsets, elem)
    for i in range(len(subsets)):    # переводим списки во множества по заданию
        subsets[i] = set(subsets[i])
    print(subsets)


test = create_set()
gen2(test)
