from copy import deepcopy
from collections.abc import Callable
from typing import Dict, Union, List, Any


def check_value(i: str, v: Any) -> Dict[str, Any]:
    if type(v) is str:
        return {i.upper(): v.upper()}
    else:
        return {i.upper(): v}


# как я сделал этот декоратор мне самому не нравится, подгонял решение под примеры, а не под правильную логику
# т.к. логику изменения этих словарей не понимал, а точнее 3 и 4 пример
def upper_case(func: Callable[[], Dict[str, Any]]):
    def wrapper():
        s = func()
        d = deepcopy(s)
        for ind, val in s.items():
            d.update(check_value(ind, val))
        s = deepcopy(d)
        for ind, val in s.items():  # а точнее я не смог придумать рекурсию
            if type(val) is list:   
                for i, v in enumerate(val):
                    if type(v) is dict:
                        for b, c in v.items():
                            d[ind][i].update(check_value(b, c))
        return print(d)

    return wrapper


@upper_case
def f1() -> Dict[str, int]:
    return {'a': 1, 'b': 2}


@upper_case
def f2() -> Dict[str, Union[str, int]]:
    return {'a': 'a', 'b': 'b'}


@upper_case
def f3() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
    return {'a': 'a', 'c': [{'b': 'b'}]}


@upper_case
def f4() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
    return {'a': 'a', 'c': [{'b': 1}, {'d': 2}]}


f1()
f2()
f3()
f4()
