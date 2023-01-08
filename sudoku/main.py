# sudoku in console
# Z2J Python 103-1

import random


class Sudoku_game:
	def __init__(self):
		self.game_board = [
				['*', '*', '*', '*', '*', '*', '*', '*', '*'],
				['*', '*', '*', '*', '*', '*', '*', '*', '*'],
				['*', '*', '*', '*', '*', '*', '*', '*', '*'],
				['*', '*', '*', '*', '*', '*', '*', '*', '*'],
				['*', '*', '*', '*', '*', '*', '*', '*', '*'],
				['*', '*', '*', '*', '*', '*', '*', '*', '*'],
				['*', '*', '*', '*', '*', '*', '*', '*', '*'],
				['*', '*', '*', '*', '*', '*', '*', '*', '*'],
				['*', '*', '*', '*', '*', '*', '*', '*', '*']]
		self.row_section = (0, 3)
		self.col_section = (0, 3)
		'''
		self.row_section = [(0, 3), (3, 6)]
		self.col_section = [(0, 3), (6, 9)]
		self.row_section = [(0, 3), (3, 6)]
		self.col_section = [(1, 3), (3, 6)]
		self.row_section = [(0, 3), (3, 6)]
		self.col_section = [(0, 3), (6, 9)]
		self.row_section = [(0, 3), (3, 6)]
		self.col_section = [(0, 3), (6, 9)]
		self.row_section = [(0, 3), (3, 6)]
		self.col_section = [(0, 3), (6, 9)]
		self.row_section = [(0, 3), (3, 6)]
		self.col_section = [(0, 3), (6, 9)]
		self.col_section = [(0, 3), (6, 9)]
		self.col_section = [(0, 3), (6, 9)]
		self.col_section = [(0, 3), (6, 9)]
		'''
	def print_board(self):
		print("- - - - - - - - - - - - -")
		for row in range(len(self.game_board)):
			if row % 3 == 0 and row != 0:
				print("- - - - - - - - - - - - -")
			for col in range(len(self.game_board[0])):
				if col % 3 == 0 and col != 0:
					print(" | ", end=" ")
				if col == 8:
					print(self.game_board[row][col])
				else:
					print(str(self.game_board[row][col])+' ', end="")
		print ("- - - - - - - - - - - - -")

	def fill_section(self):
		options_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		for row in range(len(self.game_board)):
			for col in range(len(self.game_board)):
				if row in range(*self.row_section) and col in range(*self.col_section):
					random_choice = random.choice(options_list)
					self.game_board[row][col] = random_choice
					options_list.remove(random_choice)

	def validation(self):
		pass


def main():
	sudoku_game = Sudoku_game()
	sudoku_game.fill_section()
	sudoku_game.print_board()


if __name__ == '__main__':
	main()

