# # # Egzamin_102

class Menu:
	def main_menu(self):
		print("")
		print("***********************")
		print("*   Mysterious Game   *")
		print("*********************** \n")
		print("1.  New game")
		print("2.  About a game")
		print("3.  Exit \n\n")
		data = input('Your choice is: ')
		if int(data) >= 1 and int(data) <= 3:
			match str(data):
				case "1":
					self.player_menu()
				case "2":
					self.help()
				case "3":
					print("\nPress any key to exit.\n")
					input()
					print("\n")
		else:
			print("You have to choose a correct nummer.")
			print("Press any key to return.")
			input()
			self.main_menu()

	def player_menu(self):
		print("")
		print("***********************")
		print("*     Player Menu       *")
		print("*********************** \n")
		print("  Options: \n")
		print("1.  Current room")
		print("2.  Next room")
		print("3.  Previous room")
		print("4.  Room menu")
		print("5.  Return \n\n")
		player_choice = input("Your choice is: ")
		if int(player_choice) >= 1 and int(player_choice) <= 5:
			match str(player_choice):
				case "1":
					print("\nYou are in: \n ")

					self.player_menu()
				case "2":
					print("\nYou are in: \n Next room \n")

					self.player_menu()
				case "3":
					print("\nYou are in: \n Previous room: \n")

					self.player_menu()
				case "4":

					self.room_menu()
				case "5":
					print("\nReturn to previous menu")
					self.main_menu()
		else:
			print("You have to choose a correct nummer.")
			print("Press any key to return.")
			input()
			self.player_menu()

	def room_menu(self):
		print("")
		print("***********************")
		print("*     Room Menu       *")
		print("*********************** \n")
		print("1.  Items in")
		print("2.  Available actions")
		print("3.  Return\n\n")
		player_choice = input("Your choice is: ")
		if int(player_choice) >= 1 and int(player_choice) <= 3:
			match str(player_choice):
				case "1":
					print("You are in: \n ")

					self.room_menu()
				case "2":
					print("You are in: \n Next room \n")
					print()
					self.room_menu()
				case "3":
					print("Return to previous menu")
					self.player_menu()
		else:
			print("You have to choose a correct nummer.")
			print("Press any key to return.")
			input()
			self.room_menu()

	def help(self):
		print('''

		Gra Mysterious Game jest prostą grą tekstową. Zadaniem jest przechodzenie między komnatami, znajdowanie przedmiotów i ich użycie.
		Po osiągnięciu ostatniej komnaty i zobyciu skarbu następuje koniec gry. Przedmioty należy zebrać w odpowiedniej kolejności.
		Gracz w każdej chwili może wywołać listę dostępnych opcji poprzez wybranie z menu stosownej pozycji. \n\n

		''')
		print("Press any key to return")
		input()
		self.main_menu()

class Player:
	player_items = []
	def __init__(self, name, health, age):
		self.name = name
		self.health = health
		self.age = age

	def introduce_yourself(self):
		print("\nHello " + self.name)
		print("You are " + str(self.age) + " years old. Your health level is now " + str(self.health) + ".")
		print("Let's play the game. \n")


class Room:
	def __init__(self, name):
		self.name = name

	def current_room(self):
		pass

	def next_room(self):
		pass

	def prev_room(self):
		pass

class Start_room(Room):
	def __init__(self, name):
		super().__init__(name)
		self.start_room_items = ['Magic key','Magic bootle','Basket']

	def current_room(self):
		return self.name
	
	def show_items(self):
		for item in self.start_room_items:
			print(item)

	def use_item(self):
		pass
def main():
	player_name = input("Enter your name: ")
	player_age = input("How old are you? ")
	player = Player(player_name, 100, player_age)
	player.introduce_yourself()
	# menu = Menu()
	# menu.main_menu()
	start_room = Start_room('Hall')
	start_room.show_items()

if __name__ == "__main__":
	main()




