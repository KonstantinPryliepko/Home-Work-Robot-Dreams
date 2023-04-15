
# Required task
def input_func():
    number = input("Input number: ")
    return number


def recursion_func(any_numbers: int):
    if any_numbers == 0:
        return 0
    else:
        print(any_numbers)
        num = recursion_func((any_numbers - 1))
        return num


# Optional task
    # Fibonacci sequence
def fib_sequence(any_numbers):
    if any_numbers == 0:
        return 0
    elif any_numbers == 1:
        return 1
    else:
        num = fib_sequence(any_numbers-1) + fib_sequence(any_numbers-2)
        return num


# Factorial number
def factorial_func(any_numbers):
    if any_numbers == 0:
        return 1
    else:
        num = any_numbers * fib_sequence(any_numbers-1)
        return num


def main():
    # Required task
    any_numbers = input_func()
    if any_numbers.isdigit():
        print('Required task. Just recursion.')
        num = recursion_func(int(any_numbers))
        print(num)

    # Optional task
        # Fibonacci sequence
        print('Optional task. Fibonacci sequence.')
        fib = fib_sequence(int(any_numbers))
        print(f'Fibonacci number is {fib}')

        # Factorial
        print('Optional task. Factorial.')
        fact = factorial_func(int(any_numbers))
        print(f'Factorial number is {fact}')
    else:
        print("You entered not a number.")


main()
