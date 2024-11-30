
import random as rd

from pyexpat import features

digits = []
zakres = 15
for i in range(zakres):
    digits.append(rd.randint(0,9))

print(digits)

frequency = []
j = 0
while j < 10 :
    frequency.append(0)
    j += 1
print(frequency)

for digit in digits:
    frequency[digit] += 1

print(frequency)


most_frequent = 0

for i in range(len(frequency)):
    if frequency[i] > frequency[most_frequent]:
        most_frequent = i


print(most_frequent)

print('Najczęściej występująca wartość to', str(most_frequent) + '.')
print('Występuje ona', frequency[most_frequent], 'razy.')












