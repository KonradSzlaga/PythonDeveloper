# Napisz skrypt symulujący uproszczone działanie gry losowej "jednoręki bandyta",
# wtym celu:
#  • za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E,
#  • kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
#  • wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
#  • przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
# większą liczbę liter

import random as rd
def bandyta(a = 1):

    litery = ['A', 'B', 'C', 'D', 'E']  #Zmiana potrzebna w celu losowania większej liczby liter

#Potrzeba dodać kolejne wiersze poniżej, żeby losować więcej

    x = rd.choice(litery)
    y = rd.choice(litery)
    z = rd.choice(litery)

    if x == y == z:
        print('Próba nr:', a)
        print(x, y, z)
        return
    else:
        print('Próba nr:', a)
        print(x, y, z)
        a += 1
        bandyta(a)




bandyta()