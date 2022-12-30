class Character(object):
	def __init__(self, name, role, energy_level):
		self.name = name
		self.role = role
		self.energy_level = energy_level

	def introduce_yourself(self):
		print('I am ', self.name)
		print('I have a ',self.energy_level,' points of enegry.')

class Hero(Character):
	def __init__(self, name, role, energy_level):
		super().__init__(name, role, energy_level)
		self.items_list = ['Sword']

	def hero_items(self):
		for item in self.items_list:
			print(item)

	def get_item():
		pass
		# item z listy itemów w pokoju na listę itemów usera

class Mag(Character):
	def __init__(self, name, role, energy_level):
		super().__init__(name, role, energy_level)
		self.mag_items_list = ['Magic book']

	def mag_items(self):
		for item in self.mag_items_list:
			print(item)
