import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece(col,player):
    board[get_next_open_row(board, col), col] = player
    pass

def is_valid_location(board, col):
    return board[0][col] == 0

def get_next_open_row(board,col):
    for r in range(ROW_COUNT-1,-1,-1):
        if board[r][col] == 0:
            return r

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
        drop_piece(col, turn+1)
        turn += 1
        turn = turn % 2
        print(board)

