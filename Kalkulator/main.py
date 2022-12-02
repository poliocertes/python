from tkinter import * 
from tkinter import font as tkFont


window = Tk()
window.title('Kalkulator')
window.geometry('400x435')
window.resizable(False, False)
text_field = Entry(window, width=44, borderwidth=2, relief=SUNKEN, bg="#0066CC", fg="white", justify='right', insertontime=2)
buttons_area = Frame(window, height=200)


def draw():
	text_field.pack()
	text_field.configure(font=("Arial", 16, "italic"))
	buttons_area.pack(side=TOP, expand=False, fill=BOTH)
	grid = Frame(buttons_area, background="#0066CC")
	button_font = tkFont.Font(family='Arial Bold', size=8, weight=tkFont.BOLD)
	Button(grid, text="1", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=lambda : text_field.insert("end","1")).grid(row="1", column="1", padx=10, pady=10)
	Button(grid, text="2", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=lambda : text_field.insert("end","2")).grid(row="1", column="2", padx=10, pady=10)
	Button(grid, text="3", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=lambda : text_field.insert("end","3")).grid(row="1", column="3", padx=10, pady=10)
	Button(grid, text="C", height= 5, width=4, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=clear).grid(row="1", column="4", padx=10, pady=10, sticky="w")
	Button(grid, text="AC", height= 5, width=4, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=clear_all).grid(row="1", column="4", padx=10, pady=10, sticky="e")
	Button(grid, text="4", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=lambda : text_field.insert("end","4")).grid(row="2", column="1", padx=10, pady=10)
	Button(grid, text="5", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=lambda : text_field.insert("end","5")).grid(row="2", column="2", padx=10, pady=10)
	Button(grid, text="6", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=lambda : text_field.insert("end","6")).grid(row="2", column="3", padx=10, pady=10)
	Button(grid, text="x", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=lambda : text_field.insert("end","*")).grid(row="2", column="4", padx=10, pady=10)
	Button(grid, text="7", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=lambda : text_field.insert("end","7")).grid(row="3", column="1", padx=10, pady=10)
	Button(grid, text="8", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=lambda : text_field.insert("end","8")).grid(row="3", column="2", padx=10, pady=10)
	Button(grid, text="9", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=lambda : text_field.insert("end","9")).grid(row="3", column="3", padx=10, pady=10)
	Button(grid, text="/", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=lambda : text_field.insert("end","/")).grid(row="3", column="4", padx=10, pady=10)
	Button(grid, text="+", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=lambda : text_field.insert("end","+")).grid(row="4", column="1", padx=10, pady=10)
	Button(grid, text="0", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=lambda : text_field.insert("end","0")).grid(row="4", column="2", padx=10, pady=10)
	Button(grid, text="-", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=lambda : text_field.insert("end","-")).grid(row="4", column="3", padx=10, pady=10)
	Button(grid, text="=", height= 5, width=10, bg='blue', activebackground='#0066CC', fg='white', font=button_font, command=results).grid(row="4", column="4", padx=10, pady=10)
	grid.pack()

def clear():
	a = text_field.get()
	text_field.delete(first=len(a)-1,last="end")

def clear_all():
	a = text_field.get()
	text_field.delete(0, "end")

def results():
	if text_field.get() =='':
		pass
	elif text_field.get()[0] == "0":
		if text_field.get()[1] == "":
			text_field.delete(0,"end")
		else:
			pass
	else:
		result = text_field.get()
		result = eval(result)
		text_field.insert("end","=")
		text_field.insert("end",result)

def main():
	draw()
	window.mainloop()

if __name__ == "__main__":
	main()
