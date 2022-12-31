# ---egzamin_102--- #
import time

class Room:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def room_name(self):
        print('\nYou are in: ')
        print(self.name)

    def location(self):
        return self.location


class First_chamber(Room):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.items = ['Magic Key', 'Magic Book']

    def show_items(self):
        print(f'\nPrzedmioty dostępne w {self.name}: ')
        for item in self.items:
            print(item)


class Second_chamber(Room):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.items = ['Magic Bottle', 'Secret Key']

    def show_items(self):
        print(f'\nPrzedmioty dostępne w {self.name} : ')
        for item in self.items:
            print(item)


class Last_chamber(Room):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.items = ['Gem']

    def show_items(self):
        print(f'\nPrzedmioty dostępne w {self.name} : ')
        for item in self.items:
            print(item)


class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def character_name(self):
        print(self.name)

    def character_role(self):
        print(self.role)


class Player(Character):
    def __init__(self, name, role):
        super().__init__(name, role)
        self.player_items = ['Sword']

    def show_items(self):
        print(f'{self.name} items :')
        for item in self.player_items:
            print(item)

    def use_item(self):
        pass

    def get_item(self):
        pass


class Mag(Character):
    def __init__(self, name, role):
        super().__init__(name, role)
        self.mag_items = ['Magic']

    def show_items(self):
        print(f'{self.name} items :')
        for item in self.mag_items:
            print(item)  

class Story:
    def start_game(self):
        print('\n**** ZNAJDŹ SKARB ****')
        print('''   
        Witaj w grze "Znajdź skarb". Twoja przygoda zaczyna się w pierwszej z trzech komnat. 
        Musisz zbierać przedmioty potrzebne do tego, aby móc pójść dalej. 
        Zaczynamy grę? t/n \n''')
        

    def room_one(self):
        print('''
        Jesteś w pierwszej komnacie. Musisz najpierw wziąć magiczny klucz, który pozwoli Ci otworzyć przejście
        do drugiej komnaty.Po znalezieniu klucza nie ruszaj od razu dalej. Będziesz potrzebował czegoś jeszcze... 
        Co chcesz zrobić? 
        1. Powrót
        2. Dostępne przedmioty.\n''')
        
            

    def room_two(self):
        print('''
        Jesteś w drugiej komnacie. Musisz najpierw wziąć magiczny klucz, który pozwoli Ci otworzyć przejście
        do drugiej komnaty.Po znalezieniu klucza nie ruszaj od razu dalej. Będziesz potrzebował czegoś jeszcze... 
        Co chcesz zrobić? 
        1. Powrót
        2. Dostępne przedmioty.\n''')

    def room_three(self):
        print('''
        Jesteś w ostatniej komnacie. Cel już blisko. Musisz najpierw wziąć magiczny klucz, który pozwoli Ci otworzyć przejście
        do drugiej komnaty.Po znalezieniu klucza nie ruszaj od razu dalej. Będziesz potrzebował czegoś jeszcze... 
        Co chcesz zrobić? 
        1. Powrót
        2. Dostępne przedmioty.\n''')

def main():
    first_ch = First_chamber('First Chamber', 1)
    second_ch = Second_chamber('Second Chamber', 2)
    last_ch = Last_chamber('Last Chamber', 3)
    current_room = first_ch
    story = Story()
    story.start_game()
    player_choice = input('Twój wybór :')
    if str(player_choice) == 't':
        story.room_one()
        choice = input("Wybierasz :")
        if int(choice) == 1:
            story.start_game()
        elif int(choice) == 2:
            first_ch.show_items()
            story.room_one()
    elif str(player_choice)=='n':
        print('Trudno. Spróbujemy zagrać następnym razem.')
        print('Poczekaj na wyłączenie się gry.')
        time.sleep(2)
        quit()
    else:
        print('Zła wartość. Spróbuj jeszcze raz. ')
        main()
    


if __name__ == '__main__':
    main()
