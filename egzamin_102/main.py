# egzamin 102
import time
from characters import *
from menu import *
from rooms import *
from messages import *

def main():
	room_list = ['First Chamber','Second Chamber','Last Chamber']
	role_list = ['Player','Mag']
	current_room = room_list[0]
	menu = Menu()
	messages = Messages()
	menu.main_menu()
	first_room = First_room('Pierwsza komnata')
	hero = Hero('Joe', role_list[0], 10)
	player_choice = input('Your choice is >> ')
	while not player_choice.isnumeric():
		print('Enter a number!')
		player_choice = input('Enter again your choice >> : ')
	if 1 <= int(player_choice) <= 8:
		match str(player_choice):
			case '1':
				print('\n')
				print('Jesteś w',room_list[0],'\n')
				messages.first_room()
				main()
			case '2':
				print('\n----------------------')
				print('Dostępne przedmioty')
				print('----------------------')
				first_room.show_room_items()
				main()
			case '3':
				print('\n')
				main()
			case '4':
				print('\n')
				hero.hero_items()
				main()
			case '5':
				print('\n')
				print('Teraz wyruszamy do ',current_room,'\n')
				print(current_room)
				main()
			case '6':
				print("\n")
				hero.introduce_yourself()
				main()
			case '7':
				print('\n')
				menu.help_menu()
			case '8':
				print('--------------')
				print('Exit the game.')
				print('--------------')
				time.sleep(2)
				quit()

if __name__ == '__main__':
	main()