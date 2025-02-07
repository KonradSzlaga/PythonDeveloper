zmienna = 'VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ'


def decipher(string):
    nowe_slowo = ''
    for litera in string:
        if ord(litera) >= 65 and ord(litera) <= 90:
            x = ord(litera) -3

            if x >= 65 and x <= 90:
                nowe_slowo += chr(x)

            elif x < 65:
                x = 91-(65-x)
                nowe_slowo += chr(x)

            elif x > 90:
                x = 64 + (x - 90)
                nowe_slowo += chr(x)

        else:
            nowe_slowo += litera

    return nowe_slowo


print(decipher(zmienna))