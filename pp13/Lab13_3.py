# Napisz skrypt symulujący uproszczone działanie gry losowej "jednoręki bandyta",
# wtym celu:
#  • za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E,
#  • kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
#  • wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
#  • przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
# większą liczbę liter

import random as rd
def bandyta(a = 1):
    floor = 1
    ceiling = 6
    odpowiedniki = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E'}

    x = rd.randint(floor, ceiling)
    y = rd.randint(floor, ceiling)
    z = rd.randint(floor, ceiling)

    if x == y == z:
        print('Próba nr:', a)
        print(x, y, z)
        print(odpowiedniki[x], odpowiedniki[y], odpowiedniki[z])
        return
    else:
        print('Próba nr:', a)
        print(x, y, z)
        a += 1
        bandyta(a)




bandyta()