print('*********************************************************')
print('****************  Игра Крестики-нолики  *****************')
print('********************  Правила игры  *********************')
print('* Игроки по очереди ставят на свободные клетки поля 3х3 *')
print('**  знаки (один всегда крестики,другой всегда нолики). **')
print('* Первый, выстроивший в ряд 3 своих фигуры по вертикали *')
print('********* горизонтали или диагонали,выигрывает. *********')
print('** Игрок №1 может выбирать, какой фигурой будет играть **')
print('*********************************************************'"\n")

VERTICAL_COORDINATS = ('a', 'b', 'c')  # Записываем координаты по Y, чтобы преоброзовывать при вводе в цифры

def get_user_char():
    one_user_char = input('Выберите x или 0: ').strip(' ').lower()  # Игрок 1 выбирает каким символом он будет играть Х или 0
    while one_user_char not in ('x', '0'):  # Пока игрок не выбирет х или 0 игра просит повторно ввести значение
        print('Вы выбрали не существующий игровой символ')
        one_user_char = input('Выберите x или 0 еще раз: ').strip(' ').lower()
    return one_user_char  # Если введено все правильно возвращаем то что ввел игрок 1

def show_field(field): # Функция для вывода игрового поля
    print(' ', '1', '2', '3')
    for y,v in enumerate(VERTICAL_COORDINATS):
        print(v, ' '.join(field[y]))

def is_draw(field):#Функция для проверки ничьей
    count = 0
    for y in range(3):
        count += 1 if '-' in field[y] else 0#Будем увеличивать count если такие символы есть в нашей строке или 0 если не содержится
    return count == 0#Если мы не нашли ни одного символа в стоках значит count == 0, значит ничья

def get_one_user_position(field):#Проверяем после ввода координат свободна данная ячейка или нет
    real_x, real_y = 0, 0
    while True:
        print('Ходит игрок №1')
        print("""Пример ввода координат 'a 1'. """)
        coordinats = input('Введите координаты через пробел: ').lower().split()
        if len(coordinats) != 2:
            print("Ошибка ввода")
            continue
        y, x = coordinats  # Преобразуемый полченные координаты
        if not (x.isdigit()):
            print("Ошибка ввода")
            continue
        if int(x) not in ( 1, 2, 3) or y not in VERTICAL_COORDINATS:  # Если полученный х не равен 1,2,3 или у нету в списки координат
            print('Такие координаты не существуют!')
            continue
        real_y, real_x = VERTICAL_COORDINATS.index(y), int(x) - 1  # Проверяеи координаты
        if field[real_y][real_x] == '-':
            break
        else:
            print('Это место занято другим символом!')
            continue

    return  real_y, real_x

def get_two_user_position(field):#Проверяем после ввода координат свободна данная ячейка или нет
    real_x, real_y = 0, 0
    while True:
        print('Ходит игрок №2')
        print("""Пример ввода координат 'a 1'. """)
        coordinats = input('Введите координаты через пробел: ').lower().split()
        if len(coordinats) != 2:
            print('Ошибка ввода')
            continue
        y, x = coordinats# Преобразуемый полченные координаты
        if not(x.isdigit()):
            print('Ошибка ввода')
            continue
        if int(x) not in (1, 2, 3) or y not in VERTICAL_COORDINATS:#Если полученный х не равен 1,2,3 или у нету в списки координат
            print('Такие координаты не существуют!')
            continue

        real_y, real_x  = VERTICAL_COORDINATS.index(y), int(x)-1 #Проверяеи координаты
        if field[real_y][real_x] == '-':
            break
        else:
            print('Это место занято другим символом!')
            continue
    return  real_y, real_x

def get_opponent_char(char):
    return '0' if char == 'x' else 'x'

def is_win(char,field):# Проверяем строки, колоннки и диагонали
    opponent_char = get_opponent_char(char)
    for y in range(3):
        if opponent_char not in field[y] and '-' not in field[y]:
            return True
        col = [field[0][y], field[1][y], field[2][y]]
        if opponent_char not in col and '-' not in col:
            return True
    for x in range(3):
        col = [field[0][x], field[1][x], field[2][x]]
        if opponent_char not in col and '-' not in col:
            return True
        diagonal = [field[0][0], field[1][1], field[2][2]]
        if opponent_char not in diagonal and '-' not in diagonal:
            return True
        diagonal = [field[0][2], field[1][1], field[2][0]]
        if opponent_char not in diagonal and '-' not in diagonal:
            return True
        return False

field = [['-' for y in range(3)] for x in range(3)]  # Генерируем таблицу 3х3

one_user_char = get_user_char()  # Сохраняем символ для 1 игрока
two_user_char = get_opponent_char(one_user_char) #Задаем символ для 2 игрока исходя из того какой символ остался
def game(): # Игра
    while True: # Игровой цикл
        show_field(field)#Вызываем функцию игрового поля
        y, x = get_one_user_position(field)#Просим игрока ввести координаты
        field[y][x] = one_user_char

        if is_win(one_user_char, field):# Проверяем состояние поля на победу одного из игроков
            show_field(field)
            print('Вы выиграли')
            break
        if is_draw(field):#Если ничья
            show_field(field)  # Вызываем функцию игрового поля
            print('Ничья')
            break
        show_field(field)
        y, x = get_two_user_position(field)  # Просим игрока ввести координаты
        field[y][x] = two_user_char
        if is_win(two_user_char, field):  # Проверяем состояние поля на победу одного из игроков
            show_field(field)
            print('Вы выиграли')
            break
        if is_draw(field):#Если ничья
            show_field(field)  # Вызываем функцию игрового поля
            print('Ничья')
            break
while True:
    game()
    new_game = input('Хотите сыграть ещё раз?\nДля продолжения введите "G", для выхода нажмите "Enter"\n')
    if not new_game:
        print('До скорых встреч!')
        break
    else:
        field = [['-' for y in range(3)] for x in range(3)]
        one_user_char = get_user_char()  # Сохраняем символ для 1 игрока
        two_user_char = get_opponent_char(one_user_char)  # Задаем символ для 2 игрока исходя из того какой символ остался




