# Zadanie na egzamin_102

rooms = ["Hall", "Room_of_fire", "Sezam", "Room_of_watter"]
items = ["Sword", "Shield", "Watter", "Key", "Book"]
user_items = []


class Menu:

	def main_menu(self):
		print("***********************")
		print("*                     *")
		print("*   Mysterious Game   *")
		print("*                     *")
		print("*********************** \n")
		print("  Menu Options: \n")
		print("1.New game")
		print("2.Help and Options")
		print("3.Exit \n\n")
		pass

	def new_game(self):
		pass

	def help(self):
		print("Help")

	@staticmethod
	def exit():
		print("\n")
		print("Any key to exit. \n")
		input()
		quit()


class Game:
	def __init__(self):
		pass

	def new_game(self):
		pass

	@staticmethod
	def game_over():
		quit()


class Game_character:
	def __init__(self, name, role, location):
		self.name = name
		self.role = role
		self.location = location
		self.is_in_room = False
		pass


class Fireman(Game_character):
	def __init__(self, role, location):
		super().__init__(role, location)


class Waterman(Game_character):
	def __init__(self, role, location):
		super().__init__(role, location)


class Player(Game_character):
	def __init__(self, start_point):
		super().__init__()
		self.start_point = start_point


class Room:
	def __init__(self, name):
		self.name = name
		self.items = []
		self.occupied = False

	def character_in_room(self):
		self.occupied = True

	def current_room(self):
		pass

	def previous_room(self):
		pass

	def next_room(self):
		pass


class Item(Room):
	def __init__(self):
		super().__init__()
		pass

	def item_position(self):
		pass

	def get_item(self):
		pass

	def use_item(self):
		pass


def main():
	menu = Menu()
	game = Game()
	menu.main_menu()
	data = input('Your choice is: \n\n')
	match str(data):
		case "1":
			pass
		case "2":
			pass
		case "3":
			print("Press any key to exit.")
			input()
			print("\n\n")
			game.new_game()


if __name__ == "__main__":
	main()
