#szyfr
#dla każdego znaku zmieniono czwarty bit na przeciwny - od najmniej znaczącego

msg = "Xq|`gf(bm{|(nibfq)"

#funkcja - pokazuje numer znaku w systemie z ztabeli ASCII
print(ord("c"))

#W drugą stronę
print(chr(99))

print("{:08b}".format(ord("c")))
#01100011 -> chcemy zmienić czwarty bit od pawej
#00001000 Maskowanie - pozwala wyizolować wskazany bit - uzyskujemy ją jako 1 << 3
# użyjemy alternatywy rozłącznej - XOR
# chcemy 01101011 -> docelowe


print("{:08b}".format(ord("c") ^ (1 << 3)))

for c in msg:
    n = ord(c) ^ (1 << 3)
    print(chr(n), end = "")