i = 1
s = 1

while i <= 64:
    s *= 2
    i += 1
else:
    print("Wynik to", s - 1, "ziaren.")

#Waga jedngo ziarna to 0,4mg ~ 0,0004g
kg = 0.0004


print(s * kg)