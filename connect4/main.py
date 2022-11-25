import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece(col,player):
    row = get_next_open_row(board, col)
    board[row, col] = player
    result = check_victory(board, row, col)
    return result

def is_valid_location(board, col):
    return col in range(7) and board[0][col] == 0

def get_next_open_row(board,col):
    for r in range(ROW_COUNT-1,-1,-1):
        if board[r][col] == 0:
            return r

def check_victory(board, row, col):
    player1win = 0
    player2win = 0
    for c in range(7): # Check the row 
        if board[row][c] == 1:
            player1win += 1
            player2win = 0
            if player1win == 4: return 1
        elif board[r][col] == 2:
            player1win = 0
            player2win += 1
            if player2win == 4: return 2
    player1win = 0
    player2win = 0
    for r in range(6): # Check the column
        if board[r][col] == 1:
            player1win += 1
            player2win = 0
            if player1win == 4: return 1
        elif board[r][col] == 2:
            player1win = 0
            player2win += 1
            if player2win == 4: return 2
    

board = create_board()
print(board)

game_over = False

turn = 0

while not game_over:
    #Ask for Player1 Input
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6):"))
    #Ask for Player2 Input
    else:
        col = int(input("Player 2 Make your Selection (0-6):"))
    if is_valid_location(board, col):
        result = drop_piece(col, turn+1)
        if result == 1:
            print(board)
            print("Player 1 has won!")
            game_over = True
            break
        elif result == 2:
            print(board)
            print("Player 2 has won!")
            game_over = True
            break
        turn += 1
        turn = turn % 2
        print(board)

