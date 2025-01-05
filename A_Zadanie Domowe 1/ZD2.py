rozmiar = "13TB"
rozmiar_w_MB = 13 * 1024 *1024
predkosc_pobierania_MB_s = 194 / 5

#print(rozmiar_w_MB)
#print(predkosc_pobierania_MB_s)

czas_pobierania_s = rozmiar_w_MB / predkosc_pobierania_MB_s
czas_pobierania_h = round(czas_pobierania_s / 3600,0)

print("Czas pobierania pliku o rozmiarze ", rozmiar, "to: ", czas_pobierania_h, "godzin.")



