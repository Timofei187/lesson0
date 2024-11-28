area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
players = ['Крестики', 'Нолики']
chars_ = ['X', '0']
def draw_area():
    for i in area:
        print(*i)

def check_winner():
    combinations = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[2, 0], [1, 1], [0, 2]]
    ]
    for i in range(len(chars_)):
        for j in combinations:
            if (area[j[0][0]][j[0][1]] == chars_[i]
                    and area[j[1][0]][j[1][1]] == chars_[i]
                    and area[j[2][0]][j[2][1]] == chars_[i]):
                print('Победили ', players[i])
                return True
    return False

def my_check_input(command):

    user_input = input(command)
    if not user_input.isdigit():
        print('=== Вводите только цифры ===')
        return my_check_input(command)
    else:
        correct_input = int(user_input)
        if correct_input in range(1,4):
            return correct_input-1
        else:
            print('=== Вводите только цифры от 1 до 3 ===')
            return my_check_input(command)

def do_turn(index):
    num = my_check_input('Введите номер строки ')
    col = my_check_input('Введите номер столбца ')
    if right_turn(num, col):
        area[num][col] = chars_[index]
        draw_area()
    else:
        print('=== Позиция уже занята. Повторите ввод ===')
        return do_turn(index)

def turns_left():
    count_ = 0
    for i in area:
        count_ += i.count('*')
    return count_

def right_turn(num, col):
    if area[num][col] == '*':
        return True
    else:
        return False

print('Добро пожаловать в игру Крестики-Нолики')
draw_area()
while turns_left()>0:
    if check_winner():
        break
    if turns_left() % 2 == 0:
        index = 0
    else:
        index = 1
    print("Ход делают", players[index])
    do_turn(index)
if turns_left() == 0:
        print('Ничья')