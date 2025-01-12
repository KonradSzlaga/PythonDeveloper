# Napisz program zliczający punkty w grach (karcianych, planszowych itp.), realizujący:
# • definiowanie liczby oraz imion graczy,
# • definiowanie liczby punktów potrzebnych do wygranej,
# • pobieranie informacji o zdobytych punktach w każdej turze gry,
# • wyświetlanie informacji o zwycięzcy oraz zdobytych punktach poszczególnych graczy.


def podaj_gracza(numer_gracza):
    punkty_gracza = []
    imie_gracza = input('Podaj imię {} gracza: '.format(numer_gracza))
    return {imie_gracza: punkty_gracza}

def podaj_graczy():
        gracze = {}
        ilosc_graczy = int(input('Podaj ilosc graczy (od 1 do 8): '))
        for i in range(ilosc_graczy):
         #   gracz = podaj_gracza(i + 1)
         #   gracze.update(gracz)
            gracze.update(podaj_gracza(i + 1))
        return gracze

def podaj_punkty():
    return(int(input('Podaj ilość punktów wymaganych do wygranej: ')))

def czy_wygral(gracze, wymagane_punkty):
    for gracz in gracze.keys():
        if sum(gracze[gracz]) >= wymagane_punkty:
            return True
    return False


def licz_punkty(gracze, wymagane_punkty):
    tura_gry = 1
    while True:
        print("\nTura:", tura_gry)
        for gracz in  gracze.keys():
            punkty_gracza = int(input('Podaj punkty dla gracza {}: '.format(gracz)))
            gracze[gracz].append(punkty_gracza)
            if czy_wygral(gracze, wymagane_punkty):
                return gracz
        tura_gry += tura_gry

    return 'Zwycięzca!!'


def pokaz_rezultat(gracze, zwyciezca):
    print('Wygrał gracz o imieniu {}'.format(zwyciezca))
    print()
    print('Szczegółowa tabela wyników:')
    for gracz, punkty_gracza in gracze.items():
        print(gracz, "-->", punkty_gracza)



gracze = podaj_graczy()
wymagane_punkty = podaj_punkty()

wygrany = licz_punkty(gracze, wymagane_punkty)
pokaz_rezultat(gracze, wygrany)
