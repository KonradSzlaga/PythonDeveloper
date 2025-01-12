# Napisz funkcję zamieniającą 3 listy na 1 krotkę bez powtarzających się elementów.
# Przykład: [1, 2], [1, 1], [4, 4, 4] -> (1, 2, 4)



def usun_duplikaty_i_scal(source, target):
    for element in source:
        if element not in target:
            target.append(element)


def zmiana_typu(lista1 = [1,1,15], lista2 = [1,2,3,3,58], lista3 = [58,12,69,85]):
    result = []
    usun_duplikaty_i_scal(lista1, result)
    usun_duplikaty_i_scal(lista2, result)
    usun_duplikaty_i_scal(lista3, result)
    return tuple (result)


print(zmiana_typu(lista1 = [1,1,15], lista2 = [1,2,3,3,58], lista3 = [58,12,69,85]))