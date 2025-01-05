# Napisz skrypt symulujący rozgrywkę gry w szachy, w tym celu:
#  • stwórz wirtualną szachownicę,
#  • na wirtualnej szachownicy rozmieść losowo 2. dowolne figury szachowe i 3. piony,
#  • zaprezentuj użytkownikowi stan wirtualnej szachownicy.

# Wirtualna szachownica
# Rozmieszczenie pionów
# Wyświetlenie

import random as rd

blank_square = "--"
Pieces = ["wp", "bp", "bt", "bt", "wq"]

chess_board = [[blank_square for _ in range(8)] for _ in range(8)]

counter = 0

while counter < len(Pieces):
    row = rd.randint(0, 7)
    col = rd.randint(0, 7)
    if chess_board[row][col] == blank_square:
        chess_board[row][col] = Pieces[counter]
        counter += 1

for row in range(len(chess_board)):
    for col in range(len(chess_board[row])):
        print(chess_board[row][col], end=" ")
    print()
