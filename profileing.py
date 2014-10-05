#Shrinidhi Thirumalai
from tictactoegraphics import *
import cProfile
import pstats

def minmax():
	board = create_board(INITIAL_BOARD)
	for i in range(1):
		moveIndex = best_move(board,'O')

def profile_test():
	cProfile.run('minmax()', 'stats')
	p = pstats.Stats('stats')
	p.strip_dirs()
	p.sort_stats('time')
	p.print_stats()

if __name__ == '__main__':
	profile_test()
