from typing import List
from collections.abc import Callable
import time


def func1(lst: List[int]) -> int:
    summa = sum(func2(lst))
    return summa


def slicer(func: Callable[[List[int]], List[int]]):
    def inner(x: List[int]) -> List[int]:
        if len(x) > 10:
            res = []
            while len(x) != 0:
                res.extend(func(x[:10]))
                del x[:10]
            x = res
        else:
            func(x)
        return x

    return inner


def benchmark(func: Callable[[List[int]], List[int]]):
    def inner(*args):
        start = time.perf_counter()
        res = func(*args)
        end = time.perf_counter() - start
        print(f'Функция на работу потратила: {end:.6f} секунд.')
        return res
    return inner


@benchmark
@slicer
def func2(lst: List[int]) -> List[int]:
    if len(lst) > 10:
        raise Exception('Слишком длинный список, максимум 10 чисел.')
    for i, v in enumerate(lst):
        def fact(n: int) -> int:
            if n <= 0:
                return 1
            return n * fact(n - 1)

        lst[i] = fact(v)
    return lst


test = [int(i) for i in input('Введите целые числа через пробел: ').split()]
print(f'Сумма факториалов = {func1(test)}')
