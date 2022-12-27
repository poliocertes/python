# Egzamin_102

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
		print(
			"Hallo " + self.name + ". You are " + str(self.age) + " years old and you have a " + str(self.power_level) + " points of energy. ")


class Player(Character):
	def __init__(self, name, age, power_level):
		super().__init__(name, age, power_level)


class Mag(Character):
	pass


class Item:
	pass


class Menu:
	pass


def main():
	hero_name = input("Enter your name: ")
	hero_age = input("How old are you? ")
	player = Character(hero_name, hero_age, 100)
	player.introduce_yourself()
	print("Let's play the game. ")
	choice = input()


if __name__ == "__main__":
	main()
