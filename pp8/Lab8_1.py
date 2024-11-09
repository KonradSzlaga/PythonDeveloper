i = 1
print("Liczby z zakresu od 1 do 100 z pominięciem tych podzielnych przez 3 to:")

for i in range(1,100):
    if i % 3 == 0:
        continue
    else:
        print(i)
else: print("Zakończono wyświetlanie.")