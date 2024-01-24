from typing import Union


def power(x: Union[float, int], y: int) -> Union[float, int]:
    if y == 1:
        return x
    else:
        return x * power(x, y - 1)


def check_input_and_power(s: float, c: int):
    if s == 0:
        print(1)
        return
    if c <= 0:
        print('При решении этой задачи с помощью рекурсии, второе число должно быть целым и больше нуля.')
    else:
        if s - int(s) == 0:
            s = int(s)
        print(power(s, c))


n, m = float(input('Введите первое число:')), int(input('Введите второе число:'))
check_input_and_power(n, m)
