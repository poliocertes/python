# Egzamin_102


class Room:
	def __init__(self, name, location, next_room, prev_room, current):
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
		return self.next_room_id

	def previous_room(self):
		if self.room_id > 1:
			prev_room_index = self.room_id - 1
			return self.prev_room_id
		else:
			return self.room_i

	def current_room(self):
		return self.room_id
		
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
		self.items = ["Magic key","Watter Ball","Fire Ball","Gem"]

	def item_action(self):
		pass

	def item_power_impact(self):
		pass

class Start_room(Room):
	def __init__(self, name, location, next_room, current, room_id):
		super().__init__(name, location, next_room, current, room_id)
		self.items_in_room = items_in_room
		
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

class Fire_ball(Item):
	def __init__(self, name, function, power_impact):
		super().__init__(name, function, power_impact)

class Gem(Item):
	def __init__(self, name, function):
		super().__init__(name, function)

class Menu:
	def main_menu(self):
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
		player_choice = input("Your choice is: ")
		match str(player_choice):
		  case "1":
		   room.current_room()
		  case "2":
		    room.next_room()
		  case "3":
		  	room.previous_room()
		  case "4":
		  	room.available_items()
		  case "5":
		  	item.use_item()

  			print("Press any key to exit.")
  			input()
  			print("\n\n")

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
			menu.player_menu()
		case "2":
			menu.help()
		case "3":
			print("Press any key to exit.")
			input()
			print("\n\n")

if __name__ == "__main__":
	main()
