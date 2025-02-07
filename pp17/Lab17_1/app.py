# Stwórz pakiet wraz z subpakietami i modułami wg schematu jak na rysunku
#  a dodatkowo:
#  • w każdym module umieść definicję funkcji fun(),
#  • wspomniana funkcja powinna wyświetlać informacje
#  o funkcji, module oraz pakiecie z jakiego została wywołana,
#  • skrypt app.py powinien wywoływać wszystkie funkcje.

from pack1 import mod1 as m1
from pack1.subpack1 import mod2 as m2
from pack1.subpack2 import mod3 as m3

print()
m1.fun()
print()
m2.fun()
print()
m3.fun()