import json
import time


def my_own_deco(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        t = time.asctime()
        write_data = "\nThe name of the function - " + str(func.__name__) + ". Time when function was called " + str(t) +"."
        with open('text_decorator_file.txt', 'a') as myfile:
            myfile.write(write_data)
    return wrapper


def read_phone_book(phone_book):
    try:
        with open('test.txt', 'r') as json_file:
            phone_book = json.load(json_file)
    except (TypeError, IOError):
        print('Ups empty file.')
    return phone_book


def input_func(phone_book):
    phone_number = []
    name_contact = input("Input Name and Surname:")
    number = input("Input phone number:")
    phone_number.append(number)
    phone_book[name_contact] = phone_number
    return phone_book


def delete_func(phone_book):
    user_name = input("Input the name you want to delete:")
    try:
        phone_book.pop(user_name)
    except (SyntaxError, TypeError):
        print(f"The name {user_name} is not in the phone book.")
    return phone_book


def show_name_func(phone_book):
    user_name = input("Input the name you want to show:")
    try:
        phone_number = phone_book.get(user_name)
        print(f"This name is in the phone book. Subscriber's name {user_name}, phone number {' '.join(phone_number)}.")
    except (KeyError, TypeError):
        print(f"The name {user_name} is not in the phone book.")
    return phone_book


def user_command_func():
    user_comm = input("Input one of the suggested commands (stats, add, delete, list, show or quit): ")
    return user_comm


@my_own_deco
def write_phone_book(new_phone_book):
    data = json.dumps(new_phone_book)
    with open('my_json.txt', 'wt') as myfile:
        myfile.write(data)


def main():
    phone_book = {}
    new_phone_book = read_phone_book(phone_book)

    while len(phone_book) < 2:
        input_func(phone_book)
    print(phone_book)

    new_phone_book.update(phone_book)
    print(new_phone_book)
    write_phone_book(new_phone_book)


    end_variable = True
    while end_variable:
        phone_book = {}
        user_command = user_command_func()

        if user_command == "stats":
            print(len(new_phone_book))
        elif user_command == "add":
            input_func(phone_book)
            print(phone_book)
            new_phone_book.update(phone_book)
            write_phone_book(new_phone_book)

        elif user_command == "delete":
            new_phone_book = read_phone_book(phone_book)
            update_phone_book = delete_func(new_phone_book)
            print(update_phone_book)
            new_phone_book.update(update_phone_book)
            write_phone_book(new_phone_book)

        elif user_command == "list":
            lst_name = []
            for key in new_phone_book.keys():
                lst_name.append(key)
            print(lst_name)

        elif user_command == "show":
            show_name_func(new_phone_book)
        elif user_command == "quit":
            end_variable = False
            quit()


main()
