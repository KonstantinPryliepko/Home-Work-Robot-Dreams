

def input_func(phone_book):
    phone_number = []
    name_contact = input("Input Name and Surname:")
    number = input("Input phone number:")
    phone_number.append(number)
    phone_book[name_contact] = phone_number
    return phone_book


def user_command_func():
    user_command = input("Input one of the suggested commands (stats, add, delete, list, show or quit):")
    return user_command


def delete_func(phone_book):
    user_name = input("Input the name you want to delete:")
    if user_name in phone_book:
        phone_book.pop(user_name)
    else:
        print(f"The name {user_name} is not in the phone book.")
    return phone_book


def show_name_func(phone_book):
    user_name = input("Input the name you want to show:")
    if user_name in phone_book:
        phone_number = phone_book.get(user_name)
        print(f"This name is in the phone book. Subscriber's name {user_name}, phone number {' '.join(phone_number)}.")
    else:
        print(f"The name {user_name} is not in the phone book.")
    return phone_book


def main():
    phone_book = {}
    while len(phone_book) < 3:
        input_func(phone_book)
    print(phone_book)

    user_command = user_command_func()
    if user_command == "stats":
        print(len(phone_book))
        user_command_func()
    elif user_command == "add":
        input_func(phone_book)
        print(phone_book)
        user_command_func()
    elif user_command == "delete":
        update_phone_book = delete_func(phone_book)
        print(update_phone_book)
        user_command_func()
    elif user_command == "list":
        lst_name = []
        for key in phone_book.keys():
            lst_name.append(key)
        print(lst_name)
        user_command_func()
    elif user_command == "show":
        show_name_func(phone_book)
        user_command_func()
    elif user_command == "quit":
        quit()


main()
