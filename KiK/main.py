from tkinter import *
from tkinter import font as tkFont
import random

window = Tk()
window.title("Kółko i krzyżyk")
window.geometry('670x670+500+300')
window.configure(bg="blue")
buttons_area = Frame(window, height=600)
button_font = tkFont.Font(family='Arial Bold', size=8, weight=tkFont.BOLD)
color = "#380A2E"
color_2 = '#8a2be2' 


def interface():
	buttons_area.pack(side=TOP, expand=False, fill=BOTH)
	grid = Frame(buttons_area, background="red")
	button1 = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="1", column="1", padx=1, pady=1)
	button2 = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="1", column="2", padx=1, pady=1)
	button3 = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="1", column="3", padx=1, pady=1)
	button4 = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="2", column="1", padx=1, pady=1)
	button5 = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="2", column="2", padx=1, pady=1)
	button6 = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="2", column="3", padx=1, pady=1)
	button7 = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="3", column="1", padx=1, pady=1)
	button8 = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="3", column="2", padx=1, pady=1)
	button9 = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="3", column="3", padx=1, pady=1)
	grid.pack()

def choose_first_symbol():
	pass

def mark():
	pass

def check_win():
	pass

def main():
	interface()
	mainloop()

if __name__ == "__main__":
	main()