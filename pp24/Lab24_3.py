class Osoba:
    def __init__(self, imie):
        self.imie = imie

    def __str__(self):
        return f"Imię: {self.imie}"


class ZwyklaOsoba(Osoba):
    def __init__(self, imie):
        super().__init__(imie)


class Pracownik(Osoba):
    def __init__(self, imie, wynagrodzenie):
        super().__init__(imie)
        self.wynagrodzenie = wynagrodzenie

    def __str__(self):
        return super().__str__() + f", Wynagrodzenie: {self.wynagrodzenie}"


class Menedzer(Pracownik):
    def __init__(self, imie, wynagrodzenie, projekt):
        super().__init__(imie, wynagrodzenie)
        self.projekt = projekt

    def __str__(self):
        return super().__str__() + f", Projekt: {self.projekt}"


# Tworzenie listy osób
osoby = [
    ZwyklaOsoba("Paweł"),
    Pracownik("Ola", 5000),
    Menedzer("Łukasz", 10000, "Projekt Manhattan")
]

# Wyświetlanie informacji o osobach
for osoba in osoby:
    print(osoba)