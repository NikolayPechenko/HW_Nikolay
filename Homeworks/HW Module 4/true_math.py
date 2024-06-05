from math import inf


def divide(first, second):
    if float(second) == 0:
        result = inf
    else:
        result = float(first) / float(second)
    return result
