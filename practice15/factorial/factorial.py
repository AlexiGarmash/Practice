def fact_check(n: str):
    try:
        if int(n) == float(n) and int(n) > 0:
            return True
    except ValueError:
        return False


def fact(n: int) -> int:
    if n == 0:
        return 1
    return fact(n - 1) * n
