from typing import List


def func1(lst: List[int]) -> int:
    summa = sum(func2(lst))
    return summa


def slicer(func):  # не нашел как для декораторов делать аннотацию
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
