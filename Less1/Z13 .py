def zeros(n):
    if n < 5:
        return 0
    res = 0
    pow = 5
    while pow <= n:
        res += n // pow
        pow *= 5
    return res
