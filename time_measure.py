import time
def measure_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        try:
            time.sleep(2)
            return func(*args, **kwargs)
        finally:
            ex_time = time.time() - start_time
            print(f'Execution time: {ex_time:.2f} seconds')
    return inner