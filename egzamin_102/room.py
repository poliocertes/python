# room.py

class Room:
	def __init__(self, name):
		self.name = name

	def go_to_next_room(self):
		pass

	def go_to_prev_room(self):
		pass

class Start_room(Room):
	def __init__(self, name):
		super().__init__(name)
		self.start_room_items = ['Magic key','Magic bootle','Basket']

	def show_items(self):
		for item in self.start_room_items:
			print(item)

	def current_room(self):
		print('Nie działa')

	def use_item(self):
		pass