# egzamin 102
from menu import *
from characters import *
import time

class Room(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def current_room(self):
		return self.name

class First_room(Room):
	def __init__(self, name, description):
		super().__init__(name, description)
		self.room_items = ['1','2','3']

class Second_room(Room):
	def __init__(self, name, description):
		super().__init__(name, description)
		self.room_items = ['1','2','3']

class Last_room(Room):
	def __init__(self, name, description):
		super().__init__(name, description)
		self.room_items = ['1','2','3']

	def show_room_items(self):
		for item in self.room_items:
			print(item)


class Item(object):
	def __init__(self, name, energy_impact):
		self.name = name
		self.energy_impact = energy_impact


def main():
	room_list = ['First room','Middle room','Last room']
	role_list = ['Player','Mag']
	menu = Menu()
	menu.main_menu()
	hero = Hero("Joe", role_list[0])
	player_choice = input("Your choice is >> ")
	while not player_choice.isnumeric():
		print("Enter a number!")
		player_choice = input("Enter again your choice >> : ")
	if 1 <= int(player_choice) <= 8:
		match str(player_choice):
			case "1":
				pass
			case "2":
				pass
			case "3":
				pass
			case "4":
				print("\n")
				hero.hero_items()
			case "5":
				pass
			case "6":
				pass
			case "7":
				pass
			case "8":
				print("--------------")
				print("Exit the game.")
				print("--------------")
				time.sleep(2)
				quit()

if __name__ == "__main__":
	main()