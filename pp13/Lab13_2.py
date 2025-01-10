#Korzystając z rekurencji wypisz na ekranie tabliczkę mnożenie do 100.


def tab_mnozenia():

    for x in range(1,11):
        for i in range(1,11):
            print(x, 'X', i, '=',x * i,)
        print("")
        x += 1
        if x > 10:
            return
    tab_mnozenia()


tab_mnozenia()