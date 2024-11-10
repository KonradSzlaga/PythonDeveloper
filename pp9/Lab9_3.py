# 3. Napisz skrypt, który znajdzie najczęściej występującą cyfrę w zbiorze.
# Np. w zbiorze [4, 1, 2, 9, 4, 4] najczęściej występującą cyfrą jest 4,
# występuje 3 razy

lista = [4, 1, 2, 9, 4, 4]

x = len(lista)
print(x)
liczna = []
ilosc = []


for i in range(0, x-1):
    val = lista[i]
    counter = 0
    for j in range(0, i-1):
        if i == j:
            counter += 1
