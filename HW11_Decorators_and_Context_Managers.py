import time

# Required task


def my_own_deco(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(f"The name of the function - {func.__name__}.\nTime when function was called {args}.")
    return wrapper


@my_own_deco
def func_name_and_time(vremya):
    return
func_name_and_time(time.asctime())



# Optional task 2
def my_own_deco(func):
    def wrapper(*args, **kwargs):
        n = int(args[0])
        while n != 0:
            func(*args, **kwargs)
            t = time.asctime()
            print(f" {n}. The name of the function - {func.__name__}.\nTime when function was called {t}.")
            n -= 1
    return wrapper


@my_own_deco
def func_name_and_time(vremya):
    return
func_name_and_time(8)