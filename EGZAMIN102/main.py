# --- egzamin_102 by Jacek --- #

import time
from room import *
from item import *
from character import *
from story import *
story = Story()
first_ch = First_chamber('First Chamber', 1)
second_ch = Second_chamber('Second Chamber', 2)
last_ch = Last_chamber('Last Chamber', 3)
character = Character('Joe', 'player')


def room_one_menu():
    story.room_one()
    room_one_user_input = input('No i? ')
    match str(room_one_user_input):
        case '1':
            first_ch.show_items()
            '''
                1. Dostępne przedmioty.
                2. Zabierz przedmiot.
                3. Użyj przedmiot.
                4. Następna komnata.
                5. Powrót
                '''
        case '2':
            pass
        case '3':
            pass
        case '4':
            room_two_menu()
        case '5':
            pass


def room_two_menu():
    print('haj')
    room_three_menu()


def room_three_menu():
    input_r3 = input('Dawaj: ')


def main():
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
