from tkinter import *
from tkinter import font as tkFont
import random

color="cyan"
width = 670
height = 670
x_dis = 300
y_dis = 300
window_location = str(width)+'x'+str(height)+'+'+str(x_dis)+'+'+str(y_dis)
results_table = [['','',''],['','',''],['','','']]

def  interface():
	window = Tk()
	window.title("Kółko i krzyżyk")
	window.geometry(window_location)
	window.configure(bg=color)
	window.resizable(False, False)

def choose_symbol():
	return random.randint(0, 1)

def main():
	interface()
	mainloop()

if __name__ =="__main__":
	main()