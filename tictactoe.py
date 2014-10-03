#!/usr/bin/env python


# Shrinidhi Thirumalai
# Simple Game of Tic-Tac-Toe with Minimax implemented


# representation: array of 9 cells (0 in upper-left corner, row by row)
# each cell one of 'O','_','X'




#Global Variables
WIN_SEQUENCES = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]
MARK_VALUE = {
    'O': 1,
    '_': 0,
    'X': 10
}
GRID_SIZE = 3


#Functions:
def fail (msg):
    """Graceful Fail with error message"""
    raise StandardError(msg)

def initialize_board ():
    """Initializes board with "_" as empty spaces for the given grid size(a global variable)"""
    return ['_'] * GRID_SIZE * GRID_SIZE

def has_win (board):
    """Checks who has won the game. Returns 'O' if the board is a win for O. 
    Returns 'X' if the board is a win for X. Returns False otherwise"""
    for positions in WIN_SEQUENCES:
        s = sum(MARK_VALUE[board[pos]] for pos in positions)
        if s == 3:
            return 'O'
        if s == 30:
            return 'X'
    return False

def print_board (board):
    """Prints board with empty spaces displayed as "_" """
    for i in range(0,3):
        print '  ', board[i*3],board[i*3+1],board[i*3+2]
    print


def read_player_input (board):
    """Gets input from player as a position to move from 0 to 8"""
    valid = [ i for (i,e) in enumerate(board) if e == '_']
    while True:
        move = raw_input('Position (0-8)? ')
        if move == 'q':
            exit(0)
        if len(move)>0 and int(move) in valid:
            return int(move)

def done (board):
    """Checks if there's a win or the board is full. Returns true if done, false if not"""
    return (has_win(board) or not [ e for e in board if (e == '_')])

# given a board and a move (a position 0-8) and a mark 'O' or 'X'
#  returns a new board with that move '_'recorded
def make_move (board,move,mark):
    """returns a copy of the board with the move recorded"""
    new_board = board[:]
    new_board[move] = mark
    return new_board

def possible_moves (board):
    """#Returns list of possible moves in a given board"""
    return [i for (i,e) in enumerate(board) if e == '_']


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


#Main Game Loops
def test():
    """Debug test loop"""
    board = initialize_board()
    print_board(board)
    print possible_moves(board)

def main (): 
    """Main Game Looop"""
    #Initializes and prints board
    board = initialize_board()

    print_board(board)
    #Checks if game is done
    while not done(board):
        #Gets X player's input and prints board
        move = read_player_input(board)
        board[move] = 'X'
        print_board(board)
        #Performs best move for O if game isn't over, then prints board
        if not done(board):
            move = best_move(board,'O')
            print 'Computer moves to',move
            board[move] = 'O'
            print_board(board)
    #Checks who has won, and prints result
    winner = has_win(board)
    if winner:
        print winner,'wins!'
    else:
        print 'Draw'
        
#Runs main when code is began
if __name__ == '__main__':
    main()