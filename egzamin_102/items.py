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
		# jesli wymagany inny item jest dodaj do user list a jak nie to print ze najpierw tamten

	def energy_impact(self, hero):
		hero.energy_impact -=1

	def use_item(self):
		pass
		# if item in self.items_list:....

# class Book(Item):
# 	def __init__(self,name,energy_impact):
# 		super().__init__(name,energy_impact)
	
# 	def item_requirements(self):
# 		pass

# 	def energy_impact(self, hero):
# 		hero.energy_impact +=1

# 	def use_item(self):
# 		pass
# 		# if item in self.items_list:....

# class Bottle(Item):
# 	def __init__(self,name,energy_impact):
# 		super().__init__(name,energy_impact)
	
# 	def item_requirements(self):
# 		pass

# 	def energy_impact(self, hero):
# 		hero.energy_impact -=1

# 	def use_item(self):
# 		pass
# 		# if item in self.items_list:....