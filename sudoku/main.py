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

		self.board_sections = [[(0, 3), (0, 3)], [(3, 6), (0, 3)], [(6, 9), (0, 3)], [(0, 3), (3, 6)],
							   [(3, 6), (3, 6)], [(6, 9), (3, 6)], [(0, 3), (6, 9)], [(3, 6), (6, 9)], [(6, 9), (6, 9)]]

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

	def fill_section(self, i, j, k, l):
		options_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		for row in range(len(self.game_board)):
			for col in range(len(self.game_board)):
				if row in range(*self.board_sections[i][j]) and col in range(*self.board_sections[k][l]):
					random_choice = random.choice(options_list)
					self.game_board[row][col] = random_choice
					options_list.remove(random_choice)

	def validation(self):
		row_check = []
		col_check = []

		for row in self.game_board:
			for element in row:
				if element  in row_check:
					print('Error. Duplicate in row.')
					print('Sudoku not valid!\n')
					input('Press any key to exit Sudoku')
					exit()
				else:
					row_check.append(element)
					if len(row_check) == 7:
						row_check.clear()
		for col in self.game_board:
			for element in col:
				if element in col_check:
					print('Error. Duplicate in column.')
					print('Sudoku not valid!\n')
					input('Press any key to exit Sudoku')

					exit()
				else:
					col_check.append(element)
					if len(col_check) == 6:
						row_check.clear()

def main():
	print('Lets play sudoku in terminal.\n')
	sudoku_game = Sudoku_game()
	i = 0
	j = 0
	k = 0
	l = 1
	input('Press enter to fill first section. ')
	sudoku_game.fill_section(i, j, k, l)
	sudoku_game.print_board()
	while i < 8:
		
		input('Press enter to fill next section. ')
		i += 1
		k += 1
		sudoku_game.fill_section(i, j, k, l)
		sudoku_game.print_board()
	print('Check validation.\n\n 1. Press y to confirm\n 2. Press n to cancel\n')
	user_choice = input('Validate?  \n')	


	match str(user_choice):
		case 'y':
			sudoku_game.validation()
		case 'n':
			quit()

if __name__ == '__main__':
	main()


