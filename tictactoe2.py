#!/usr/bin/env python


# Game Programming, Level 2 Project
# TIC-TAC-TOE 4
# A simple strategy game, an extension of the standard 3x3 tic-tac-toe


#Imports:
import sys

#Global Variables:
GRID_SIZE = 4
INITIAL_BOARD = '.' *GRID_SIZE *GRID_SIZE
WIN_SEQUENCES = [
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11],
    [12,13,14,15],
    [0,4,8,12],
    [1,5,9,13],
    [2,6,10,14],
    [3,7,11,15],
    [0,5,10,15],
    [3,6,9,12],
]

def fail (msg):
    raise StandardError(msg)

def mark_value (markString):
    markValue = {
        'O': 1,
        '.': 0,
        'X': 10
    }
    return markValue[markString]

def create_board (boardString):
    # Take a description of the board as input and create the board
    #  in your representation
    # The string description is a sequence of 16 characters,
    #   each either X or O, or . to represent a free space
    # It is allowed to pass in a string describing a board
    #   that would never arise in legal play starting from an empty
    #   board
    board = []
    boardLength = GRID_SIZE * GRID_SIZE
    for i in range(boardLength):
        board.append(boardString[i])
    return board

def get_mark (board,x,y):
    # Take a board representation and checks if there's a mark at
    #    position x, y (each between 1 and 4)
    # Return 'X' or 'O' if there is a mark
    # Return False if there is not
    index = ((x - 1)*GRID_SIZE) + (y - 1)
    return board[index]

def get_row (board, row):
    indexes = range((row-1)*GRID_SIZE, (row-1)*GRID_SIZE + GRID_SIZE)
    return (board[index] for index in indexes)

def get_column (board, col):
    indexes = range(col-1, GRID_SIZE*GRID_SIZE, GRID_SIZE)
    return (board[index] for index in indexes)

def has_win (board):
    # FIX ME
    # 
    # Check if a board is a win for X or for O.
    # Return 'X' if it is a win for X, 'O' if it is a win for O,
    # and False otherwise

    for sequence in WIN_SEQUENCES:
        total = sum(mark_value(board(pos)) for pos in sequence)
    if total == 0:
        return False
    if total == 1*GRID_SIZE:
        return 'O'
    if total == 10*GRID_SIZE:
        return 'X'

def is_full (board):
    if '.' not in board:
        return True
    else:
        return False

def done (board):
    # Check if the board is done, either because it is a win or a draw
    return has_win(board) or is_full(board)

def print_board (board):
    # FIX ME
    # Display a board on the console
    for row in range(1, GRID_SIZE + 1):
        for column in range(1, GRID_SIZE + 1):
            print '  ' + get_mark(board, column, row),
        print ''

def is_string_valid(moveString):
    if len(moveString) != 3 or moveString[1] != ' ':
        fail('Invalid Input. Enter as "column row"')
    elif int(moveString[0]) not in range(1, GRID_SIZE + 1) or int(moveString[2]) not in range(1, GRID_SIZE + 1):
        fail('Invalid Input: Column or Row is out of range')
    else: return True

def is_move_valid(board, x, y):
    mark = get_mark(board, x, y)
    if mark != '.':
        fail('Position is already taken')
    else: return True

def perform_move(board, movePos, player):
    board[movePos] = player
    return board

def perform_player_move (board, player):
    #Gets string input
    moveString = raw_input('Position as "column row": ')
    #Checks if string is Valid, then gets column and row integers
    if is_string_valid(moveString):
        x = int(moveString[0]) - 1
        y = int(moveString[2]) - 1
    #Checks if if position is already taken, then performs move and returns board
    if is_move_valid(board, x, y):
        movePos = (x*GRID_SIZE + y)
        board = perform_move(board, movePos, player)
        return board

def main ():
    board = create_board(INITIAL_BOARD)
    print_board(board)

    board = perform_player_move(board, 'X')
    print_board(board)

if __name__ == "__main__":
    main()



