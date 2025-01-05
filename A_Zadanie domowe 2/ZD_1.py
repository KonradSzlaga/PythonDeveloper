# 1. Napisz program sumujący pobrane liczby od użytkownika wg wytycznych:
# • program powinien pobierać od użytkownika liczby całkowite,
# • niepodanie liczby powinno zakończyć wprowadzanie danych,
# • program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych.


numbers = int(input("Podaj ile liczb chcesz wprowadzić:"))
if numbers == 0:
    print('Widocznie użytkownik nie chce zagrać. Program zakończy działanie')


digits = []
for i in range(numbers):
    print('Podaj', i + 1, 'liczbe: ', end = "")
    liczba = input()

    if len(liczba.strip()) != 0:
        if float(liczba) % 1 == 0:
            digits.append(int(liczba))


        else:
            print('Podana liczbę która nie jest całkowita. Program zakończy działanie')
            break
    else:
        print('Nie wprowadzono żadnej liczby. Program zakończy działanie')
        break

print(digits)


odd_even_sum = [0,0]

for j in range(len(digits)):
    if digits[j] % 2 == 0:
        odd_even_sum[0] += digits[j]
    else:
        odd_even_sum[1] += digits[j]

print('Suma liczb parzystych to:', odd_even_sum[0], 'a nieparzystych to:', odd_even_sum[1] )
