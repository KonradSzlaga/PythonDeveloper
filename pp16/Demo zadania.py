import math as m
import sys
import random
from random import choice, sample

# print(m.pi)
# print(m.sin(m.pi / 2))
#
# print(m.factorial(10))
# print(m.floor(4.99999))
# print(m.ceil(4.00000001))
# print(m.tan(m.pi / 3))
# print(m.tan(0))
# print(m.tan(259))



#help(random)

#choice - wybiera jedną wartość ze zbioru
lst = [i for i in range(1,11)]

print(choice(lst))


#sample - wybiera kilak elementów ze zbioru - bez powtórzeń

print(sample(lst,5))

