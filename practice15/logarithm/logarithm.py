import math


def log_check(a=2, b=0):
    try:
        if float(a) > 0 and float(a) != 1 and float(b) > 0:
            return True
    except ValueError:
        return False


def log(a: float, b: float):
    return math.log(b, a)


def ln(b: float):
    return math.log1p(b)


def lg(b: float):
    return math.log10(b)