# rooms.py

class Room(object):
	def __init__(self, name):
		self.name = name

	def current_room(self):
		return self.name

	def next_room(self):
		pass


class First_room(Room):
	def __init__(self, name):
		super().__init__(name)
		self.room_items = ['Książka','Magiczny klucz']

	def actions_in_room(self):
		pass

	def describe_room(self):
		print('''
				W tym miejscu zaczyna się gra. 
			''')

	def show_room_items(self):
		for item in self.room_items:
			print(item)

class Second_room(Room):
	def __init__(self, name):
		super().__init__(name)
		self.room_items = ['1','2','3']

	def actions_in_room(self):
		pass

	def describe_room(self):
		print('''
				Połowa misji. 
			''')

	def show_room_items(self):
		for item in self.room_items:
			print(item)

class Last_room(Room):
	def __init__(self, name):
		super().__init__(name)
		self.room_items = ['1','2','3']

	def actions_in_room(self):
		pass

	def describe_room(self):
		print('''
				Jesteś o krok od sukcesu.
			''')

	def show_room_items(self):
		for item in self.room_items:
			print(item)