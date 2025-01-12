# Napisz wyszukiwarkę numerów telefonów:
# • zdefiniuj słownik par imię -> numer telefonu,
# • zapytaj użytkownika o imię,
# • wyświetl użytkownikowi numer telefonu lub informację o jego braku.


#Słownik  z numerami telefonów:

numer = {
    "Paweł": 123456789,
    "Łukasz": 987654321,
    "Sylwia": 569874123,
    "Ola": 741258963,
    "Maria": 369874125
}

while True:
    name = input("Podaj imię osoby, dla której chcesz uzyskać numer telefonu: ")
    if name == '':
        break
    if name in numer.keys():
        print('Numer telefonu, którego szukasz to:', numer.get(name))
    else:
        print('Nie znaleziono takiego użytkownika:', name)