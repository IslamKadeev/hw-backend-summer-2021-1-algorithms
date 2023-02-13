__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    dividers: int = 0

    if number == 1 or number == 0:
        return False

    for num in range(1, number // 2 + 1):
        if number % num == 0:
            dividers += 1
            if dividers > 1:
                return False
    return True
