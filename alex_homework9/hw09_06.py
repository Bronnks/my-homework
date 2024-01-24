def reverse_int2(n: int) -> int:  # вариант функции, где находится развернутое число, но т.к.
    res = n % 10  # число 12340 в развороте будет 04321, то тут у нас будет теряться 0 при выводе
    if n < 10:
        return n
    count = 1  # с помощью счетчика считаем разрядность числа.
    s = n
    while s > 9:
        count *= 10
        s = s // 10
    x = res * count
    return x + reverse_int2(n // 10)


def reverse_int(n: int):  # вариант функции, где выводится все посимвольно
    print(n % 10, end='')
    if n < 10:
        return
    return reverse_int(n // 10)


def check_int(t):
    if t == 0:
        print(0)
    elif t < 0:
        print('-', end='')
        reverse_int(abs(t))
    else:
        reverse_int(t)


test = int(input('Введите число:'))
check_int(test)
