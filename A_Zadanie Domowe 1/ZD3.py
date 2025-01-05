kapital = 30_000
r1 = 1 #roczna kapitalizacja odsetek
r2 = 4 #kwartalna kapitalizacja odsetek

#Oprocentowanie roczne -> wartość w stringu
or_string_1 = "7,5%"
or_string_2 = "8,0%"
or_string_3 = "8,25%"


#Oprocentowanie roczne -> wartość do mnożenia
or1 = 1.075
or2 = 1.08
or3 = 1.0825

#rzeczywiste oprocentowanie kwartalne

ok1 = 1+ ((or1 -1) /r2)
ok2 = 1+ ((or2 -1) /r2)
ok3 = 1+ ((or3 -1) /r2)

#print(ok1)
#print(ok2)
#print(ok3)



#kapitalizacja roczna
print("Stan konta w przypadku rocznej kapitalizacji odsetek, dla kapitału własnego w wysokości 30 000 zł i oprocentowania rocznego w wysokości", or_string_1, "wynosi:", kapital*or1, "zł.")
print("Stan konta w przypadku rocznej kapitalizacji odsetek, dla kapitału własnego w wysokości 30 000 zł i oprocentowania rocznego w wysokości", or_string_2, "wynosi:", round(kapital*or2,1), "zł.")
print("Stan konta w przypadku rocznej kapitalizacji odsetek, dla kapitału własnego w wysokości 30 000 zł i oprocentowania rocznego w wysokości", or_string_3, "wynosi:", kapital*or3, "zł.\n")




print("Stan konta w przypadku kwartalnej kapitalizacji odsetek, dla kapitału własnego w wysokości 30 000 zł i oprocentowania rocznego w wysokości", or_string_1, "wynosi:")
print("Po 1 kwartale:", round(kapital * ok1 ** 1, 2))
print("Po 2 kwartale:", round(kapital * ok1 ** 2, 2))
print("Po 3 kwartale:", round(kapital * ok1 ** 3, 2))
print("Po 4 kwartale:", round(kapital * ok1 ** 4, 2), "\n")

print("Stan konta w przypadku kwartalnej kapitalizacji odsetek, dla kapitału własnego w wysokości 30 000 zł i oprocentowania rocznego w wysokości", or_string_2, "wynosi:")
print("Po 1 kwartale:", round(kapital * ok2 ** 1, 2))
print("Po 2 kwartale:", round(kapital * ok2 ** 2, 2))
print("Po 3 kwartale:", round(kapital * ok2 ** 3, 2))
print("Po 4 kwartale:", round(kapital * ok2 ** 4, 2), "\n")

print("Stan konta w przypadku kwartalnej kapitalizacji odsetek, dla kapitału własnego w wysokości 30 000 zł i oprocentowania rocznego w wysokości", or_string_3, "wynosi:")
print("Po 1 kwartale:", round(kapital * ok3 ** 1, 2))
print("Po 2 kwartale:", round(kapital * ok3 ** 2, 2))
print("Po 3 kwartale:", round(kapital * ok3 ** 3, 2))
print("Po 4 kwartale:", round(kapital * ok3 ** 4, 2), "\n")

print("Roczny zysk dla rocznej kapitalizacji  odsetek wynosi:")
print( (kapital * or1) - (kapital), " zł, w przypadku rocznej kapitalizacji odsetek w wysokości ", or_string_1,".", sep = "")
print( round((kapital * or2) - (kapital),1), " zł, w przypadku rocznej kapitalizacji odsetek w wysokości ", or_string_2,".", sep = "")
print( (kapital * or3) - (kapital), " zł, w przypadku rocznej kapitalizacji odsetek w wysokości ", or_string_3,".\n", sep = "")

print("Roczny zysk dla kwartalnej kapitalizacji  odsetek wynosi:")
print( round( (kapital * ok1 ** 4) - kapital, 2),  " zł, w przypadku rocznej kapitalizacji odsetek w wysokości ", or_string_1,".", sep = "")
print( round( (kapital * ok2 ** 4) - kapital, 2),  " zł, w przypadku rocznej kapitalizacji odsetek w wysokości ", or_string_2,".", sep = "")
print( round( (kapital * ok3 ** 4) - kapital, 2),  " zł, w przypadku rocznej kapitalizacji odsetek w wysokości ", or_string_3,".", sep = "")




