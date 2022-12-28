# Egzamin_102
import time

rooms = ['Hall', 'Chamber of magic', 'Sezam']


class Menu:
	def menu(self):
		print("")
		print("***********************")
		print("*     Game Menu       *")
		print("*********************** \n")
		print("1.  Current room")
		print("2.  Items in room")
		print("3.  Available actions")
		print("4.  User items")
		print("5.  Next room")
		print("6.  Previous room")
		print("7.  Help")
		print("8.  Exit \n\n")
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
					print("Player items: ")
					Hero.show_hero_items()
				case "5":
					pass
				case "6":
					pass
				case "7":
					print("About a game")
					self.help()
				case "8":
					print("Exit the game.")
					time.sleep(2)
					quit()
		else:
			print("You have to choose a correct nummer.")
			print("Press any key to return.")
			input()
			self.menu()

	def help(self):
		print('''
		Gra Mysterious Game jest prostą grą tekstową. Zadaniem jest przechodzenie między komnatami, znajdowanie przedmiotów i ich użycie.
		Po osiągnięciu ostatniej komnaty i zobyciu skarbu następuje koniec gry. Przedmioty należy zebrać w odpowiedniej kolejności oraz pilnować poziomu
		życia tak aby nie spadł on do zera gdyż wykonywanie czynności i zbieranie przedmiotów wiąże się z utratą pewnej porcji energi. 
		Gracz w każdej chwili może wywołać listę dostępnych opcji poprzez wybranie z menu stosownej pozycji. \n\n
		''')
		print("Press any key to return")
		input()
		self.menu()


class Room:
	def __init__(self, name):
		self.name = name

	def current_room(self):
		print(self.name)

	def next_room(self):
		pass

	def prev_room(self):
		pass

class Hall(Room):
	pass

class Chamber_of_Magic(Room):
	pass

class Sezam(Room):
	pass

class Character:
	def __init__(self, name, health, age):
		self.name = name
		self.health = health
		self.age = age

	def introduce_yourself(self):
		print("\nHello " + self.name)
		print("You are " + str(self.age) + " years old. Your health level is now " + str(self.health) + ".")
		print("Let's play the game. \n")


class Hero(Character):
	def __init__(self, name, health, age):
		super().__init__(name, health, age)
		self.hero_items = ['Sword']

	def show_hero_items(self):
		print(self.name + '\n items: \n')
		for item in self.hero_items:
			print(item)


class Mag(Character):
	def __init__(self, name, health, age):
		super().__init__(name, health, age)
		self.mag_items = ['Magic key']



class Item:
	def __init__(self, name, energy_impact):
		self.name = name
		self.energy_impact = energy_impact

	def item_name(self):
		return self.name


def main():
	hero_name = input("Enter your name: ")
	while not hero_name.isalpha():
		print("Only letters are allowed")
		hero_name = input("Enter a correct player name: ")
	hero_age = input("How old are you? ")
	while not hero_age.isnumeric():
		print("Enter a number")
		hero_age = input("Enter again how old are you: ")
	hero = Hero(hero_name, 100, hero_age)
	hero.introduce_yourself()
	menu = Menu()
	menu.menu()


if __name__ == "__main__":
	main()




