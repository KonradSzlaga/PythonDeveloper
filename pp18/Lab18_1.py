alfabet = 'a ą b c ć d e ę f g h i j k l ł m n ń o ó p r s ś t u w y z ź ż'
alfabet = alfabet.replace(' ', '')

for i in alfabet:
    print(i, ord(i))