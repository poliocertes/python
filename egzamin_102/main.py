# egzamin 102
import time
from characters import *
from menu import *
from rooms import *

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
				pass
			case "2":
				pass
			case "3":
				pass
			case "4":
				print("\n")
				hero.hero_items()
				main()
			case "5":
				pass
			case "6":
				hero.introduce_yourself()
				main()
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