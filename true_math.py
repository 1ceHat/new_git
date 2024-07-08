from math import inf


def divide(first, second):
    if float(second) == 0:
        return inf
    else:
        return float(first)/float(second)