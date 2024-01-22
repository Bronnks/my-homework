def create_set():
    test = set(map(int, input('Введите элементы множества через пробел - ').split()))
    return test


def sub(subs, el):
    for i in range(len(el)):
        el = list(el)
        x = el[:i] + el[i + 1:]
        if x not in subs:
            subs.append(x)


def gen2(testset):
    subset = [list(testset)]
    for elem in subset:
        sub(subset, elem)
    for i in range(len(subset)):
        subset[i] = set(subset[i])
    print(subset)


test = create_set()
gen2(test)
