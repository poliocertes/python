import time


class Story:

	def start_game(self):
		print('\n**** ZNAJDŹ SKARB ****')
		print('''   
			Witaj w grze "Znajdź skarb". Twoja przygoda zaczyna się w pierwszej z trzech komnat. 
			Musisz zbierać przedmioty potrzebne do tego, aby móc pójść dalej. 
			Zaczynamy grę? t/n \n''')


	def room_one(self):
		print('''
			Jesteś w pierwszej komnacie. Musisz najpierw wziąć magiczny klucz, który pozwoli Ci otworzyć przejście
			do drugiej komnaty.Po znalezieniu klucza nie ruszaj od razu dalej. Będziesz potrzebował czegoś jeszcze... 
			Co chcesz zrobić? 
			
			1. Dostępne przedmioty.
			2. Zabierz przedmiot.
			3. Użyj przedmiot.
			4. Następna komnata.
			5. Powrót\n''')


	def room_two(self):
		print('''
			Jesteś w drugiej komnacie. Musisz najpierw wziąć magiczny klucz, który pozwoli Ci otworzyć przejście
			do drugiej komnaty.Po znalezieniu klucza nie ruszaj od razu dalej. Będziesz potrzebował czegoś jeszcze... 
			Co chcesz zrobić? 
			
			1. Dostępne przedmioty.
			2. Zabierz przedmiot.
			3. Użyj przedmiot.
			4. Następna komnata.
			5. Powrót\n''')


	def room_three(self):
		print('''
			Jesteś w ostatniej komnacie. Cel już blisko. Musisz najpierw wziąć magiczny klucz, który pozwoli Ci otworzyć przejście
			do drugiej komnaty.Po znalezieniu klucza nie ruszaj od razu dalej. Będziesz potrzebował czegoś jeszcze... 
			Co chcesz zrobić? 
			
			1. Dostępne przedmioty.
			2. Zabierz przedmiot.
			3. Użyj przedmiot.
			4. Powrót\n''')

	def game_over(self):
		print('''
			Tym sposobem doszedłeś drogi graczu do końca zabawy. Wciśnij dowolny klawisz aby zakończyć gre. Dzięki za 
			spedzony wspólnie czas.
		''')
		input()
		time.sleep(3)