def root_check(n):
    try:
        if float(n) > 0:
            return True
    except ValueError:
        return False


def root2(n: float) -> float:
    return n ** (1 / 2)


def root3(n: float) -> float:
    return n ** (1 / 3)
