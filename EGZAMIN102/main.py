# --- egzamin_102 by Jacek --- #

import time
from room import *
from item import *
from character import *
from story import *
story = Story()
first_chamber = First_chamber('First Chamber', 1)
second_chamber = Second_chamber('Second Chamber', 2)
last_chamber = Last_chamber('Last Chamber', 3)
character = Character('Joe', 'player')


def room_one_menu():
    story.room_one()
    room_one_user_input = input('No i? ')
    match str(room_one_user_input):
        case '1':
            first_chamber.show_items()
            input("\nDowolny klawisz aby wrócić.")
            room_one_menu()
        case '2':
            pass
        case '3':
            pass
        case '4':
            room_two_menu()
        case '5':
            pass


def room_two_menu():
    story.room_two()
    room_two_user_input = input('No i co robimy dalej? ')
    match str(room_two_user_input):
        case '1':
            second_chamber.show_items()
            input("\nDowolny klawisz aby wrócić.")
            room_two_menu()
        case '2':
            pass
        case '3':
            pass
        case '4':
            room_three_menu()
        case '5':
            pass


def room_three_menu():
    story.room_three()
    room_three_user_input = input('No i? ')
    match str(room_three_user_input):
        case '1':
            last_chamber.show_items()
            input("\nDowolny klawisz aby wrócić.")
            room_three_menu()
        case '2':
            pass
        case '3':
            pass
        case '4':
            story.game_over()


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
