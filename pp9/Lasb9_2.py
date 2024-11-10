

# 2. Napisz program, który zasymuluje 16 rzutów kostką do gry a następnie
# wyświetli poniższe informacje:
# • zestaw wylosowanych wyników,
# • wyrzucaną wartość za 8 razem,
# • liczbę wyrzuconych szóstek,
# • maksymalną liczbę wyrzuconych tych samych wartości pod rząd.

import random as rd

tabela = []
for i in range(16):
    tabela.append(rd.randint(1, 6))
print("RTabela z wylosowanymi wynikami to:", tabela)
print("Wyrzucona wartość przy rzucie za 8 razem to:", tabela[7])

counter = 0
for i in range(len(tabela)):
    if tabela[i] == 6:
        counter += 1

print("Ilość wyrzuconych szóstek to:", counter )

counter = 0
lista = []

for i in range(len(tabela) - 1):
    if tabela[i] == tabela[i + 1]:
        counter += 1
        lista.append(counter)
    else:
        counter = 0

powtorzenia = lista.sort()
x = len(lista)
#print(x)
#print(lista)
print("maksymalna ilość tych samych wartości wyrzuconych pod rząd to:", str((lista[x-1])+1))


#DOPISAC JESZCZE TABLIOCE KTORA PRZECHOWUJE INFORMACJE O TYM JAKA LICZBA ZOSTAŁA NAJCZESCIEJ WYRZUCONA POD RZAD


#