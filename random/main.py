import random
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Zgaduj Zgadula')
window.geometry('570x370+700+500')
window.resizable(False, False)


color = "green"
color2 = "blue"
color3 = "white"
window.configure(background=color2)
grid = Frame(window, background=color, bd=1)
tries = 0
random_number = 0


def draw_nummer():
    global random_number
    if not from_field.get() and to_field.get():
        messagebox.showinfo(title="Error", message='Podaj obie liczby!')
    else:
        begin_nummer = int(from_field.get())
        end_nummer = int(to_field.get())
        random_number = random.randint(begin_nummer, end_nummer)
        draw_button["state"] = "disabled"


def check_number():
    global tries
    user_number = int(add_number_field.get())

    if user_number < random_number:
        result_field.delete(0, "end")
        result_field.configure(fg="red")
        result_field.insert("end", "Za mało!")
        tries += 1
        number_of_tries_field.delete(0, "end")
        number_of_tries_field.insert("end", str(tries))
        add_number_field.delete(0, "end")
    elif user_number > random_number:
        result_field.delete(0, "end")
        result_field.configure(fg="red")
        result_field.insert("end", "Za dużo!")
        tries += 1
        number_of_tries_field.delete(0, "end")
        number_of_tries_field.insert("end", str(tries))
        add_number_field.delete(0, "end")
    else:
        result_field.delete(0, "end")
        result_field.configure(fg="green")
        result_field.insert("end", "To ta liczba. Brawo!")
        tries += 1
        number_of_tries_field.delete(0, "end")
        number_of_tries_field.insert("end", str(tries))
        check_result_button.configure(text="Koniec", bg="red", command=game_over)


def game_over():
    window.quit()
    window.destroy()


from_label = Label(grid, text="Od", bg=color)
to_label = Label(grid, text="Do", bg=color)
draw_button = Button(grid, text="Losuj", height= 2, width=20, bg=color2, activebackground=color,
                     fg='white', command=draw_nummer)
from_field = Entry(grid, width=25, bg=color3, )
to_field = Entry(grid, width=25, bg=color3, )
add_number_label = Label(grid, text="Podaj liczbę", bg=color)
number_of_tries_label = Label(grid, text="Liczba prób", bg=color)
result_label = Label(grid, text="Wynik", bg=color)
add_number_field = Entry(grid, width=25, bg=color3)
number_of_tries_field = Entry(grid, width=25, bg=color3, )
result_field = Entry(grid, width=25, bg=color3, )
check_result_button = Button(grid, text="Sprawdź", command=check_number, height= 2, width=20, bg=color2,
                             activebackground=color, fg='white')

from_label.grid(row=1, column=1, padx=30, pady=10)
to_label.grid(row=1, column=3, padx=30, pady=10)
draw_button.grid(row=3, column=2, padx=30, pady=30)
from_field.grid(row=2, column=1, padx=10, pady=10)
to_field.grid(row=2, column=3, padx=10, pady=10)
add_number_label.grid(row=4, column=1, padx=30, pady=10)
number_of_tries_label.grid(row=4, column=2, padx=30, pady=10)
result_label.grid(row=4, column=3, padx=30, pady=10)
add_number_field.grid(row=5, column=1, padx=10, pady=10)
number_of_tries_field.grid(row=5, column=2, padx=10, pady=10)
result_field.grid(row=5, column=3, padx=10, pady=10)
check_result_button.grid(row=6, column=2, padx=30, pady=30)

grid.pack()
window.mainloop()
