from modules.divider import divider as d
import time


def chronometer(func):
    def wrapper(n):
        start = time.time()
        func(n)
        end = time.time()
        print(f"Elapsed time: {end - start}")
    return wrapper


@chronometer
def short_sleep(n):
    time.sleep(n)


@chronometer
def long_sleep(n):
    time.sleep(n)


d()


short_sleep(1)
print("Hello World")
long_sleep(3)


d()
