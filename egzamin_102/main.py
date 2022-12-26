# Egzamin_102
import time
class Menu:

	def menu(self):
		print("")
		print("***********************")
		print("*     Game Menu       *")
		print("*********************** \n")
		print("1.  Current room")
		print("2.  Items in room")
		print("3.  Available actions")
		print("4.  Use item")
		print("5.  Next room")
		print("6.  Previous room")
		print("7.  Room menu")
		print("8.  Help")
		print("9.  Exit \n\n")
		player_choice = input("Your choice is: ")
		if int(player_choice) >= 1 and int(player_choice) <= 9:
			match str(player_choice):
				case "1":
					pass
				case "2":
					pass
				case "3":
					pass
				case "4":
					pass
				case "5":
					pass
				case "6":
					pass
				case "7":
					pass
				case "8":
					print("About a game")
					self.help()
				case "9":
					time.sleep(1)
					quit()
		else:
			print("You have to choose a correct nummer.")
			print("Press any key to return.")
			input()
			self.menu()

	def help(self):
		print('''

		Gra Mysterious Game jest prostą grą tekstową. Zadaniem jest przechodzenie między komnatami, znajdowanie przedmiotów i ich użycie.
		Po osiągnięciu ostatniej komnaty i zobyciu skarbu następuje koniec gry. Przedmioty należy zebrać w odpowiedniej kolejności.
		Gracz w każdej chwili może wywołać listę dostępnych opcji poprzez wybranie z menu stosownej pozycji. \n\n

		''')
		print("Press any key to return")
		input()
		self.menu()

class Room:
	def __init__(self, name):
		self.name = name

	def current_room(self):
		print("Current Room")

class Player:
	def __init__(self, name, health, age):
		self.name = name
		self.health = health
		self.age = age
		self.player_items = ['Sword']

	def introduce_yourself(self):
		print("\nHello " + self.name)
		print("You are " + str(self.age) + " years old. Your health level is now " + str(self.health) + ".")
		print("Let's play the game. \n")

	def show_player_items(self):
		print('\n Player items: \n')
		for item in self.player_items:
			print(item)
			print(item)

class Start_room(Room):
	def __init__(self, name):
		super().__init__(name)
		self.start_room_items = ['Magic key','Magic bootle','Basket']

	def show_items(self):
		for item in self.start_room_items:
			print(item)

	def get_item(self):
		pass

def main_menu():
	rooms = ['Hall','Fire room','Water room','Sezam']
	player_name = input("Enter your name: ")
	player_age = input("How old are you? ")
	player = Player(player_name, 100, player_age)
	player.introduce_yourself()
	room_list = rooms[0]
	print(player_name + ' you are in ' + room_list + ' now.')
	menu = Menu()
	menu.menu()
	data = input('Your choice is: ')
	if int(data) >= 1 and int(data) <= 3:
		match str(data):
			case "1":
				menu.menu()
			case "2":
				menu.help()
			case "3":
				print("\nPress any key to exit.\n")
				input()
				print("\n")
	else:
		print("You have to choose a correct nummer.")
		print("Press any key to return.")
		input()
		menu.menu()


def main():

	main_menu()
if __name__ == "__main__":
	main()




