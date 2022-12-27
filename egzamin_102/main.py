# Egzamin_102
import time

rooms = ['Hall','Chamber of magic','Sezam']
class Room:
	def __init__(self, name):
		self.name = name
		self.rooms = []

	def current_room(self):
		pass

	def next_room(self):
		pass

	def prev_room(self):
		pass


class Hall(Room):
	pass


class Store(Room):
	pass


class Sezam(Room):
	pass


class Character:
	def __init__(self, name, age, power_level):
		self.name = name
		self.age = age
		self.power_level = power_level

	def introduce_yourself(self):
		print("Hallo " + self.name + ". You are " + str(self.age) + " years old and you have a " + str(self.power_level) + " points of energy. \n")


class Player(Character):
	def __init__(self, name, age, power_level, magic_level):
		super().__init__(name, age, power_level)
		self.magic_level = magic_level
		self.player_items = ['Sword']

	def show_player_items(self):
		if len(self.player_items):
			print("\nPlayer items:\n")
			for item in self.player_items:
				print(item)
		else:
			print("Player has no items.")

	def use_item(self):
		pass


class Mag(Character):
	def __init__(self):
		super().__init__()

class Item:
	pass


class Menu:
	def main_menu(self):
		print("Let's play the game. ")
		print("* * * * * * * * * * * * *")
		print(" * Mysterious game menu  *")
		print("* * * * * * * * * * * * *")
		print("1.	Player items")
		print("2.	Use item")
		print("3.	Get item")
		print("4.	Current room")
		print("5.	Next room")
		print("6.	Prev room")
		print("7.	Help")
		print("8.	Exit")

	def menu_help(self):
		print('''

				Gra Mysterious Game jest prostą grą tekstową. Zadaniem jest przechodzenie między komnatami, znajdowanie przedmiotów i ich użycie.
				Po osiągnięciu ostatniej komnaty i zobyciu skarbu następuje koniec gry. Przedmioty należy zebrać w odpowiedniej kolejności oraz pilnować poziomu
				życia tak aby nie spadł on do zera gdyż wykonywanie czynności i zbieranie przedmiotów wiąże się z utratą pewnej porcji energi. 
				Gracz w każdej chwili może wywołać listę dostępnych opcji poprzez wybranie z menu stosownej pozycji. \n

				''')
		print("Press any key to return")
		input()
		self.main_menu()



def main():
	menu = Menu()
	hero_name = input("Enter your name: ")
	while not hero_name.isalpha():
		print("Only letters are allowed")
		hero_name = input("Enter a correct player name: ")
	hero_age = input("How old are you? ")
	while not hero_age.isnumeric():
		print("Enter a number")
		hero_age = input("Enter again: ")
	player = Player(hero_name, hero_age, 100, 50)
	player.introduce_yourself()
	menu.main_menu()
	player_choice = input("Your choice: ")
	if 8 >= int(player_choice) >= 1:
		match str(player_choice):
			case "1":
				player.show_player_items()
				menu.main_menu()
				input()
			case "2":
				pass
			case "3":
				pass
			case "4":
				pass
			case "5":
				pass
			case "":
				pass
			case "7":
				print("Help menu")
				menu.menu_help()
			case "8":
				print("\nYou leave the game.")
				time.sleep(1)
				quit()
	else:
		print("Value Error. Please enter correct number. ")
		menu.main_menu()


if __name__ == "__main__":
	main()
