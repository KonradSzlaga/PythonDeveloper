#

number = int(input("Wprowadź liczbę: "))
nbit = int(input("Wprowadź numer bita, w liczbie, który chcesz sprawdzić: : "))

#mask
mask = 1 << nbit
result = number & mask
bit = int(bool(result))

print("Bit na pozycji n-tej, ma wartość " + str(bit) + ".")


#sprawdzenie
print("{:08b}".format(number))

print("-" * 8)

print("{:08b}".format(mask))

print(result)