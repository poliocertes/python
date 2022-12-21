# Egzamin_102

class Menu:
	def main_menu(self):
		print("")
		print("***********************")
		print("*   Mysterious Game   *")
		print("*********************** \n")
		print("1.New game")
		print("2.About a game")
		print("3.Exit \n\n")
		data = input('Your choice is: \n')
		if int(data) >= 1 and int(data) <= 6:
			match str(data):
				case "1":
					self.player_menu()
				case "2":
					self.help()
				case "3":
					print("Press any key to exit.")
					input()
					print("\n")
		else:
			print("You have to choose a correct nummer.")
			print("Press any key to return.")
			input()
			self.main_menu()

	def player_menu(self):
		print("***********************")
		print("*     Player Menu       *")
		print("*********************** \n")
		print("  Options: \n")
		print("1.  Current room")
		print("2.  Next room")
		print("3.  Previous room")
		print("4.  Room menu")
		print("5.  Return")
		player_choice = input("Your choice is: \n\n")
		if int(player_choice) >= 1 and int(player_choice) <= 6:
			match str(player_choice):
				case "1":
					print("You are in: \n ")

					self.player_menu()
				case "2":
					print("You are in: \n Next room \n")
					print()
					self.player_menu()
				case "3":
					print("You are in: \n Previous room: \n")
					print()
					self.player_menu()
				case "4":
					print("")
					self.room_menu()
				case "5":
					print("Return to previous menu")
					self.main_menu()
		else:
			print("You have to choose a correct nummer.")
			print("Press any key to return.")
			input()
			self.player_menu()

	def room_menu(self):
		print("***********************")
		print("*     Room Menu       *")
		print("*********************** \n")
		print("1.  Items")
		print("2.  Available actions")
		print("3.  Return")
		player_choice = input("Your choice is: \n\n")
		if int(player_choice) >= 1 and int(player_choice) <= 3:
			match str(player_choice):
				case "1":
					print("You are in: \n ")

					self.player_menu()
				case "2":
					print("You are in: \n Next room \n")
					print()
					self.player_menu()
				case "3":
					print("Return to previous menu")
					self.player_menu()
		else:
			print("You have to choose a correct nummer.")
			print("Press any key to return.")
			input()
			self.player_menu()


	def help(self):
		print('''	
		
		Gra Mysterious Game jest prostą grą tekstową. Zadaniem jest przechodzenie między komnatami, znalezienie przedmiotów i ich uzycie.
		Po osiągnięciu ostatniej komnaty i zobyciu skarbu następuje koniec gry.
		Gracz w każdej chwili może wywołać listę dostępnych opcji poprzez wybranie z menu stosownej opcji. \n\n 
		
		''')
		print("Press any key to return")
		input()
		self.main_menu()

class Room:
	def __init__(self, name, current_room, next_room, prev_room, task):
		self.name = name
		self.current_room = current_room
		self.next_room = next_room
		self.prev_room = prev_room
		self.task = task

	def room_task(self):
		print("You have to:" + self.task)

	def describe(self):
		print("You are in:" + self.name)
		print("Yaour task is" + str(self.room_task()))

	def current_room(self):
		return self.current_room()


class Start_room(Room):
	def __init__(self, name, current_room, next_room, task):
		super().__init__(name, current_room, next_room, task)
		self.available_items = []
	def available_items(self):
		for items in self.available_items:
			print(items)
class Water_room(Room):
	pass
class Fire_room(Room):
	pass
class Sezam(Room):
	pass
class Character:
	pass
class Player(Character):
	pass
class Mag(Character):
	pass
class Item:
	pass
class Watter_key(Item):
	pass
class Fire_key(Item):
	pass
class Gem(Item):
	pass
def main():
	menu = Menu()
	menu.main_menu()
	start_room = Start_room("Hall", "Start room", "Watter room", "go to the next")

if __name__ == "__main__":
	main()
