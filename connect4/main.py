import numpy as np
import pygame
import sys

ROW_COUNT = 6
COLUMN_COUNT = 7

BLUE = (0,0,255)
YELLOW = ()

def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece(col,player):
    row = get_next_open_row(board, col)
    board[row, col] = player
    if player == 1:
        pygame.draw.circle(screen, (255,0,0), (col*SQUARE_SIZE+SQUARE_SIZE/2, row*SQUARE_SIZE+SQUARE_SIZE*3/2), SQUARE_SIZE/2 - 5)
    if player == 2:
        pygame.draw.circle(screen, (255,255,0), (col*SQUARE_SIZE+SQUARE_SIZE/2, row*SQUARE_SIZE+SQUARE_SIZE*3/2), SQUARE_SIZE/2 - 5)
    pygame.display.update()
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
        elif board[row][c] == 2:
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
    player1win = 0
    player2win = 0
    # Check for positive slope diagonals
    for a in range(4): # [3,0] to [0.3]
        if board[3-a, a] == 1:
            player1win += 1
            player2win = 0
            if player1win == 4: return 1
        if board[3-a, a] == 2:
            player1win = 0
            player2win += 1
            if player2win == 4: return 2
    player1win = 0
    player2win = 0
    for a in range(5):
        if board[4-a, a] == 1:
            player1win += 1
            player2win = 0
            if player1win == 4: return 1
        if board[4-a, a] == 2:
            player1win = 0
            player2win += 1
            if player2win == 4: return 2
    player1win = 0
    player2win = 0
    for a in range(6):
        if board[5-a, a] == 1:
            player1win += 1
            player2win = 0
            if player1win == 4: return 1
        if board[5-a, a] == 2:
            player1win = 0
            player2win += 1
            if player2win == 4: return 2
    player1win = 0
    player2win = 0
    for a in range(6):
        if board[5-a, a+1] == 1:
            player1win += 1
            player2win = 0
            if player1win == 4: return 1
        if board[5-a, a+1] == 2:
            player1win = 0
            player2win += 1
            if player2win == 4: return 2
    player1win = 0
    player2win = 0
    for a in range(5):
        if board[5-a, a+2] == 1:
            player1win += 1
            player2win = 0
            if player1win == 4: return 1
        if board[5-a, a+2] == 2:
            player1win = 0
            player2win += 1
            if player2win == 4: return 2
    player1win = 0
    player2win = 0
    for a in range(4):
        if board[5-a, a+3] == 1:
            player1win += 1
            player2win = 0
            if player1win == 4: return 1
        if board[5-a, a+3] == 2:
            player1win = 0
            player2win += 1
            if player2win == 4: return 2
    player1win = 0
    player2win = 0
    # Check for negative slope diagonals
    for a in range(4):
        if board[a+2, a] == 1:
            player1win += 1
            player2win = 0
            if player1win == 4: return 1
        elif board[a+2, a] == 2:
            player1win = 0
            player2win += 1
            if player2win == 4: return 2
    player1win = 0
    player2win = 0
    for a in range(5):
        if board[a+1, a] == 1:
            player1win += 1
            player2win = 0
            if player1win == 4: return 1
        elif board[a+1, a] == 2:
            player1win = 0
            player2win += 1
            if player2win == 4: return 2
    player1win = 0
    player2win = 0
    for a in range(6):
        if board[a, a] == 1:
            player1win += 1
            player2win = 0
            if player1win == 4: return 1
        elif board[a, a] == 2:
            player1win = 0
            player2win += 1
            if player2win == 4: return 2
    player1win = 0
    player2win = 0
    for a in range(6):
        if board[a, a+1] == 1:
            player1win += 1
            player2win = 0
            if player1win == 4: return 1
        elif board[a, a+1] == 2:
            player1win = 0
            player2win += 1
            if player2win == 4: return 2
    player1win = 0
    player2win = 0
    for a in range(5):
        if board[a, a+2] == 1:
            player1win += 1
            player2win = 0
            if player1win == 4: return 1
        elif board[a, a+2] == 2:
            player1win = 0
            player2win += 1
            if player2win == 4: return 2
    player1win = 0
    player2win = 0
    for a in range(4):
        if board[a, a+3] == 1:
            player1win += 1
            player2win = 0
            if player1win == 4: return 1
        elif board[a, a+3] == 2:
            player1win = 0
            player2win += 1
            if player2win == 4: return 2

pygame.init()

board = create_board()
print(board)

game_over = False

turn = 0

def draw_board(board):
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            pygame.draw.rect(screen, (0,0,255), (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, (0,0,0), (c*SQUARE_SIZE+SQUARE_SIZE/2, r*SQUARE_SIZE+SQUARE_SIZE*3/2), SQUARE_SIZE/2 - 5)
    pass


SQUARE_SIZE = 100
width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT+1) * SQUARE_SIZE

size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, (0,0,0), (0,0,width, SQUARE_SIZE))
            if turn == 0:
                pygame.draw.circle(screen, (255,0,0), (event.pos[0],SQUARE_SIZE/2), SQUARE_SIZE/2)
            else:
                pygame.draw.circle(screen, (255,255,0), (event.pos[0],SQUARE_SIZE/2), SQUARE_SIZE/2)
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            col = event.pos[0]//SQUARE_SIZE
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
                pygame.draw.rect(screen, (0,0,0), (0,0,width, SQUARE_SIZE))
                turn += 1
                turn = turn % 2
                if turn == 0:
                    pygame.draw.circle(screen, (255,0,0), (event.pos[0],SQUARE_SIZE/2), SQUARE_SIZE/2)
                else:
                    pygame.draw.circle(screen, (255,255,0), (event.pos[0],SQUARE_SIZE/2), SQUARE_SIZE/2)
                pygame.display.update()
                
                print(board)

