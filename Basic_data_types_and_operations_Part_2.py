# Required task
input_something = input("Input something - ")
if input_something.isdigit():
    if int(input_something) % 2 == 0:
        print(f" The {input_something} is digit. And the number is even.")
    else:
        print(f" The {input_something} is digit. And the number is odd.")
elif input_something.isalpha():
    print(f" The {input_something} is word, its length is {len(input_something)}.")
else:
    print("Error")

# Optional task
input_something = input("Input something - ")
match input_something:
    case int():
        print(f" The {input_something} is digit.")
    case str():
        print(f" The {input_something} is word.")