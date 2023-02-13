from typing import Any, List
import itertools

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    """
    Должна возвращать все пары элементы двух массивов:
    cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    if not arr1 or not arr2:
        return []

    result: List = []

    for element in itertools.product(arr1, arr2):
        result.append(element)

    return result
