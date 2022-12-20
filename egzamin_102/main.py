# Egzamin_102

class Room:
	def __init__(self, name, location, next_room, prev_room, current, room_id):
		self.rooms = ["Hall","Water Room","Fire Room","Sezam"]
		self.name = name
		self.location = location
		self.next_room = next_room
		self.prev_room = prev_room
		self.current = current
		self.items_in_room = []
		self.room_id = room_id

	def next_room(self):
		next_room_index = self.room_id + 1
		return self.next_room

	def previous_room(self):
		if self.room_id > 1:
			prev_room_index = self.room_id - 1
			return self.prev_room
		else:
			print("No previous room")
			return self.room_id

	def current_room(self):
		return self.current_room
		
	def possible_actions(self, room):
		pass
		# print possible actions and prev menu

class Character:
	def __init__(self, name, function, location):
		self.characters = []
		self.name = name
		self.function = function
		self.location = location

	def get_item(self):
		pass
		# usunac item z listy dostepnych itemow i dopisac do listy itemow playera

	def use_item(self):
		pass
		# zrobic itemem action
		# usunac item z listy itemow playera

	def move_to_next(self): 
		pass
		# room.next room

	def move_to_previous(self):
		pass
		# room.previous_room

class Item:
	def __init__(self, name, function, power_impact):
		self.name = name
		self.function = function
		self.power_impact = power_impact
		self.items = ["Magic key","Watter Ball","Fire Ball","Gem"]

	def item_action(self):
		pass

	def item_power_impact(self):
		pass

class Start_room(Room):
	def __init__(self, name, location, next_room, current, room_id):
		super().__init__(name, location, next_room, current, room_id)
		self.items_in_room = items_in_room
		self.possoble_action = possoble_action

	def actions(self):
		pass
		
class Watter_room(Room):
	def __init__(self, name, location, next_room, prev_room, current, room_id):
		super().__init__(name, location, next_room, prev_room, current, room_id)

class Fire_room(Room):
	def __init__(self, name, location, next_room, prev_room, current, room_id):
		super().__init__(name, location, next_room, prev_room, current, room_id)

class Sezam(Room):
	def __init__(self, name, location, prev_room, current, room_id):
		super().__init__(name, location, prev_room, current, room_id)

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

	def watter_ball(self):
		pass
		# watterball append user items

class Fire_ball(Item):
	def __init__(self, name, function, power_impact):
		super().__init__(name, function, power_impact)

	def take_fireball(self):
		pass
		# fireball append user items

class Gem(Item):
	def __init__(self, name, function):
		super().__init__(name, function)

	def take_gem(self):
		pass
		# gam append user items

	def use_gem(self):
		print(" You Win!")

class Menu:
	def main_menu(self):
		print("")
		print("***********************")
		print("*   Mysterious Game   *")
		print("*********************** \n")
		print("1.New game")
		print("2.Help and Options")
		print("3.Exit \n\n")

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
		player_choice = input("Your choice is: ")
		match str(player_choice):
			case "1":
				print("You are in: \n\n ")
			case "2":
				print("Next room")
			case "3":
				print("Previous room: ")
			case "4":
				print("Available items")
			case "5":
				print("Using items")

	def help(self):
		print("Gra Mysterious Game jest prostą grą tekstową.")

def main():
	menu = Menu()
	menu.main_menu()
	data = input('Your choice is: \n\n')
	match str(data):
		case "1":
			menu.player_menu()
		case "2":
			menu.help()
		case "3":
			print("Press any key to exit.")
			input()
			print("\n\n")

if __name__ == "__main__":
	main()
