import random
def solo():
    name = 'User'
    while True:
        position = input('Вы хотите играть за крестики (1) или за нолики(0)?')

        if not (position.isdigit()):
            print(" Введите 0 или 1! ")
            continue

        pos = int(position)

        if pos != 0:
            if pos != 1:
                print(" Введите 0 или 1! ")
                continue

        return name, pos


def start():
    while True:
        m = 1
        n = m
        return n

def instr(name_1, name_2 = None):
    print('Рады преведствовать в игре!')
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

field = [["-"] * 10 for i in range(10) ]

def show():
    print()
    print("    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ")
    print("  ------------------------------------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        # print("  ----------------------------- ")
    print()


def strock(name):
    while True:
        cords = input(f' {name}, Ваш ход: ').split()

        if len(cords) !=2:
            print(' Введите 2 координаты! ')
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(' Введите числа! ')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 9 or 0 > y or y > 9:
            print(' Координаты вне диапазона! ')
            continue

        if field[x][y] != '-':
            print(' Клетка занята! ')
            continue

        return x, y

def computer_move():
    for i in range(9):
        if field[i][0] == field[i][1] == field[i][2] == field[i][3] and field[i][4] == '----':
            return i, 4
        elif field[i][1] == field[i][2] == field[i][3] == field[i][4] and field[i][0] == '----':
            return i, 0
        elif field[i][2] == field[i][3] == field[i][4] == field[i][0] and field[i][1] == '----':
            return i, 1
        elif field[i][3] == field[i][4] == field[i][0] == field[i][1] and field[i][2] == '----':
            return i, 2
        elif field[i][4] == field[i][0] == field[i][1] == field[i][2] and field[i][0] == '----':
            return i, 3

    for i in range(9):
        if field[0][i] == field[1][i] == field[2][i] == field[3][i] and field[4][i] == '----':
            return  4,i
        elif field[1][i] == field[2][i] == field[3][i] == field[4][i] and field[0][i] == '----':
            return  0,i
        elif field[2][i] == field[3][i] == field[4][i] == field[0][i] and field[1][i] == '----':
            return  1,i
        elif field[3][i] == field[4][i] == field[0][i] == field[1][i] and field[2][i] == '----':
            return  2,i
        elif field[4][i] == field[0][i] == field[1][i] == field[2][i] and field[0][i] == '----':
            return  3,i

    for x in range(6):
        if field[x][x] == field[x+1][x+1] == field[x+2][x+2] == field[x+3][x+3] and field[x+4][x+4] == '-':
            return x+4, x+4
        if field[x+1][x+1] == field[x+2][x+2] == field[x+3][x+3] == field[x+4][x+4] and field[x][x] == '-':
            return x, x
        if field[x+2][x+2] == field[x+3][x+3] == field[x+4][x+4] == field[x][x] and field[x+1][x+1] == '-':
            return x+1, x+1
        if field[x+3][x+3] == field[x+4][x+4] == field[x][x] == field[x+1][x+1] and field[x+2][x+2] == '-':
            return x+2, x+2
        if field[x+4][x+4] == field[x][x] == field[x+1][x+1] == field[x+2][x+2] and field[x+3][x+3] == '-':
            return x+3, x+3


    if field[0][4] == field[1][3] == field[2][2] == field[3][1] and field[4][0] == '-':
        return 4, 0
    if field[1][3] == field[2][2] == field[3][1] == field[4][0] and field[0][4] == '-':
        return 0, 4
    if field[0][4] == field[2][2] == field[3][1] == field[4][0] and field[1][3] == '-':
        return 1, 3
    if field[0][4] == field[1][3] ==  field[3][1] == field[4][0] and field[2][2] == '-':
        return 2, 2
    if field[0][4] == field[1][3] == field[2][2] ==  field[4][0] and field[3][1] == '-':
        return 3, 1

    while True:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if field[row][col] == '-':
            return row, col

def check_win():
    for i in range(10):
        for c in range(6):
            symbols = []
            for j in range(c,c+5):
                symbols.append(field[i][j])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True

    for j in range(10):
        for c in range(6):
            symbols = []
            for i in range(c,c+5):
                symbols.append(field[i][j])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True

    for c in range(6):
        symbols = []
        for i in range(c,c+5):
            symbols.append(field[i][i])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True
    for x in range(5):
        for c in range(1,6):
            symbols = []
            for i in range(x,5):
                symbols.append(field[i][i+c])
                if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                    return True
            symbols = []
            for i in range(5):
                symbols.append(field[i+c][i])
                if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                    return True
    for c in range(5):
        symbols = []
        for i in range(5):
            symbols.append(field[c+i][c+1+i])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True
        symbols = []
        for i in range(5):
            symbols.append(field[c+1 + i][c + i])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True

    for x in range(6):
        for y in range(5):
            symbols = []
            for i in range(5):
                symbols.append(field[i + x][y+4 - i])
                if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                    return True

    for x in range(6):
        for y in range(5):
            symbols = []
            for i in range(5):
                symbols.append(field[i + y][x + i])
                if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                    return True


    for с in range(1,6):
        symbols = []
        for i in range(c, c+5):
            symbols.append(field[i][10-i])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True
        symbols = []
        for i in range(c, c + 5):
            symbols.append(field[i][5 - i])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True
        symbols = []
        for i in range(c, c+5):
            symbols.append(field[10-i][i])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True
        symbols = []
        for i in range(c, c + 5):
            symbols.append(field[5 - i][i])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True

    for c in range(6):
        symbols = []
        for i in range(c,c+5):
            symbols.append(field[i][c+4-i])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True
        symbols = []
        for i in range(c,c+5):
            symbols.append(field[i][c - i])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True
        symbols = []
        for i in range(c,c+5):
            symbols.append(field[c+4-i][i])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True
        symbols = []
        for i in range(c,c+5):
            symbols.append(field[c - i][i])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True

    for c in range(5):
        symbols = []
        for i in range(1,6):
            symbols.append(field[i][c + i])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True
        symbols = []
        for i in range(1,6):
            symbols.append(field[c + i][i])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True


    for c in range(5):
        symbols = []
        for i in range(c,c+5):
            symbols.append(field[i][c+5 - i])
            if symbols == ['X', 'X', 'X', 'X', 'X'] or symbols == ['O', 'O', 'O', 'O', 'O']:
                return True
    return False

def solo_play(name, position):
    smb_user = 'X'
    smb_comp = 'O'

    if not position:
        smb_user, smb_comp = smb_comp, smb_user

    count = 0
    while True:
        count += 1
        show()
        if count % 2 == 1:
            if position:
                x, y = strock(name)
                field[x][y] = 'X'
                if check_win():
                    show()
                    print(f' {name} победил! ')
                    break
            else:
                print('Ход компютера:')
                x, y = computer_move()
                field[x][y] = 'X'
                if check_win():
                    show()
                    print(f' Компютер победил! ')
                    break
        else:
            if not position:
                x, y = strock(name)
                field[x][y] = 'O'
                if check_win():
                    show()
                    print(f' {name} победил! ')
                    break
            else:
                print('Ход компютера:')
                x, y = computer_move()
                field[x][y] = 'O'
                if check_win():
                    show()
                    print(f' Компютер победил! ')
                    break

        if count == 100:
            print(" Ничья!")
            break

n = int(start())

if n == 1:
    name, position = solo()
    instr(name)
    solo_play(name,position)
