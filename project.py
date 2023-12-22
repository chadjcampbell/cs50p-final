import os
import time
import sys

from playsound import playsound
from global_thermonuclear_war import global_thermonuclear_war
from guess_the_number import guess_the_number
from rock_paper_scissors import rock_paper_scissors
from simple_term_menu import TerminalMenu
from tic_tac_toe import tic_tac_toe


def main():
    os.system('clear')
    """ while True:
            single_print('LOGON: ', 0.1)
            username = input()
            if username.lower().strip() == 'joshua':
                os.system('clear')
                break
            else:
                access_denied()
        fake_norad()
        single_print('GREETINGS PROFESSOR FALKEN.',0.1)
        time.sleep(3)
        print('\n'*2)
        playsound('Shall-we-play-a-game.mp3', block=False)
        single_print('SHALL WE PLAY A GAME?',0.1) """
    print('')
    game = pick_game()
    if game == 'Guess the Number':
        guess_the_number()
    elif game == 'Tic-Tac-Toe':
        tic_tac_toe()
    elif game == 'Rock, Paper, Scissors':
        rock_paper_scissors()
    else:
        global_thermonuclear_war()



def single_print(string, speed):
    for char in string:
        sys.stdout.write(char + '\a')
        sys.stdout.flush()
        time.sleep(speed)


def fake_norad():
    single_print('jmnsZJrExk6f8xSaRCbuQl9vcT85K5YQs2rCYIRN0194KtIO1hXEMqcWtPwpSbPq',0.02)
    os.system('clear')
    single_print('wSRq1wztrXkoslH03h7Y139KVib4VRMHRmoEywKbi23JqOUmR5cXRz5n28HoAvdIIGtWxbs4BaBy4cWwWKUxCjtdKACxg11lZlP8iYe4QxKIgl18fzUz6jiVlNJLDvIgZCA2EG8rUqcWdpi82',0.01)
    os.system('clear')
    single_print('▒▒▒▒9vcT85▒▒▒  ▒03h7Y1▒▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒▒KtIO1h▒▒▒ 867-5309 ▒▒▒▒▒ ▒▒▒▒▒▒aBy4c▒▒▒▒ ▒▒▒▒▒▒▒▒',0.02)
    os.system('clear')

def access_denied():
    print('\n'*5)
    print('           ** IDENTIFICATION NOT RECOGNIZED **')
    print('                   ** ACCESS DENIED **')
    time.sleep(2)
    os.system('clear')

def pick_game():
    options = ["Guess the Number", "Tic-Tac-Toe", "Rock, Paper, Scissors", "Global Thermonuclear War"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    return options[menu_entry_index]
    
    


if __name__ == "__main__":
    main()