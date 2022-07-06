import random


def field(cells):
    print('\033[33m {}'.format('- ' * 31))
    for i in range(0, 10):
        for j in range(0, 10):
            st = str(cells[j + i * 10])
            if st == 'X' or st == 'O':
                print(' |', end='')
                print('\033[37m {:^3}'.format(st), end='')
                print('\033[33m', end='')
            else:
                print(' |', f'{st:^3}', end='')
        print(' |')
        print(' -' * 31)


def check(elem, numm, cells):
    # горизонталь
    line = 1
    for i in range(1, 5):
        if (numm - i) % 10 != 0:
            if cells[numm - i - 1] == elem:
                line += 1
            else:
                break
        else:
            break
    for i in range(1, 5):
        if (numm + i) % 10 != 1:
            if cells[numm + i - 1] == elem:
                line += 1
            else:
                break
        else:
            break
    if line >= 5:
        return True

    # вертикаль
    line = 1
    for i in range(10, 50, 10):
        if numm - i > 0:
            if cells[numm - i - 1] == elem:
                line += 1
            else:
                break
        else:
            break
    for i in range(10, 50, 10):
        if numm + i < 101:
            if cells[numm + i - 1] == elem:
                line += 1
            else:
                break
        else:
            break
    if line >= 5:
        return True

    # левая диагональ
    line = 1
    for i in range(9, 45, 9):
        if numm - i > 0 and (numm - i) % 10 != 1:
            if cells[numm - i - 1] == elem:
                line += 1
            else:
                break
        else:
            break
    for i in range(9, 45, 9):
        if numm + i < 101 and (numm + i) % 10 != 0:
            if cells[numm + i - 1] == elem:
                line += 1
            else:
                break
        else:
            break
    if line >= 5:
        return True

    # правая диагональ
    line = 1
    for i in range(11, 55, 11):
        if numm - i > 0 and (numm - i) % 10 != 0:
            if cells[numm - i - 1] == elem:
                line += 1
            else:
                break
        else:
            break
    for i in range(11, 55, 11):
        if numm + i < 101 and (numm + i) % 10 != 1:
            if cells[numm + i - 1] == elem:
                line += 1
            else:
                break
        else:
            break
    if line >= 5:
        return True

    return False


print('НАЧИНАЕМ ИГРУ В ОБРАТНЫЕ КРЕСТИКИ-НОЛИКИ :)')
cells = list(range(1, 101))
cellscut = cells.copy()
cellscut1 = cellscut.copy()
cross = 0
print('ПОСМОТРИМ, КТО БУДЕТ ХОДИТЬ ПЕРВЫМ')
print('БРОСАЮ ЖРЕБИЙ')
if((random.randint(1, 2)) == 1):
    print('ВЫ ХОДИТЕ ПЕРВЫМ')
    field(cells)
else:
    print('ВЫ ХОДИТЕ ВТОРЫМ')
    rand = random.randint(1, 100)
    cells[rand - 1] = 'O'
    cellscut.pop(rand - 1)
    cellscut1.pop(rand - 1)
    field(cells)
while cellscut != []:
    while True:
        cross = input('ВВЕДИТЕ НОМЕР ЯЧЕЙКИ: ')
        if not cross.isdigit():
            print('ВЫ ОШИБЛИСЬ! ПОПРОБУЙТЕ ЕЩЕ РАЗ: ')
            continue
        cross = int(cross)
        if cross > 100 or cross < 1 or cells[cross - 1] == 'O' or\
           cells[cross - 1] == 'X':
            print('ВЫ ОШИБЛИСЬ! ПОПРОБУЙТЕ ЕЩЕ РАЗ: ')
        else:
            break
    cells[cross - 1] = 'X'
    field(cells)
    if check('X', cross, cells):
        print('ВЫ ПРОИГРАЛИ')
        break
    cellscut.remove(cross)
    if cross in cellscut1:
        cellscut1.remove(cross)

    while True:
        rand = random.choice(cellscut1)
        cellscut1.remove(rand)
        if check('O', rand, cells):
            if cellscut1 == []:
                break
            else:
                continue
        break

    print('Я ВЫБИРАЮ ЯЧЕЙКУ №', rand)
    cells[rand - 1] = 'O'
    field(cells)
    if check('O', rand, cells):
        print('ВЫ ВЫИГРАЛИ')
        break
    cellscut.remove(rand)

else:
    print('НИЧЬЯ')
