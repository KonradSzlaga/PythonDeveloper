# Napisz program zliczający punkty w grach (karcianych, planszowych itp.), realizujący:
# • definiowanie liczby oraz imion graczy,
# • definiowanie liczby punktów potrzebnych do wygranej,
# • pobieranie informacji o zdobytych punktach w każdej turze gry,
# • wyświetlanie informacji o zwycięzcy oraz zdobytych punktach poszczególnych graczy.


def podaj_gracza(numer_gracza):
    punkty_gracza = []
    imie_gracza = input('Podaj imię {} gracza: '.format(numer_gracza))
    return {imie_gracza, punkty_gracza}

def podaj_graczy():
        gracze = {}
        ilosc_graczy = int(input('Podaj ilosc graczy (od 1 do 8): '))
        for i in range(ilosc_graczy):
            gracz = podaj_gracza(i + 1)
            gracze.update({i + 1 : gracz})
        return gracze

players = podaj_graczy()
print(players)