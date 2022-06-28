from math import prod
from itertools import combinations_with_replacement


def count_find_num(primesL, limit):
    resmin = prod(primesL)
    if resmin > limit:
        return []
    resmax = resmin
    res = resmin
    summ = 1
    i = 0
    while resmin * primesL[0] ** i <= limit:
        i += 1
        combin = combinations_with_replacement(primesL, i)
        for comb in combin:
            res = resmin * prod(comb)
            if res <= limit:
                if res > resmax:
                    resmax = res
                summ += 1
    return [summ, resmax]


