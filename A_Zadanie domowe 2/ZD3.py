# 3. Napisz program pobierający od użytkownika liczbę całkowitą i zwracający
# liczbę jedynek w ciągu bitów reprezentujących tę liczbę.



liczba = int(input('Podaj liczbę:'))

binary = bin(liczba)
print('Zapis binarny to:', bin(liczba))
binarnie = str(binary).count('1')


print('Liczba jedynek w zapisie binarnym reprezentującym podaną liczbę to', str(binarnie) + '.')