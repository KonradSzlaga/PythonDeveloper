#Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.

def potega():
    lista = [1,2,3,4,5,6,7,8,9,10]
    print("Lista zawiera elementy:", lista)
    x = int(input("Podaj potęgę, do której podnieść wszystkie elementy listy: "))

    lista2 = []

    for i in range(len(lista)):
        y = lista[i] ** x
        lista2.append(y)

    print("Lista po podniesieniu elementów do potęgi", x, "zawiera elementy:", lista2)

potega()