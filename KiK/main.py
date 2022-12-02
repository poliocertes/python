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
scores = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
click_counter = 1


def interface():
	buttons_area.pack(side=TOP, expand=False, fill=BOTH)
	grid = Frame(buttons_area, background="red")
	button = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="1", column="1", padx=1, pady=1)
	button = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="1", column="2", padx=1, pady=1)
	button = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="1", column="3", padx=1, pady=1)
	button = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="2", column="1", padx=1, pady=1)
	button = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="2", column="2", padx=1, pady=1)
	button = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="2", column="3", padx=1, pady=1)
	button = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="3", column="1", padx=1, pady=1)
	button = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="3", column="2", padx=1, pady=1)
	button = Button(grid, text="", height= 15, width=30, bg=color, activebackground=color_2, fg='white', font=button_font, command=mark).grid(row="3", column="3", padx=1, pady=1)
	grid.pack()


def draw_symbol():
	choice = random.randint(0, 1)
	return choice


def mark():
	global click_counter
	if click_counter == 1:
		print(draw_symbol())
		click_counter += 1
	else:
		if click_counter % 2 == 0:
			click_counter += 1
			print("0")
		else:
			click_counter += 1
			print("x")


def logic():
	pass


def main():
	interface()
	mainloop()


if __name__ == "__main__":
	main()