from tkinter import *
from tkinter import font as tkFont

window = Tk()
window.title("Kółko i krzyżyk")
window.geometry('670x670+500+300')
window.configure(bg="blue")
buttons_area = Frame(window, height=600)
button_font = tkFont.Font(family='Arial Bold', size=8, weight=tkFont.BOLD)

def interface():
	buttons_area.pack(side=TOP, expand=False, fill=BOTH)
	grid = Frame(buttons_area, background="red")
	Button(grid, text="", height= 15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command ="").grid(row="1", column="1", padx=1, pady=1)
	Button(grid, text="", height= 15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command ="").grid(row="1", column="2", padx=1, pady=1)
	Button(grid, text="", height= 15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="1", column="3", padx=1, pady=1)
	Button(grid, text="", height= 15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="2", column="1", padx=1, pady=1)
	Button(grid, text="", height= 15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="2", column="2", padx=1, pady=1)
	Button(grid, text="", height= 15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="2", column="3", padx=1, pady=1)
	Button(grid, text="", height= 15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="3", column="1", padx=1, pady=1)
	Button(grid, text="", height= 15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="3", column="2", padx=1, pady=1)
	Button(grid, text="", height= 15, width=30, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command="").grid(row="3", column="3", padx=1, pady=1)
	grid.pack()




def main():
	interface()
	mainloop()

if __name__ == "__main__":
	main()