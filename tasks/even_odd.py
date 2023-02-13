__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    if not arr:
        return 0

    even_list= list(filter(lambda element: element % 2 == 0, arr))
    odd_list = list(filter(lambda element: element % 2 != 0, arr))

    if not odd_list:
        return 0
    if not even_list:
        return 0

    return sum(even_list) / sum(odd_list)
