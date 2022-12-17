# Egzamin_102

class Game:
	pass
	''' 
	Nowa Gra
	tworzenie nowego gracza
	lokalizacja Start_room
	
	'''
class Room:
	def __init__(self, name, location, next_room, prev_room, current):
		self.rooms = ["Hall","Water Room","Fire Room","Sezam"]
		self.name = name
		self.location = location
		self.next_room = next_room
		self.prev_room = prev_room
		self.current = current
		self.items_in_room = []

	'''
	możliwe opcje. Jak Start_room to nie ma poprzedniego. Idizemy dalej i klikamy co jest i jaki jest cel.
	'''

	def next_room(self):
		pass

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

	def get_item(self):
		pass

	def use_item(self):
		pass

	def move_to_next(self): # index pokoju. przenosimy postac z listy w danym pokoju do listy nastepnym (Lub boolean dla kazdego roomu)
		pass

	def move_to_previous(self):
		pass


class Item:
	def __init__(self, name, function, power_impact):
		self.name = name
		self.function = function
		self.power_impact = power_impact

	def item_action(self):
		pass

	def item_power_impact(self):
		pass


class Start_room(Room):
	def __init__(self, name, location, next_room, current):
		super().__init__(name, location, next_room, current)
		self.next = next


class Watter_room(Room):
	def __init__(self, name, location, next_room, prev_room, current):
		super().__init__(name, location, next_room, prev_room, current)

class Fire_room(Room):
	def __init__(self, name, location, next_room, prev_room, current):
		super().__init__(name, location, next_room, prev_room, current)

class Sezam(Room):
	def __init__(self, name, location, prev_room, current):
		super().__init__(name, location, prev_room, current)

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

	def help(self):
		print('''
		Gra Mysterious Game jest prostą grą tekstową. 
		
		''')

	def exit(self):
		print("\n\n")
		print("Any key to exit.\n")
		input()
		quit()


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

'''
01. Main menu
	1.Nowa gra
	2.Pomoc
	3.Wyjście
1.1
	1.Gdzie jestem
	2.Dostepne przedmioty
	3.Uzyj item
	4.Warunki odblokowania DALEJ
	5.Ostatni pokój( Zabierz Gral) <-- tylko w ostatnim
	6.Poprzedni pokój
	7.Następny pokój
	8.Rozmowa z magiem
1.2
	1.O grze i opis
	2.Sterowanie
	3.Wyjście
'''