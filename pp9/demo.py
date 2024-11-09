# temp = 12
# is_sun_shining = False
#
# if temp > 0 and is_sun_shining:
#     print("idziemy na spacer")
# else:
#     print("zostajemy w domu")
#
#
#  #jezeli bedzie ujemna temperatura lub jest pochmurnie to zostaniemy w domu a jezeli nie to
#  #pojdziemy na spacer
#
#
# if not(temp < 0 or not is_sun_shining):
#     print("idziemy na spacer")
# else:
#     print("zostajemy w domu")



#Operatory logiczne:
#and - koniunkcja
#or - alternatywa
#not - negacja

#iterujemny od  do 9 (10) iteracji - wyswietlmy cyfre chyba ze
#bedzie t liczba parzysta lub liczba większa od 6 to wyświetl gwiazdkę

#
# for i in range (10):
#     if i % 2 == 0 or i > 6:
#         print("*")
#     else:
#         print(i)
#

#sprawdzamy czy da sie zrobic trójkąt:
#sprawdzamy jaki to trójkąt ze wzgledu na boki - równo, różno, równoramienny.
#sprawdzamy jaki to trójkąt ze wzgledu na kąty - prostokątny, ostro i rozwartokątny

a = int(input("Podaj długość pierwszzego odcinka: "))
b = int(input("Podaj długość drugiego odcinka: "))
c = int(input("Podaj długość trzeciego odcinka: "))

if (a+b) > c and (a+c) > b and (b+c) > a:
    print("Można zbudować trójkąt.")

    print("Będzie to trójkąt ", end = "")
    if a == b == c:
        print("równoboczny.")
    elif a == b or b == c or c == a:
        print("równoramienny.")
    else:
        print("różnoboczny.")

    if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2):
        print("Będzie to trójkąt prostokątny.")
    elif (a**2 + b**2 > c**2) or (c**2 + b**2 > a**2) or (b**2 + c**2 > a**2):
        print("Będzie to trójkąt ostrokątny.")
    else:
        print("Będzie to trójkąt rozwartokątny.")


else:
    print("Nie można zbudować trójkąta.")

