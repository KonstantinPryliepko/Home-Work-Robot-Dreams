# Required Task
def uniq_elements_func(first_lst, second_lst):
    uniq_elements = set(first_lst).symmetric_difference(set(second_lst))
    return uniq_elements


def same_elements_func(first_lst, second_lst):
    same_elements = set(first_lst).intersection(set(second_lst))
    return same_elements


# Oprional Task
def uppercase_func(elements):
    uppercase_elements = elements.upper()
    return uppercase_elements


def numb_elements_func(elements):
    return isinstance(elements, int)


def main():

# Required Task

    first_lst = [1, 2, 3, 4, 5, 6, 7]
    second_lst = [5, 6, 7, 8, 9, 10]
    same_elements = same_elements_func(first_lst, second_lst)
    print(same_elements)

    uniq_elements = uniq_elements_func(first_lst, second_lst)
    print(uniq_elements)


# Oprional Task
# 1
    strng_elements = "kukusiki"
    new_strng_elements = ""
    print(strng_elements)
    for elem in map(uppercase_func, strng_elements):
        new_strng_elements += elem
    print(new_strng_elements)
# 2
    elements = ["asad", [1, 2, 4], "xoxoxoxo", 9, 8, "asad", 7, 0, "asad", 0]
    numb_elements = []
    for elem in filter(numb_elements_func, elements):
        numb_elements.append(elem)
    print(numb_elements)


main()
