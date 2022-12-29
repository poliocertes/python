class Messages:
	def first_room(self):
		print('''Jesteś w pierwszej komnacie. Aby pójść dalej musisz zebrać potrzebne przedmioty. Potrzebne są klucz i książka. Użyj komend z menu aby zdobyć potrzebne Ci rzeczy. \n''')
		print("Wciskając dowolny klawisz wracasz do menu.")
		input()


	def next_room(self):
		print('''
			Idziemy dalej. Czas na kolejną komnatę. 
			''')
		print("Wciskając dowolny klawisz wracasz do menu.")
		input()

	def prev_room(self):
		print('''
			Wracamy do poprzedniej komnaty.
			''')
		print("Wciskając dowolny klawisz wracasz do menu.")
		input()
