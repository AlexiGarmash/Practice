def exp_check(n: str):
    try:
        float(n)
        return True
    except ValueError:
        return False


def exp2(n: float) -> int:
    return n ** 2


def exp3(n: float) -> int:
    return n ** 3
