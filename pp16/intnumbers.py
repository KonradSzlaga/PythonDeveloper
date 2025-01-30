def verint(lst):
    return all(isinstance(i, int) for i in lst)


def sumlst(lst):
    return sum(lst)

def iloczyn(lst):
    result = 1
    for i in lst:
        result *= i
    return result


if __name__ == '__main__':

    print(verint([1,2,3,4,5,6]) == True)
    print(verint([1, 2, 3.2, 4, 5, 6]) == False)

    print(sumlst([1,2,3,4,5,6]) == 21)
    print(sumlst([1,2,3.2,4,5,6]) == 21.2)

    print(iloczyn([1,2,3.2,4,5,6]) == 768.0)

