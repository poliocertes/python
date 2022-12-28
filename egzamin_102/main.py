# egzamin 102
import time
from characters import *
from menu import *
from rooms import *



class Item(object):
	def __init__(self, name, energy_impact):
		self.name = name
		self.energy_impact = energy_impact

class Key(Item):
	def __init__(self,name,energy_impact):
		super().__init__(name,energy_impact)

	def item_requirements(self):
		pass

	def energy_impact(self):
		pass

class Book(Item):
	def __init__(self,name,energy_impact):
		super().__init__(name,energy_impact)
	pass

class Bottle(Item):
	def __init__(self,name,energy_impact):
		super().__init__(name,energy_impact)
	pass

def main():
	room_list = ['First room','Second room','Last room']
	role_list = ['Player','Mag']
	menu = Menu()
	menu.main_menu()
	hero = Hero("Joe", role_list[0], 10)
	player_choice = input("Your choice is >> ")
	while not player_choice.isnumeric():
		print("Enter a number!")
		player_choice = input("Enter again your choice >> : ")
	if 1 <= int(player_choice) <= 8:
		match str(player_choice):
			case "1":
				hero.introduce_yourself()
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
				print("\n")
				menu.help_menu()
			case "8":
				print("--------------")
				print("Exit the game.")
				print("--------------")
				time.sleep(2)
				quit()

if __name__ == "__main__":
	main()