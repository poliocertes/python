from tkinter import *
from tkinter import font as tkFont
import random

color="blue"
width = 670
height = 670
window_size = str(width)+'x'+str(height)
results_table = [['','',''],['','',''],['','','']]

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

	def choose_first_symbol(self):
		return random.randint(0, 1)

	def mark_button():
		pass

	def check_results():
		pass

def main():
	runnig = True
	game = Game()
	game.interface()

if __name__ =="__main__":
	main()