# Egzamin_102

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
		print("1.  Items")
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
		Po osiągnięciu ostatniej komnaty i zobyciu skarbu następuje koniec gry.
		Gracz w każdej chwili może wywołać listę dostępnych opcji poprzez wybranie z menu stosownej pozycji. \n\n 
		
		''')
		print("Press any key to return")
		input()
		self.main_menu()

class Room:
	def __init__(self, name):
		self.name = name
		self.rooms = []
		self.items_in_room = []

	def describe_room(self):
		print("You are in" + self.name)
		for item in self.items_in_room:
			print("Available items:" + item)

class Hall(Room):
	def __init__(self, name):
		super().__init__(name)

class Item:
	def __init__(self, name, function):
		self.name = name
		self.function = function

	def item_function(self):
		return self.function


def main():
	menu = Menu()
	menu.main_menu()



if __name__ == "__main__":
	main()
