import random as rd


def decide_on_numbers():
    number_of_balls = 0
    counter = 1
    while counter <= 1:
        try:
            nob = int(input("Wprowadź liczbę za zakresu od 6 do 12. Liczba ta będzie determinować ile numerów wylosuje maszyna i ile numerów będziesz musiał(a) podać Ty: "))

            if (nob < 6 or nob > 12):
                print("Podana liczba nie należy do porządanego zakresu")
                continue
            else:
                number_of_balls = nob
                counter += 1
        except:
            print("To nie jest liczba, spróbuj ponownie.")
            continue
    return number_of_balls

print(decide_on_numbers())



def draft_numbers(nob):
    """This function returns a list of numbers drafted by a machine."""
    drafted_numbers = []
    drafted_numbers = rd.sample(range(1, 50), nob)
    return drafted_numbers




balls_to_draw = decide_on_numbers()
print(balls_to_draw)
lucky_numbers = draft_numbers(balls_to_draw).sort()
print(lucky_numbers)