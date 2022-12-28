# items.py

class Item(object):
	def __init__(self, name, energy_impact):
		self.name = name
		self.energy_impact = energy_impact

class Key(Item):
	def __init__(self,name,energy_impact):
		super().__init__(name,energy_impact)

	def item_requirements(self):
		pass

	def energy_impact(self):
		pass

class Book(Item):
	def __init__(self,name,energy_impact):
		super().__init__(name,energy_impact)
	pass

class Bottle(Item):
	def __init__(self,name,energy_impact):
		super().__init__(name,energy_impact)
	pass