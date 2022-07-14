import time


def extern_dec_param(call_count, start_sleep_time, factor, border_sleep_time):

    def dec_param(funс):

        def wrapper(*args, **kwargs):
            print('Начало работы')
            number = args[0]
            func_result = funс(*args, **kwargs)
            times = start_sleep_time
            counter = 0
            while times < border_sleep_time:
                time.sleep(times)
                func_result = funс(*args, **kwargs)
                print(f'Запуск номер {counter + 1}. Ожидание: {times} секунд. Результат декорируемой функции = '
                      f'{func_result}')
                times *= factor
                counter += 1
            if counter < call_count:
                for i in range(call_count - counter):
                    time.sleep(border_sleep_time)
                    func_result = funс(*args, **kwargs)
                    print(f'Запуск номер {i + 1 + counter}. Ожидание: {border_sleep_time} секунд. Результат '
                          f'декорируемой функции = {func_result}')
            print('Конец работы')
            return func_result
        return wrapper
    return dec_param


@extern_dec_param(7, 1, 2, 10)
def multiplier(number: int):
    return number * 2

multiplier(3)
