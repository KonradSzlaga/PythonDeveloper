import random as rd


def decide_on_numbers():
    number_of_balls = 0
    counter = 1
    while counter <= 1:
        try:
            nob = int(input("Wprowadź liczbę za zakresu od 6 do 12. Liczba ta będzie determinować ile numerów wylosuje maszyna i ile num,erów będziesz musiał(a) podać Ty: "))

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


def draft_numbers(number_of_balls):
    """This function returns a list of numbers drafted by a machine."""
    drafted_numbers = []
    drafted_numbers = rd.sample(range(1, 50), number_of_balls)
    return drafted_numbers

def users_numbers(number_of_balls):
    """This function returns a list of numbers provided by a user."""
    user_numbers = []
    counter = 1
    while counter <= number_of_balls:
        try:
            number = int(input("Wprowadź {} liczbę za zakresu od 1 do 49: ".format(counter)))

            if number in user_numbers:
                print("Podana liczba już została wylosowana, spróbuj ponownie.")
                continue

            if number < 1 or number > 49:
                print("Ta liczba nie jest w porządanym zakresie.")
                continue
            user_numbers.append(number)
            counter += 1
        except:
            print("To nie jest liczba. Spróbuj ponownie.")
            continue

    return user_numbers





def compare_numbers(drafted_numbers, user_numbers):
    """This function checks how many numbers match."""
    counter = 0
    matching_list = []
    for number in user_numbers:
       if number in drafted_numbers:
            counter += 1
            matching_list.append(number)

    return {"scalar": counter, "list": matching_list}


if __name__ == '__main__':

    balls_to_draw = decide_on_numbers()
    print(balls_to_draw)



    lucky_numbers = draft_numbers(balls_to_draw).sort()
    print(lucky_numbers)

    user_number = users_numbers(balls_to_draw).sort()
    print(user_number)

    results = compare_numbers(lucky_numbers, user_number)
    print(results)

















