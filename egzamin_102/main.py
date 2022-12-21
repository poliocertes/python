# Egzamin_102

class Menu:
	def main_menu(self):
		print("")
		print("***********************")
		print("*   Mysterious Game   *")
		print("*********************** \n")
		print("1.New game")
		print("2.About a game")
		print("3.Exit \n\n")
		data = input('Your choice is: \n')
		match str(data):
			case "1":
				self.player_menu()
			case "2":
				self.help()
			case "3":
				print("Press any key to exit.")
				input()
				print("\n")

	def player_menu(self):
		print("***********************")
		print("*     Player Menu       *")
		print("*********************** \n")
		print("  Options: \n")
		print("1.  Current room")
		print("2.  Next room")
		print("3.  Previous room")
		print("4.  Available items")
		print("5.  Use item")
		print("6.  Return")
		player_choice = input("Your choice is: \n")
		match str(player_choice):
			case "1":
				print("You are in: \n ")
				print()
				self.player_menu()
			case "2":
				print("You are in: \n Next room \n")
				print()
				self.player_menu()
			case "3":
				print("You are in: \n Previous room: \n")
				print()
				self.player_menu()
			case "4":
				print("Available items")  # items in room list
				# self.available_items() for item in room_items print item np. :)
				print("Press any key to return")
				input()
				self.player_menu()
			case "5":
				print("Using items") #item action and item from user items remove
			case "6":
				print("Return to previous menu")
				self.main_menu()

	def help(self):
		print('''	Gra Mysterious Game jest prostą grą tekstową. Zadaniem jest przechodzenie między komnatami, znalezienie przedmiotów i ich uzycie.
		Po osiągnięciu ostatniej komnaty i zobyciu skarbu następuje koniec gry.
		2Gracz w każdej chwili może wywołać listę dostępnych opcji poprzez wybranie z menu stosownej opcji. \n\n ''')
		print("Press any key to return")
		input()
		self.main_menu()

class Room:
	def __init__(self, name, next_room, prev_room, current):
		self.name = name
		self.next_room = next_room
		self.prev_room = prev_room
		self.current = current
		self.items_in_room = []
	

	def current_room(self):
		return self.current

	def next_room(self):
		return self.next_room

	def prev_room(self):
		return self.prev_room


		# nazwa pokoju, itemy i możliwe opcje

class Start_room(Room):
	def __init__(self, name, next_room, current):
		super().__init__(name, next_room, current)
		pass

	def start_room_tasks(self):
		pass

	def describe_room(self):
		pass
class Water_room(Room):
	def __init__(self, name, next_room, prev_room, current):
		super().__init__(name, next_room, prev_room, current)
		pass

	def water_room_tasks(self):
		pass

	def describe_water_room(self):
		pass

class Fire_room(Room):
	def __init__(self, name, next_room, prev_room, current):
		super().__init__(name, next_room, prev_room, current)
		pass

	def fire_room_tasks(self):
		pass

	def describe_fire_room(self):
		pass

class Sezam(Room):
	def __init__(self, name, prev_room, current):
		super().__init__(name, prev_room, current)
		pass

	def sezam_tasks(self):
		pass

	def describe_sezam(self):
		pass

class Character:
	def __init__(self):
		pass

class Player(Character):
	def __init__(self):
		super().__init__()
		pass

class Mag(Character):
	def __init__(self):
		super().__init__()
		pass

class Item:
	def __init__(self):
		pass

class Watter_key(Item):
	def __init__(self):
		super().__init__()
		pass

class Fire_key(Item):
	def __init__(self):
		super().__init__()
		pass

class Gem(Item):
	def __init__(self):
		super().__init__()
		pass

def main():
	menu = Menu()
	menu.main_menu()

if __name__ == "__main__":
	main()
