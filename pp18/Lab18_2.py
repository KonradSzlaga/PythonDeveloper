def count_letters(strng):
    chars = []
    dic = {}
    for char in strng:
        if char not in chars:
            chars.append(char)

    for chr in chars:
        ilosc = strng.count(chr)
        dic.update({chr: ilosc})

    return dic

print(count_letters('abracadabra'))