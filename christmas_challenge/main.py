
import random

challenge_list = ['Ubierz choinkę', 'Przygotuj barszcz', 'Zaproś mamę na święta', 'Zorganizuj opłatek',
                  'Sprzątnij w domu']
challenges_done = []


class Menu:
    def main_menu(self):
        print('**********************')
        print('Christmas Challenges ')
        print('MENU')
        print('1.   Available challenges')
        print('2.   Show done list')
        print('3.   Add challenge')
        print('4.   Draw challenge')
        print('5.   Exit game')

class Challenge:
    def __init__(self):
        pass

    def draw_challenge(self):
        item = random.choice(challenge_list)
        print('Your challenge ist: ' + item + '\n')
        print('Do you want to remove a challenge from challenges list')
        print('1.   Yes')
        print('2.   No')
        user_choice = input()
        if int(user_choice) == 1:
                    challenges_done.append(item)
                    challenge_list.remove(item)
        else:
            pass

    def add_challenge(self):
        user_input = input("Your new challenge proposal: ")
        challenge_list.append(str(user_input))
        print(challenge_list)
        main()

    def print_challenge_list(self):
        print('\n Challenges list: \n')
        for item in challenge_list:
            print(item)

    def print_done_list(self):
        print('\n Done list: \n')
        if len(challenges_done) == 0:
            print(" No done challenges")
        else:
            for items in challenges_done:
                print (items)

def main():
    menu = Menu()
    challenge = Challenge()
    menu.main_menu()
    user_input = input("Your choice is: " )
    if (int(user_input) >=1) and (int(user_input) <=4):
        match str(user_input):
            case '1':
                challenge.print_challenge_list()
                print('\n')
                main()
            case '2':
                challenge.print_done_list()
                print('\n')
                main()
            case '3':
                challenge.add_challenge()
                main()
            case '4':
                challenge.draw_challenge()
                main()
            case '5':
                print("\nPress any key to exit.\n")
                input()

if __name__ == '__main__':
            main()