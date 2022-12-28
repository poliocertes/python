# rooms.py

class Room(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def current_room(self):
		return self.name

class First_room(Room):
	def __init__(self, name, description):
		super().__init__(name, description)
		self.room_items = ['1','2','3']

	def actions_in_room(self):
		pass

	def describe_room(self):
		pass

	def show_room_items(self):
		for item in self.room_items:
			print(item)

class Second_room(Room):
	def __init__(self, name, description):
		super().__init__(name, description)
		self.room_items = ['1','2','3']

	def actions_in_room(self):
		pass

	def describe_room(self):
		pass

	def show_room_items(self):
		for item in self.room_items:
			print(item)

class Last_room(Room):
	def __init__(self, name, description):
		super().__init__(name, description)
		self.room_items = ['1','2','3']

	def actions_in_room(self):
		pass

	def describe_room(self):
		pass

	def show_room_items(self):
		for item in self.room_items:
			print(item)