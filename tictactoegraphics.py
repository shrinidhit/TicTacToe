#!/usr/bin/env python
#Shrinidhi Thirumalai

# Game Programming, Level 2 Project
# TIC-TAC-TOE 4, with an AI implemented
# A simple strategy game, an extension of the standard 3x3 tic-tac-toe


#Imports:
import sys
from graphics import *

#Global Variables:
GRID_SIZE = 4
INITIAL_BOARD = '.' *GRID_SIZE *GRID_SIZE
BOARD_TEST = 'XO.XXXO....OOO..'

# #Comment this out for playing with 4
# WIN_SEQUENCES = [
#     [0,1,2],
#     [3,4,5],
#     [6,7,8],
#     [0,3,6],
#     [1,4,7],
#     [2,5,8],
#     [0,4,8],
#     [2,4,6]
# ]

#Comment this out for playing with 3
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

#Functions
def fail (msg):
    """Graceful Fail with error message"""
    raise StandardError(msg)

def mark_value (markString):
    """Returns Mark Value of String. Value is used in detecting wins"""
    markValue = {
        'O': 1,
        '.': 0,
        'X': 10
    }
    return markValue[markString]

def index_to_tuple(index):
    """Gets index and outputs coordinate in grid as a tuple"""
    y = int(index) / int(GRID_SIZE)
    x = index % GRID_SIZE
    return (x + 1, y + 1)

def tuple_to_index(coordinate):
    """Gets coordinate as a tuple and outputs index in list"""
    x, y = coordinate
    index = (y - 1)*GRID_SIZE + (x-1)
    return index

def create_board (boardString):
    """Take a description of the board a string input( a sequence of X's, O's, and .s )
    and outputs the board as a list of letters. 'X' is player X, '.' is a space, and 'O' is Player O"""
    # It is allowed to pass in a string describing a board
    #   that would never arise in legal play starting from an empty board
    board = []
    boardLength = GRID_SIZE * GRID_SIZE
    for i in range(boardLength):
        board.append(boardString[i])
    return board

def get_mark (board,x,y):
    """Take a board representation and checks if there's a mark at position x, y (each between 1 and GRID_SIZE)
    Return 'X' or 'O' if there is a mark, and returns False if there is not"""
    index = tuple_to_index((x,y))
    return board[index]

def get_row (board, row):
    """Returns positions of a row as a list"""
    indexes = range((row-1)*GRID_SIZE, (row-1)*GRID_SIZE + GRID_SIZE)
    return indexes

def get_column (board, col):
    """Returns positions of a column as a list"""
    indexes = range(col-1, GRID_SIZE*GRID_SIZE, GRID_SIZE)
    return indexes

def has_win (board):
    """Checks if a board is a win for X or for O.
    Return 'X' if it is a win for X, 'O' if it is a win for O, and False otherwise"""
    for sequence in WIN_SEQUENCES:
        total = sum(mark_value(board[pos]) for pos in sequence)
        if total == 1*GRID_SIZE:
            return 'O'
        if total == 10*GRID_SIZE:
            return 'X'
    return False

def is_full (board):
    """Checks if board is full"""
    if '.' not in board:
        return True
    else:
        return False

def done (board):
    """Checks if game is over. This is either full(draw) or a win"""
    return has_win(board) or is_full(board)

def print_board (board):
    """Display a board on the console"""
    for row in range(1, GRID_SIZE + 1):
        for column in range(1, GRID_SIZE + 1):
            print '  ' + get_mark(board, column, row),
        print ''

def is_string_valid(moveString):
    """Checks if a string input is valid. Row and Column are within grid range, and separated by a space.
    Returns true if valid, and all other inputs throw an error"""
    if len(moveString) != 3 or moveString[1] != ' ':
        fail('Invalid Input. Enter as "column row"')
    elif int(moveString[0]) not in range(1, GRID_SIZE + 1) or int(moveString[2]) not in range(1, GRID_SIZE + 1):
        fail('Invalid Input: Column or Row is out of range')
    else: return True

def is_move_valid(board, x, y):
    """Checks if move is valid on board(if the position is already taken). Throws error if false, or returns true
    if valid"""
    mark = get_mark(board, x, y)
    if mark != '.':
        fail('Position is already taken')
    else: return True

def perform_move(board, movePos, player):
    """Takes move position, player, and board, then makes move"""
    board[movePos] = player
    return board

def perform_player_move (board, player):
    """Gets player input, checks if it is valid, and makes move"""
    #Gets string input
    moveString = raw_input('Position as "column row": ')
    #Checks if string is Valid, then gets column and row integers
    if is_string_valid(moveString):
        x = int(moveString[0])
        y = int(moveString[2])
    #Checks if if position is already taken, then performs move and returns board
    if is_move_valid(board, x, y):
        return (x,y)

def make_move (board, move ,mark):
    """returns a copy of the board with the move recorded"""
    new_board = board[:]
    new_board[move] = mark
    return new_board

def possible_moves (board):
    """#Returns list of possible moves in a given board"""
    return [i for (i,e) in enumerate(board) if e == '.']


def utility (board):
    """Returns utility of final board state. Must pass in the final board state to be accurate"""
    if has_win(board) == 'O':
        return -1
    elif has_win(board) == 'X':
        return  1
    else:
        return 0

def min_value (board):
    """Returns the minimum utility possible after a single move"""
    possibleUtilities = []
    #Checks if game is over and returns utility
    if done(board):
        return utility(board)
    #Else, gets possible moves and moves one move down to repeat
    possibleMoves = possible_moves(board)
    for move in possible_moves(board):
        newBoard = make_move(board, move, 'O')
        possibleUtilities.append(max_value(newBoard))
    #returns minimum utility
    return min(possibleUtilities)

def max_value (board):
    possibleUtilities = []
    """Returns the maximum utility possible after a single move"""
    #Checks if game is over, and returns utility
    if done(board):
        return utility(board)
    #Else, gets possible moves and moves one move down to repeat
    possibleMoves = possible_moves(board)
    for move in possible_moves(board):
        newBoard = make_move(board, move, 'X')
        possibleUtilities.append(min_value(newBoard))
    #returns maximum utility
    return max(possibleUtilities)

def best_move (board, player):
    """Returns the best move possible, given a player input"""
    possibleDict = {} #Dictionary of all possible move results with the utility as the key and the move as the value
    #Loops through player's move options and adds to dictionary possibleDict
    for move in possible_moves(board):
        newBoard = make_move(board, move, player)
        if player == 'X':
            value = min_value(newBoard)
        if player == 'O':
            value = max_value(newBoard)
        possibleDict[value] = move
    #Returns best move option for player. Returns move with max utility for X and move with lowest utility for Y
    if player == 'X':
        return possibleDict[max(possibleDict)]
    else:
        return possibleDict[min(possibleDict)]

#Display Class:
class Display(object):
    """Class containing methods to group the pretty display for Game, using the graphics.py framework"""

    def __init__(self, board):
        """Displays an empty grid of given GRID_SIZE"""
        # Initializations of Attributes:
        self.board = board
        self.coordMap =  {} # dictionary of coordinate pairs mapping to respective rectangles
        self.win = GraphWin("graphicsTest", 600, 600) # names & sizes window (pixels)
        self.win.setCoords( 0, GRID_SIZE + 2, GRID_SIZE + 2, 0 ) # makes coordinates un-ugly (the rectangle in (row1, column1) will have its top left-hand corner in (1,1), rectangle in (row3, column5) will have (3,5), etc.)
        # draws empty rectangles/board
        for i in range(1,GRID_SIZE + 1):
            for j in range(1,GRID_SIZE + 1):
                coord = (i,j) # coord of rectangle's top left-hand corner
                rect = Rectangle(Point(i,j), Point(i+1,j+1))
                self.coordMap[coord] = rect # ads coord:rect to dictionary (yay!)
                rect.draw(self.win)

    def update_mark(self, mark, coordinate):
        """Draws a mark onto the grid, given it's mark and coordinate, and also returns updated board"""
        #Draws onto display
        x, y = coordinate
        Mark = Text(Point(x,y), mark)
        Mark.setSize(36)
        Mark.move(.5, .5)
        Mark.draw(self.win)
        #Updates board list and returns it
        index = tuple_to_index((x,y))
        self.board[index] = mark
        return self.board

    def start_board(self, board):
        """Creates starting display from a given board as a list"""
        for x in range(1, GRID_SIZE + 1):
            for y in range(1, GRID_SIZE + 1):
                mark = get_mark(board, x, y)
                if mark != '.':
                    self.update_mark(mark, (x,y))

def main ():
    """Main Game Loop"""
    #Creates and prints initial board
    board = create_board(BOARD_TEST)
    print_board(board)
    View = Display(board)
    View.start_board(board)
    #Gets User input and prints new board
    while not done(board):
        moveTuple = perform_player_move(board, 'X')
        board = View.update_mark('X', moveTuple)
        print_board(board)
        #Plays computer input if game isn't over
        if not done(board):
            moveIndex = best_move(board,'O')
            print moveIndex
            moveTuple = index_to_tuple(moveIndex)
            print 'Computer moves to', moveTuple
            board = View.update_mark('O', moveTuple)
            print_board(board)
    #Checks who has won, and prints result
    winner = has_win(board)
    if winner:
        print winner,'wins!'
    else:
        print 'Draw'

if __name__ == "__main__":
    main()
