def cach_dec(fun):
    storage = {}

    def wrapper(*args, **kwargs):
        number = args[0]
        if number in storage:
            return storage[number]
        storage[number] = fun(*args, **kwargs)
        return storage[number]
    return wrapper


@cach_dec
def multiplier(number: int):
    return number * 2
