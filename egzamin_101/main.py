import random


items = ['papier', 'kamien', 'nozyce']
comp_choice = (random.choice(items))
game = True
print('Gra w Papier, kamien, nozyce')

while game:
	print('MENU')
	print('Masz trzy możliwosci: 1 -> Papier, 2 -> Kamien, 3 -> Nozyce')
	user_choice = input("Dokonaj wyboru: \n")
	if int(user_choice) == 1:
		print('Wybrales papier')
		if comp_choice == 'papier':
			print('Komputer wylosował papier')
			print('REMIS')
		elif comp_choice == 'kamien':
			print('Komputer wylosował kamien')
			print('Wygrywa Gracz')
		else:
			print('Komputer wylosował nozyce')
			print('Wygrywa Komputer')
	elif int(user_choice) == 2:
		print('Wybrales kamien')
		if comp_choice == 'papier':
			print('Komputer wylosował papier')
			print('Wygrywa Komputer')
		elif comp_choice == 'kamien':
			print('Komputer wylosował kamien')
			print('Remis')
		else:
			print('Komputer wylosował nozyce')
			print('Wygrywa Gracz')
	elif int(user_choice) == 3 :
		print('Wybrales nozyce')
		if comp_choice == 'papier':
			print('Komputer wylosował papier')
			print('wygrywa Gracz')
		elif comp_choice == 'kamien':
			print('Komputer wylosował kamien')
			print('Wygrywa Komputer')
		else:
			print('Komputer wylosował nozyce')
			print('Remis')

	print('Chcesz dalej grac?')
	print('1 -> TAK, Kązdy inny klawisz: -> NIE:')
	next_step = input("Moj wybor to: ")
	if next_step == '1':
		game = True
	else:
		game = False

