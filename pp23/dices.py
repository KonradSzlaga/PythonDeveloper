# Symuluje rzut dwiema koścmi do gry
# rzucamy do momemntu wyrzucenia dubletu:

import random as rd


#Kostaka do gry będzie miała stan - wyrzucona wartość oczek
#Metoda - rzut kostką


class Dice:
    def __init__(self):
        self.value = None

    def dice_throw(self):
        self.value = rd.randint(1,6)

        # pokazuje reprezentacje dla obiektu jako ciąg znaków:
    def __str__(self):
        return f"[{self.value}]"  # [1], etc - wyrucona wartość dla kości







# stan dwóch kostek
# rzut dwiema koścmi

class DicePair:
    def __init__(self):
        self.pair = [Dice(), Dice()]    # Parametr to lista dwóch obiektów

# Ta metoda wywołuje metodę dice_throw() dla kalsy Dice. Robi to 2 razy bo mamy 2 obiekty w liście pair[]
    def dices_throw(self):
        self.pair[0].dice_throw()
        self.pair[1].dice_throw()

    def __str__(self):
        #return f"[{self.pair[0].value}][{self.pair[1].value}]"  #Można zapisać tak
        return str(self.pair[0]) + str(self.pair[1])          #"__str__" "wywoływana jest albo w funkcji print albo w funkcji string

    def is_double(self):
        return self.pair[0].value == self.pair[1].value


dices = DicePair()
counter = 0
while True:
    dices.dices_throw()
    print(dices)
    counter += 1

    if dices.is_double():
        print(f"Ilość rzutów potrzeban do wylosowania dubletu: {counter}.")
        break
