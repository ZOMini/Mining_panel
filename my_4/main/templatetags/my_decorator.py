import functools
import time


def my_exception(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
            return result
        except Exception as e:
            empty = {}
            print(f'Лови пустоту. Случилась глобальная хрень. Error: {e}. Но мы продолжаем работу!')
            return empty
    return wrapper


def timeit(method):
    @functools.wraps(method)
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te - ts))
        return result
    return timed
