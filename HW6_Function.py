# Task 1
def exponent_digits(x, y):
    return x ** y
def main():
    pow_digits = exponent_digits(x=9, y=3)
    print(pow_digits)
main()


# Task 2
def sum_any_numbers(*args):
    sum_tpl = sum(args)
    #print(type(args))
    return sum_tpl
def main():
    any_numbers = sum_any_numbers(1, 2, 3, 4, 5, 6, 7, 8, 111)
    print(any_numbers)
main()