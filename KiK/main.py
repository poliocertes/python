from tkinter import *
from tkinter import font as tkFont
import random

color="blue"
width = 670
height = 670
window_size = str(width)+'x'+str(height)
res_table = [['','',''],['','',''],['','','']]

class Game:

	def __init__(self):
		self.width = width
		self.height = height
		self.color = color

	def board(self):
		button_font = tkFont.Font(family='Arial Bold', size=8, weight=tkFont.BOLD)
		Button(grid, text="", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="1", column="1", padx=10, pady=10)
		Button(grid, text="", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="1", column="2", padx=10, pady=10)
		Button(grid, text="", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="1", column="3", padx=10, pady=10)
		Button(grid, text="", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="2", column="1", padx=10, pady=10)
		Button(grid, text="", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="2", column="2", padx=10, pady=10)
		Button(grid, text="", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="2", column="3", padx=10, pady=10)
		Button(grid, text="", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="3", column="1", padx=10, pady=10)
		Button(grid, text="", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="3", column="2", padx=10, pady=10)
		Button(grid, text="", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="3", column="3", padx=10, pady=10)
		

	def  interface(self):
		window = Tk()
		window.title("Kółko i krzyżyk")
		window.geometry(window_size)
		window.configure(bg=self.color)
		window.resizable(False, False)
		mainloop()

	def choose_first_symbol(self):
		return random.randint(0, 1)

	def mark_button(self):
		pass

	def check_results(self):
		if (res_table[0][0]==res_table[0][1]==res_table[0][2] or res_table[1][0]==res_table[1][1]==res_table[1][2] or res_table[2][0]==res_table[2][1]==res_table[2][2] or
			res_table[0][0]==res_table[1][0]==res_table[2][0] or res_table[0][1]==res_table[1][1]==res_table[2][1] or res_table[0][2]==res_table[1][2]==res_table[2][2] or
			res_table[0][0]==res_table[1][1]==res_table[2][2]or res_table[0][2]==res_table[1][1]==res_table[2][0]):
			pass

def main():
	game = Game()
	game.interface()

if __name__ =="__main__":
	main()