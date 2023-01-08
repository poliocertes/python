# sudoku in console
# Z2J Python 103-1

import random


game_board = [
			['*', '*', '*', '*', '*', '*', '*', '*', '*'],
			['*', '*', '*', '*', '*', '*', '*', '*', '*'],
			['*', '*', '*', '*', '*', '*', '*', '*', '*'],
			['*', '*', '*', '*', '*', '*', '*', '*', '*'],
			['*', '*', '*', '*', '*', '*', '*', '*', '*'],
			['*', '*', '*', '*', '*', '*', '*', '*', '*'],
			['*', '*', '*', '*', '*', '*', '*', '*', '*'],
			['*', '*', '*', '*', '*', '*', '*', '*', '*'],
			['*', '*', '*', '*', '*', '*', '*', '*', '*']]

def print_board(board) -> None:
	print("- - - - - - - - - - - - ")
	for row in range(len(board)):
		if row % 3 == 0 and row != 0:
			print("- - - - - - - - - - - - ")
		for col in range(len(board[0])):
			if col % 3 == 0 and col != 0:
				print(" | ", end="")

			if col == 8:
				print(board[row][col])
			else:
				print(str(board[row][col])+' ', end="")

print_board(game_board)

# tablica.losowanie bez powtorzen z usuwaniem
# podzial na sekcje

