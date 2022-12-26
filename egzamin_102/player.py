# player.py

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