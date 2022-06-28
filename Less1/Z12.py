def int32_to_ip(int32):
    res = [0] * 4
    for i in range(3, 0, -1):
        res[i] = int32 % 256
        int32 = int32 // 256
    res[0] = int32
    return '.'.join(map(str, res))
