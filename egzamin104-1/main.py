# sortowanie babelkowe z GUI- python
# Z2J Python 104-l01

from tkinter import *
from tkinter import font as tkFont

class Bubble_sort:
	def end_menu(self):
		print('Co dalej ?')
		print('1. Kolejne sortowanie ')
		print('2. Wyjście ')
		user_input = input()
		match str(user_input):
			case '1':
				main()

			case '2':
				quit()

			case other:
				print('Zły wybór. Wracamy do gry.')
				main()

	def draw(self):
		window = Tk()
		window.title('Buble Sort')
		title_frame = Frame(window, height=200)
		window.geometry('600x400')
		window.resizable(False, False)
		window.configure(bg='blue')
		lbl = Label(window, text='Podaj ciąg liczb do posortowania. Rozdziel je przecinkami.', bg='blue', fg='white', padx=150, pady=30)
		lbl.grid()
		title_frame.grid()
		window.mainloop()

def main():
	bub_sort = Bubble_sort()
	bub_sort.draw()

	print('Sortowanie babelkowe Python')
	items_list = []
	user_input = input('Podaj liczby które chcesz posortować rozdzielając je przecinkiem: \n').split(',')
	items_list.extend(user_input)
	if len(items_list) > 1:
		items_list = [int(x) for x in items_list]
		list_lenght = len(items_list) - 1
		print('\nOriginalna lista: ', items_list)
		for i in range(0, list_lenght):
			for j in range(0, list_lenght - i):
				if items_list[j] > items_list[j + 1]:
					temporary_list_item_value = items_list[j]
					items_list[j] = items_list[j + 1]
					items_list[j + 1] = temporary_list_item_value
		print('Posortowana lista: ', items_list, '\n')
		bub_sort.end_menu()
	else:
		print('Lista jest pusta.')
		print('Musisz dodać przynajmniej dwie liczby. \n')
		main()


if __name__ == '__main__':
	main()
