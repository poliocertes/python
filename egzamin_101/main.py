import random

items = ['papier', 'kamien', 'nozyce']

comp_choice = (random.choice(items))

print('Gra w Papier, kamien, nozyce')
print('MENU')
print('1 -> Papier, 2 -> Kamien, 3 -> Nozyce')
print('Wybierz: ')

user_choice = input("Dokonaj wyboru:")


if int(user_choice) == 1:
	print('Wybrales papier')
	if comp_choice == 'papier':
		print('Komputer wylosował papier')
		print('REMIS')
	elif comp_choice == 'kamien':
		print('Komputer wylosował kamien')
		print('Wygrywa Komputer')
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
		print('Wygrywa Komputer')
elif int(user_choice) == 'nozyce':
	print('Wybrales nozyce')
	if comp_choice == 3:
		print('Komputer wylosował papier')
		print('Wygrywa Gracz')
	elif comp_choice == 'kamien':
		print('Komputer wylosował kamien')
		print('Wygrywa Komputer')
	else:
		print('Komputer wylosował nozyce')
		print('Remis')
