#Wyświetl wszysytkie cyfry

#While

i = 0
while i < 10:
    print(i, end = " ")
    i +=  1
else:
    print("Zakończono.")

#For

for i in range(0, 10):
    print(i, end = " ")
else:
    print("Zakończono.")

for i in range(10):
    print(i, end = " ")
else:
    print("Zakończono.")

for i in range(0, 10, 1):
    print(i, end = " ")
else:
    print("Zakończono.")

#Wartości ujemne
for i in range(9, -1, -1):
    print(i, end = " ")
else:
    print("Zakończono.")


#Silnia
#3! = 1 * 2 * 3 = 6

number = 5

factorial = 1

#For
for i in range(1, number + 1):
        factorial *= i #factorial = factorial * i
else:
    print(factorial)

#While - nie działa

number = 5
while number:
    factorial *= number  # factorial = factorial * number
    number -= 1

else:
    print(factorial)




for i in range(5):
    print(i)
    if i == 3 :
        break
else:
    print("koniec pętli.")







