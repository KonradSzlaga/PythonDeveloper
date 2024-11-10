# a = 3
# b = 2
# c = 11
# d = 2
# e = 20

list = [3, 2, 11, 2, 20]

print(list)

fruits = ['apple', 'banana', 'cherry']

#własności liczb
#jest uporządkowana
# pozwala przechowywać duplikaty
numbers = [1, 1, 1]
print(numbers)

#pozwala przechowywać elementy różnych typów
numbers = [1, "jeden", True, 0xFF]
print(numbers)

# kazdy element z listy posiada indeks - elementy numerowane od zera
print(numbers[0], numbers[1])
#
#
#usuwanie

print(fruits)
del fruits[0]
print(fruits)

#append dodaje na końcu
#insert tam gdzie wskazemy

fruits.insert(0, 'orange')
print(fruits)


#iterowanie
for i in range(len(fruits)):
    print(fruits[i])
print()

for fruit in fruits:
   print(fruit)









