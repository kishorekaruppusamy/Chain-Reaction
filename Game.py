board_Count = [[0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]

board_Player = [['0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0']]

Display_Box = [['0', '0', '0', '0', '0'],
               ['0', '0', '0', '0', '0'],
               ['0', '0', '0', '0', '0'],
               ['0', '0', '0', '0', '0'],
               ['0', '0', '0', '0', '0']]


# mapping 1d elements to 2d elements
def mapper(num):
    if num == 0:
        return 0, 0
    elif num == 1:
        return 0, 1
    elif num == 2:
        return 0, 2
    elif num == 3:
        return 0, 3
    elif num == 4:
        return 0, 4
    elif num == 5:
        return 1, 0
    elif num == 6:
        return 1, 1
    elif num == 7:
        return 1, 2
    elif num == 8:
        return 1, 3
    elif num == 9:
        return 1, 4
    elif num == 10:
        return 2, 0
    elif num == 11:
        return 2, 1
    elif num == 12:
        return 2, 2
    elif num == 13:
        return 2, 3
    elif num == 14:
        return 2, 4
    elif num == 15:
        return 3, 0
    elif num == 16:
        return 3, 1
    elif num == 17:
        return 3, 2
    elif num == 18:
        return 3, 3
    elif num == 19:
        return 3, 4
    elif num == 20:
        return 4, 0
    elif num == 21:
        return 4, 1
    elif num == 22:
        return 4, 2
    elif num == 23:
        return 4, 3
    else:
        return 4, 4


def red_play_first(row, col):
    board_Player[row][col] = 'R'
    board_Count[row][col] += 1
    return 'green'


def red_play(row, col):
    if board_Player[row][col] == 'R' or board_Player[row][col] == '0':
        board_Player[row][col] = 'R'
        board_Count[row][col] += 1
        split_Check(row, col)
        check_val = win_check()
        if check_val == 'red-win':
            return 'Red'
        return 'green'
    else:
        return 'red'


def green_play(row, col):
    if board_Player[row][col] == 'G' or board_Player[row][col] == '0':
        board_Player[row][col] = 'G'
        board_Count[row][col] += 1
        split_Check(row, col)
        check_val = win_check()
        if check_val == 'green-win':
            return 'Green'
        return 'red'
    else:
        return 'green'


# function to check the four edges
def edge_check():
    if board_Count[0][0] == 2:
        Split(0, 0, board_Player[0][0])
    elif board_Count[0][4] == 2:
        Split(0, 4, board_Player[0][4])
    elif board_Count[4][0] == 2:
        Split(4, 0, board_Player[4][0])
    elif board_Count[4][4] == 2:
        Split(4, 4, board_Player[4][4])


# function to check the splitting possibility
def split_Check(row, col):
    edge_check()
    if (row == 0 and col != 0) or (row == 4 and col != 0) or (row != 0 and col == 0) or (row != 0 and col == 4):
        if board_Count[row][col] == 3:
            Split(row, col, board_Player[row][col])
    elif row != 0 and col != 0 and row != 4 and col != 4:
        if board_Count[row][col] == 4:
            Split(row, col, board_Player[row][col])


# function to split the balls (chaining)
def Split(row, col, player):
    board_Player[row][col] = '0'
    board_Count[row][col] = 0
    if row - 1 >= 0:
        board_Player[row - 1][col] = player
        board_Count[row - 1][col] += 1
        split_Check(row - 1, col)
    if row + 1 <= 4:
        board_Player[row + 1][col] = player
        board_Count[row + 1][col] += 1
        split_Check(row + 1, col)
    if col - 1 >= 0:
        board_Player[row][col - 1] = player
        board_Count[row][col - 1] += 1
        split_Check(row, col - 1)
    if col + 1 <= 4:
        board_Player[row][col + 1] = player
        board_Count[row][col + 1] += 1
        split_Check(row, col + 1)


# function to check the winning possibility of player
def win_check():
    row = 0
    red_player_ctr = 0
    green_player_ctr = 0
    for i in range(5):
        col = 0
        for j in range(5):
            # Condition to the check the red winning
            if (board_Player[row][col] == 'R') or (board_Player[row][col] == '0'):
                red_player_ctr += 1
                if red_player_ctr == 25:
                    print("red win")
                    return 'red-win'
            # Condition to check the Green winning
            if (board_Player[row][col] == 'G') or (board_Player[row][col] == '0'):
                green_player_ctr += 1
                if green_player_ctr == 25:
                    print("green-win")
                    return 'green-win'
            col += 1
        row += 1


def Star_Converter():
    for i in range(5):
        for j in range(5):
            if board_Count[i][j] == 1:
                Display_Box[i][j] = '*'
            elif board_Count[i][j] == 2:
                Display_Box[i][j] = '**'
            elif board_Count[i][j] == 3:
                Display_Box[i][j] = '***'
            elif board_Count[i][j] == 4:
                Display_Box[i][j] = '****'
            else:
                Display_Box[i][j] = '0'
