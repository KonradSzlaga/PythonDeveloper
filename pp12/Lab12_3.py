print('Obliczanie wskaźnika BMI')

def parametry():
    waga = float(input('Podaj masę ciała:'))
    wzrost = float(input('Podaj wzrost w cm:')) / 100
    return [waga, wzrost]

def bmi(weight, height):
    return weight / (height ** 2)

dane = []
dane = parametry()

print(dane)


_bmi = (bmi(dane[0], dane[1]))

def determine_category(_bmi):
    if _bmi < 18.5:
        return 'Niedowaga'
    elif 18.5 <= _bmi < 25:
        return 'Norma'
    elif 25 <= _bmi < 30:
        return 'Nadwaga'
    else:
        return 'Otyłość'

category = determine_category(_bmi)

print('Wskaźnik BMI:', _bmi)
print('Kategoria:', category)