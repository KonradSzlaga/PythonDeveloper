"""
This is my first module
Will be used for practice

"""


def is_string(val):
    """Tu jest opis funkcji"""
    return isinstance(val, str)


def sum_list_elements(lst):
    suma = 0
    for elem in lst:
        suma += elem
    return suma


# print(__name__)

if __name__ == '__main__':
    # tu można dorobić testy jednostkowe
    print(is_string('abc') == True)
    print(is_string(5) == False)
    print(is_string('23432534') == True)

    print(sum_list_elements([1, 2, 3]) == 6)
    print(sum_list_elements([]) == 0)
