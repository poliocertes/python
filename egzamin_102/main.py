# Zadanie na egzamin_102

class Room:
	def __init__(self, name, location):
		self.rooms = ["Hall","Water Room","Fire Room","Sezam"]
		self.name = name
		self.location = location

	def next_room(self):
		pass # lokalizacja w tablicy i indeks +1

	def previous_room(self):
		pass # lokalizacja w tablicy i indeks -1

	def current_room(self):
		pass # lokalizacja w tablicy jako indeks

	def acessible_items(self):
		pass # w zaleznosci od pomieszczenia ma pokazac itemy w konsoli

	def possible_actions(self):
		pass

class Character:
	def __init__(self, name, function, location):
		self.characters = []
		self.name = name
		self.function = function
		self.location = location

	def move_to_next(self): # index pokoju. przenosimy postac z listy w daynm pokoju do listy nastepnym (Lub boolean dla kazdego roomu)
		pass

	def move_to_previous(self):
		pass


class Item:
	def __init__(self, name, function, power_impact):
		self.name = name
		self.function = function
		self.power_impact = power_impact

	def get_item(self):
		pass

	def use_item(self):
		pass


class Hall(Room):
	def __init__(self, name, location):
		super().__init__(name, location)
		pass


class Watter_room(Room):
	def __init__(self, name, location):
		super().__init__(name, location)

class Fire_room(Room):
	def __init__(self, name, location):
		super().__init__(name, location)

class Sezam(Room):
	def __init__(self, name, location):
		super().__init__(name, location)

class Player(Character):
	def __init__(self, name, function, location):
		super().__init__(name, function, location)
		self.player_items = []
		self.power_level = 0


class Mag(Character):
	def __init__(self, name, function, location):
		super().__init__(name, function, location)

class Watter_ball(Item):
	def __init__(self, name, function, power_impact):
		super().__init__(name, function, power_impact)

class Fire_ball(Item):
	def __init__(self, name, function, power_impact):
		super().__init__(name, function, power_impact)

class Gem(Item):
	def __init__(self, name, function):
		super().__init__(name, function)

class Menu:
	def exit(self):
		print("\n\n")
		print("Any key to exit.\n")
		input()
		quit()


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



def main():
	menu = Menu()
	menu.main_menu()
	data = input('Your choice is: \n\n')
	match str(data):
		case "1":
			menu.new_game()
		case "2":
			menu.help()
		case "3":
			print("Press any key to exit.")
			input()
			print("\n\n")


if __name__ == "__main__":
	main()
