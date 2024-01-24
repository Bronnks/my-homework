def modify_list(lst: list, *funcs: callable) -> None:
    for j in funcs:
        for i, v in enumerate(lst):
            lst[i] = j(v)


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


test = [int(i) for i in input('Введите список целых чисел через запятую: ').split(',')]
modify_list(test, lambda x: x ** x if x % 2 == 0 else x, lambda x: x + 1 if x % 2 != 0 else x,
            lambda x: x * 3 if is_prime(x) else x)
print(test)
