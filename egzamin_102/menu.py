# menu.py

class Menu(object):
	def main_menu(self):
		print('')
		print('----------------------')
		print('     Game Menu       ')
		print('----------------------\n')
		print('1.  Current room')
		print('2.  Items in room')
		print('3.  Available actions')
		print('4.  User items')
		print('5.  Go to the next room')
		print('6.  Return to the previous room')
		print('7.  Help')
		print('8.  Exit \n\n')

	def help_menu(self):
		print('''
		Gra Mysterious Game jest prostą grą tekstową. Zadaniem jest przechodzenie między komnatami, znajdowanie przedmiotów i ich użycie.
		Po osiągnięciu ostatniej komnaty i zobyciu skarbu następuje koniec gry. Przedmioty należy zebrać w odpowiedniej kolejności oraz pilnować poziomu
		życia tak aby nie spadł on do zera gdyż wykonywanie czynności i zbieranie przedmiotów wiąże się z utratą pewnej porcji energi. 
		Gracz w każdej chwili może wywołać listę dostępnych opcji poprzez wybranie z menu stosownej pozycji. \n\n
		''')
		print('Press any key to return')
		input()
		self.main_menu()
