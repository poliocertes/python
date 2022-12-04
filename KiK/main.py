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

	def  interface(self):
		window = Tk()
		window.title("Kółko i krzyżyk")
		window.geometry(window_size)
		window.configure(bg=color)
		window.resizable(False, False)
		mainloop()

	def board(self):
		pass

	def choose_first_symbol(self):
		return random.randint(0, 1)

	def mark_button(self):
		pass

	def check_results(self):
		if res_table[0][0]==res_table[0][1]==res_table[0][2] or res_table[1][0]==res_table[1][1]==res_table[1][2] or res_table[2][0]==res_table[2][1]==res_table[2][2] or
			res_table[0][0]==res_table[1][0]==res_table[2][0] or res_table[0][1]==res_table[1][1]==res_table[2][1] or res_table[0][2]==res_table[1][2]==res_table[2][2] or
			res_table[0][0]==res_table[1][1]==res_table[2][2]or res_table[0][2]==res_table[1][1]==res_table[2][0]:
			pass

def main():
	runnig = True
	game = Game()
	game.interface()

if __name__ =="__main__":
	main()