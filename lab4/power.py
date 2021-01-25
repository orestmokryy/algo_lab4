from math import log


def can_be_power(binary, x):
    decimal = int(binary, 2)
    if int(binary) == 0:
        return False
    if x == 1:
        return decimal == 1
    logarithm = log(decimal, x)
    if x ** int(logarithm) == decimal:
        return True
    else:
        return False
