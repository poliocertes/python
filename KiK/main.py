from tkinter import *
from tkinter import font as tkfont
import random

color = "green"
width = 670
height = 670
window_size = str(width) + 'x' + str(height) + '+' + str(500) + '+' + str(500)
res_table = [['', '', ''], ['', '', ''], ['', '', '']]
counter = 0


class Game:

	def __init__(self):
		self.width = width
		self.height = height
		self.color = color

	def choose_symbol(self):
		choosen_symbol = random.randint(0, 1)
		return choosen_symbol
	
	def mark_field(self):
		va = self.choose_symbol()
		global counter
		if counter == 0:
			if va == 0:
				counter += 1
			elif va == 1:
				counter += 1
		elif counter > 0:
			counter += 1
			print(counter)

	def check_results(self):
		pass

	def board(self):
		window = Tk()
		window.title("Kółko i krzyżyk")
		window.geometry(window_size)
		window.configure(bg=color)
		window.resizable(False, False)
		button_font = tkfont.Font(family='Arial Bold', size=8, weight=tkfont.BOLD)
		Button(window, text="", height=15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=self.mark_field).grid(row=0, column=0, padx=1, pady=1)
		Button(window, text="", height=15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=self.mark_field).grid(row=0, column=1, padx=1, pady=1)
		Button(window, text="", height=15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=self.mark_field).grid(row=0, column=2, padx=1, pady=1)
		Button(window, text="", height=15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=self.mark_field).grid(row=1, column=0, padx=1, pady=1)
		Button(window, text="", height=15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=self.mark_field).grid(row=1, column=1, padx=1, pady=1)
		Button(window, text="", height=15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=self.mark_field).grid(row=1, column=2, padx=1, pady=1)
		Button(window, text="", height=15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=self.mark_field).grid(row=2, column=0, padx=1, pady=1)
		Button(window, text="", height=15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=self.mark_field).grid(row=2, column=1, padx=1, pady=1)
		Button(window, text="", height=15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=self.mark_field).grid(row=2, column=2, padx=1, pady=1)

def main():
	game = Game()
	game.board()
	game.choose_symbol()

	mainloop()
	


if __name__ == "__main__":
	main()
