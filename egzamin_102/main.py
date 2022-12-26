# Egzamin_102

from menu import Menu
from room import Room, Start_room
from player import Player


def main():
	player_name = input("Enter your name: ")
	player_age = input("How old are you? ")
	player = Player(player_name, 100, player_age)
	player.introduce_yourself()
	menu = Menu()
	menu.main_menu()


if __name__ == "__main__":
	main()




