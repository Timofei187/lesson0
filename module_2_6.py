print('Добро пожаловать в игру Крестики-Нолики')
area = ['*', '*', '*', '*', '*', '*','*', '*', '*']
players = ['Крестики', 'Нолики']
chars_ = ['X', '0']


def draw_area(board):
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")

def check_winner():
    combinations = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in range(len(chars_)):
        for j in combinations:
            if (area[j[0]] == chars_[i]
                    and area[j[1]] == chars_[i]
                    and area[j[2]] == chars_[i]):
                print("Победили ", chars_[i])
                return True
    return False

def my_check_input(command):

    user_input = input(command)
    if user_input.isdigit():
        correct_input = int(user_input)
        if correct_input in range(1, 4):
            return correct_input
    else:
        print('=== Вводите только цифры ===')
        return my_check_input(command)

    print('=== Вводите только цифры от 1 до 3 ===')
    return my_check_input(command)

def do_turn(index_):
    num = my_check_input('Введите номер строки ')
    col = my_check_input('Введите номер столбца ')
    position = calc_position(num, col)
    # print(position)
    if right_turn(position):
        # print(area[position])
        area[position] = chars_[index_]
        draw_area(area)
    else:
        print('=== Позиция уже занята. Повторите ввод ===')
        return do_turn(index_)

def calc_position(num, col):
    position = ((num - 1) * 3) + col - 1
    return position

def right_turn(position):
    if area[position] == '*':
        return True
    return False

def main():
    turns_left = 9
    is_first_player_turn = True
    draw_area(area)
    while turns_left>0:
        if is_first_player_turn:
            index = 0
        else:
            index = 1
        print("Ход делают", players[index])
        do_turn(index)
        turns_left -= 1
        is_first_player_turn = not is_first_player_turn
        if check_winner():
            break
        if turns_left == 0:
            print('Ничья')
            break

main()