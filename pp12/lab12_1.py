def printer(char = 'a', how_many = 10, how = 'horizontal'):
    if how == 'horizontal':
        print(char * how_many)
    elif how == 'vertical':
        for i in range(how_many):
            print(char)
    else:
        print('Argument "how" powinien być określony jako "horizontal" lub "vertical".')

printer(how = 'gg')