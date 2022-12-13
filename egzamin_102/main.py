# zadanie na egzamin_102

rooms = ["Hall","Room_fire","Room_watter","Store"]
items = ["Sword","Shield","Watter","Key","Book"]
user_items = []

class Game_character:

	def __init__(self):
		self.name = name
		self.age = age

	def add_character(self):
		pass

	def character_info(self):
		pass

class Player(Game_character):

	def __init__(self):
		super():__init__(name, age):
		self.role = role

	def action(self):
		pass

	def take_item(self):
		pass

	def use_item(self):
		pass

class Wizard(Game_character):

	def __init__(self):
		super():__init__(name, age):
		pass

class Room:

	def init(self):
		self.name = name
		self.location
		self.current_room = current_room
		self.next_room = next_room
		self.previous_room = previous_room

class Item(Room):

	def init(self):
		self.max_user_items = max_user_items
		self.item_location = item_location
		self.item_function = item_function


class Menu(Game):
	
	def init(self):
		pass

	def menu(self):
		'''
		1.Where am I
		2.Avalable command
		3.Current Room
		4.Next Room
		5.Previous Room
		6.Avalable items
		7.Use item
		8.Get item
		9.Drop Item
		10. Actions in room
		'''
		pass

	def help(self):
		pass

def main():
	running = True
	menu()
	while running:
		print("Hello World")
		print("Hello World1")
		print("Hello World2")
		print("Hello World3")
		print("Hello World4")
		data = input('Co dalej:')
		print(data)
if __name__ == "__main__":
	main()
