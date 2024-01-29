from typing import List
from collections.abc import Callable

def func1(lst: List[int]) -> int:
    summa = sum(func2(lst))
    return summa


def slicer(func: Callable[[List[int]], List[int]]):
    def inner(x: List[int]) -> List[int]:
        if len(x) > 10:
            res = []                      # создаем список,куда будем кидать факториалы
            while len(x) != 0:
                res.extend(func(x[:10]))  # кидаем первые 10 факториалов
                del x[:10]                # уменьшаем начальный список, удаляя уже отформатированные числа
            x = res
        else:
            func(x)
        return x
    return inner


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
print(func1(test))
