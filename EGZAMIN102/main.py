# --- egzamin_102 by Jacek --- #
import time


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
            W magicznej ksiazce przeczytasz jak powinienes dalej postapic. Kazda czynnosc odbiera Ci troche mocy...
            Co chcesz zrobić? 
            
            1. Dostępne przedmioty.
            2. Zabierz przedmiot.
            3. Użyj przedmiot.
            4. Następna komnata.
            5. Powrót\n''')


    def room_two(self):
        print('''
            Jesteś w drugiej komnacie. Powienies odnalezc sekretny klucz, który pozwoli Ci otworzyć przejście
            do kolejnej juz ostatniej komnaty. Po znalezieniu klucza nie ruszaj od razu dalej. Będziesz potrzebował czegoś jeszcze... 
            Tracisz punkty energii i moze je odnowic gdy uzyjesz butelki z magicznym plynem. Zycze powodzenia w poszukiwaniach.
            Co robimy dalej? 
            
            1. Dostępne przedmioty.
            2. Zabierz przedmiot.
            3. Użyj przedmiot.
            4. Następna komnata.
            5. Powrót\n''')


    def room_three(self):
        print('''
            Jesteś w ostatniej komnacie. Cel już blisko. Niewiele przed Toba. Sprawdzajac dostepne przedmioty pamietaj 
            aby najpierw porozmawiac z Magiem, ktory tu na Ciebie od poczatku czeka i chce Ci cos powiedziec. Ostatni zebrany elememnt odbierze Ci tez troche mocy.
            Twoj wybor? 
            
            1. Dostępne przedmioty.
            2. Zabierz przedmiot.
            3. Użyj przedmiot.
            4. Koniec przygody\n''')

    def game_over(self):
        print('''
            Tym sposobem doszedłeś drogi graczu do końca zabawy. Zdobyles skarb. Moje gratulacje. Wciśnij dowolny klawisz aby zakończyć gre. Dzięki za 
            spedzony wspólnie czas.
        ''')
        input()
        time.sleep(3)


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
        print(f'\nPrzedmioty dostępne w {self.name}: \n')
        for item in self.items:
            print(item)   


class Second_chamber(Room):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.items = ['Magic Bottle', 'Secret Key']

    def show_items(self):
        print(f'\nPrzedmioty dostępne w {self.name} : \n')
        for item in self.items:
            print(item)


class Last_chamber(Room):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.items = ['Gem']

    def show_items(self):
        print(f'\nPrzedmioty dostępne w {self.name} : \n')
        for item in self.items:
            print(item)


class Character:
    def __init__(self, name, role, energy_level):
        self.name = name
        self.role = role
        self.energy_level = energy_level

    def character_name(self):
        print(self.name)

    def character_role(self):
        print(self.role)

    def energy_level(self):
        return self.energy_level


class Player(Character):
    def __init__(self, name, role, energy_level):
        super().__init__(name, role, energy_level)
        self.player_items = []

    def show_items(self):
        if len(player.player_items) > 0:
            for item in self.player_items:
                print(item)
        else:
            print('Brak przedmiotów')


class Mag(Character):
    def __init__(self, name, role, energy_level):
        super().__init__(name, role, energy_level)
        self.mag_items = ['Magic']

    def say_instruction(self):
        print('''Witaj Graczu. Jestes u kresu wedrowki. Przed Toba skarb. Aby ukonczyc wyzwanie musisz miec wystarczajaco duzy zapas energii.
            
            ''')
        time.sleep(7)


story = Story()
first_chamber = First_chamber('First Chamber', 1)
second_chamber = Second_chamber('Second Chamber', 2)
last_chamber = Last_chamber('Last Chamber', 3)
player = Player('Joe', 'player', 10)
mag = Mag('Merlin','mag',100)


def room_one_menu():
    time.sleep(1)
    story.room_one()
    room_one_user_input = input('Co chcesz teraz zrobić ? ')

    if room_one_user_input.isnumeric:
        if 5 > int(room_one_user_input) >0:
            match str(room_one_user_input):
                case '1':
                    first_chamber.show_items()
                    input("\nDowolny klawisz aby wrócić.")
                    room_one_menu()
                case '2':
                    print('Masz w komnacie dostepne dwa przedmioty:')
                    first_chamber.show_items()
                    print('\n')
                    if len(first_chamber.items) > 0:
                        choosen_item = input('Ktory przedmiot chcesz wziac? Wybór jako cyfra dla przedmiotów w kolejności od góry. ')
                        if choosen_item.isnumeric:
                            match str(choosen_item):
                                case '1':
                                    taken_item = first_chamber.items[0]
                                    player.player_items.append(first_chamber.items[0])
                                    first_chamber.items.remove(first_chamber.items[0])
                                    print('Zabierasz ', taken_item)
                                    room_one_menu()
                                case '2':
                                    taken_item = first_chamber.items[1]
                                    player.player_items.append(first_chamber.items[1])
                                    first_chamber.items.remove(first_chamber.items[1])
                                    print('Zabierasz ', taken_item)
                                    room_one_menu()
                        else:
                            print('Tylko cyfry jako wybór.')
                            room_one_menu()

                    else:
                        print('Bark dostępnych przedmiotów.')
                        room_one_menu()

                case '3':
                    print('\nPlayer', player.name,' posiada:\n')
                    player.show_items()
                    if len(player.player_items) != 0:
                        choosen_user_item = input('Czego chcesz uzyc :')
                        match str(choosen_user_item):
                            case '1':
                                print('Uzywam...', player.player_items[0])
                                player.energy_level -= 2
                                player.player_items.remove(player.player_items[0])
                                print('Poziom mocy :', player.energy_level)
                                room_one_menu()
                            case '2':

                                print('Uzywam...', player.player_items[1])
                                room_one_menu()
                    else:
                        print('Musisz poszukać czegoś w komnatach...')
                        room_one_menu()
                case '4':
                    if len(player.player_items) > 0:
                        room_two_menu()
                    else:
                        print('Musisz zabrać stąd coś ze sobą aby móc iśc dalej. :) ')
                        room_one_menu()
                case '5':
                    story.start_game()
        else:
            print('Zły wybór. Spróbuj cyfr z przedziału od 1 do 5')
            room_one_menu()
    else:
        print('Tylko cyfry bohaterze.')


def room_two_menu():
    time.sleep(1)
    story.room_two()
    room_two_user_input = input('No i co robimy dalej? ')
    match str(room_two_user_input):
        case '1':
            second_chamber.show_items()
            input("\nDowolny klawisz aby wrócić.")
            room_two_menu()
        case '2':
            pass
            # zabierz przedmiot
        case '3':
            pass
             # uzyj przedmiot
        case '4':
            room_three_menu()
        case '5':
            room_one_menu()


def room_three_menu():
    time.sleep(1)
    mag.say_instruction()
    story.room_three()
    room_three_user_input = input('No i? ')
    match str(room_three_user_input):
        case '1':
            last_chamber.show_items()
            input("\nDowolny klawisz aby wrócić.")
            room_three_menu()
        case '2':
            pass
            # zabierz przedmiot
        case '3':
            pass
             # uzyj przedmiot
        case '4':
            time.sleep(2)
            story.game_over()


def main():
    print('Imie gracza: ')
    player_name = player.character_name()
    story.start_game()
    player_choice = input('Twój wybór: ')
    if str(player_choice) == 't':
        room_one_menu()
    elif str(player_choice) == 'n':
        print('Trudno. Spróbujemy zagrać następnym razem.')
        print('Poczekaj na wyłączenie się gry.')
        time.sleep(2)
        quit()
    else:
        print('Zła wartość. Spróbuj jeszcze raz. ')
        main()


if __name__ == '__main__':
    main()
