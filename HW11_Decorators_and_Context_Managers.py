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
def my_own_deco(my_varaible):
    def wrapper(func):
        def inner(*args, **kwargs):
            print(f"The name is {my_varaible}")
            n = int(my_varaible)
            while n != 0:
                t = time.asctime()
                print(f" {n}. The name of the function - {func.__name__}.\nTime when function was called {t}.")
                n -= 1
        return inner
    return wrapper


@my_own_deco(my_varaible="5")
def func_name_and_time(a, b):
    return
func_name_and_time(1, 2)
