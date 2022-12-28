class Character(object):
	def __init__(self, name, role):
		self.name = name
		self.role = role

	def introduce_yourself(self):
		print("I'm " + self.name)

class Hero(Character):
	def __init__(self, name, role):
		super().__init__(name, role)
		self.items_list = ['Sword']

	def hero_items(self):
		for item in self.items_list:
			print(item)

class Mag(Character):
	def __init__(self, name, role):
		super().__init__(name, role)

	def mag_items(self):
		pass
