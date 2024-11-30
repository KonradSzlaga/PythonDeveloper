#robię pustą listę

imiona_lista = []

ilosc_imion = int(input('Podaj ilość imion, które chces wprowadzić: '))

for i in range(ilosc_imion):
        imiona_lista.append(input('Podaj ' + str(i + 1) + ' imię: '))

print('Imiona podane przez użytkownika to:',imiona_lista)