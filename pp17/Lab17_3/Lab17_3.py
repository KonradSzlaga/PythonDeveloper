import sys

sys.path.append(r"C:\Users\konrad.szlaga\Desktop\packages")

import games

from games import lotto_module as lm



#określenie ile liczb będziemy losować:
ntd = lm.decide_on_numbers()



#maszyna losuje liczby
drafted_numbers = lm.draft_numbers(ntd)


print("Numery wylosowane przez system, to:", drafted_numbers)

#my podajemy liczby
my_numbers = lm.users_numbers(ntd)



print("Numery wylosowane przez system, to: ", end = "\n")
print(*drafted_numbers, sep = ", ")
print()
print("Numery podane przez Ciebie, to: ", end = "\n")
print(*my_numbers, sep = ", ")
print()
print("Ilość trafionych numerów to: ", lm.compare_numbers(drafted_numbers, my_numbers)['scalar'], sep = '\n')
print()
print("Trafione numery, to: ", end = "\n")
print(*lm.compare_numbers(drafted_numbers, my_numbers)['list'], sep = ", ")

