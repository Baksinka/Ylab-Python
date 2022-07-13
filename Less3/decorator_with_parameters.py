import time


def extern_dec_param(call_count, start_sleep_time, factor, border_sleep_time):

    def dec_param(funс):

        def wrapper(*args, **kwargs):
            number = args[0]
            func_result = funс(*args, **kwargs)
            times = start_sleep_time
            counter = 0
            while times < border_sleep_time:
                time.sleep(times)
                times *= factor
                func_result = funс(*args, **kwargs)
                counter += 1
            if counter < call_count:
                for i in range(call_count - counter):
                    time.sleep(border_sleep_time)
                    func_result = funс(*args, **kwargs)
            return func_result
        return wrapper
    return dec_param


@external_dec_param(7, 1, 2, 10)
def multiplier(number: int):
    return number * 2

multiplier(3)
