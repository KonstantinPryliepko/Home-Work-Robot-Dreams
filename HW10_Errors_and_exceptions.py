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


def main():
    phone_book = {}
    while len(phone_book) < 2:
        input_func(phone_book)
    print(phone_book)

    end_variable = True
    while end_variable:
        user_command = user_command_func()

        if user_command == "stats":
            print(len(phone_book))
        elif user_command == "add":
            input_func(phone_book)
            print(phone_book)
        elif user_command == "delete":
            update_phone_book = delete_func(phone_book)
            print(update_phone_book)

        elif user_command == "list":
            lst_name = []
            for key in phone_book.keys():
                lst_name.append(key)
            print(lst_name)

        elif user_command == "show":
            show_name_func(phone_book)
        elif user_command == "quit":
            end_variable = False
            quit()


main()
