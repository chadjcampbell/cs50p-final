import os
import time
import sys

from playsound import playsound
from simple_term_menu import TerminalMenu
from colorist import blue

from global_thermonuclear_war import global_thermonuclear_war
from guess_the_number import guess_the_number
from rock_paper_scissors import rock_paper_scissors
from tic_tac_toe import tic_tac_toe


def main():
    os.system('clear')
    while True:
        single_print('LOGON: ', 0.1)
        username = input()
        if username.lower().strip() == 'joshua':
            os.system('clear')
            break
        else:
            access_denied()
    fake_norad()
    single_print('GREETINGS PROFESSOR FALKEN.', 0.1)
    time.sleep(3)
    print('\n'*2)
    pick_game()
    game_over()


def single_print(string, speed, output_stream=sys.stdout):
    printed_content = ""
    for char in string:
        output_stream.write(char + '\a')
        output_stream.flush()
        printed_content += char
        time.sleep(speed)

    return printed_content


def fake_norad():
    single_print(
        'jmnsZJrExk6f8xSaRCbuQl9vcT85K5YQs2rCYIRN0194KtIO1hXEMqcWtPwpSbPq', 0.02)
    os.system('clear')
    single_print('wSRq1wztrXkoslH03h7Y139KVib4VRMHRmoEywKbi23JqOUmR5cXRz5n28HoAvdIIGtWxbs4BaBy4cWwWKUxCjtdKACxg11lZlP8iYe4QxKIgl18fzUz6jiVlNJLDvIgZCA2EG8rUqcWdpi82', 0.01)
    os.system('clear')
    single_print(
        '▒▒▒▒9vcT85▒▒▒  ▒03h7Y1▒▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒▒KtIO1h▒▒▒ 867-5309 ▒▒▒▒▒ ▒▒▒▒▒▒aBy4c▒▒▒▒ ▒▒▒▒▒▒▒▒', 0.02)
    os.system('clear')


def access_denied():
    print('\n'*5)
    print('           ** IDENTIFICATION NOT RECOGNIZED **')
    print('                   ** ACCESS DENIED **')
    time.sleep(2)
    os.system('clear')


def pick_game():
    playsound('Shall-we-play-a-game.mp3', block=False)
    single_print('SHALL WE PLAY A GAME?', 0.1)
    print('\n'*2)
    print('  Move with Up/Down, Enter to Select\n')
    options = ["Guess the Number", "Tic-Tac-Toe",
               "Rock, Paper, Scissors", "Global Thermonuclear War", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    game = options[menu_entry_index]
    if game == 'Exit':
        os.system('clear')
        sys.exit()
    while game != "Global Thermonuclear War":
        if game == 'Guess the Number':
            os.system('clear')
            guess_the_number()
            time.sleep(3)
            os.system('clear')
            pick_game()
            return
        elif game == 'Tic-Tac-Toe':
            os.system('clear')
            tic_tac_toe()
            time.sleep(3)
            os.system('clear')
            pick_game()
            return
        elif game == 'Rock, Paper, Scissors':
            os.system('clear')
            rock_paper_scissors()
            os.system('clear')
            pick_game()
            return
        else:
            os.system('clear')
            blue('**  NORAD SYSTEM ERROR  **')
            sys.exit()
    global_thermonuclear_war()


def game_over():
    os.system('clear')
    single_print('A STRANGE GAME.', 0.1)
    print('')
    single_print('THE ONLY WINNING MOVE', 0.1)
    print('')
    single_print('IS NOT TO PLAY.', 0.1)
    print('\n')
    time.sleep(2)
    single_print('HOW ABOUT A NICE GAME OF CHESS?', 0.1)
    time.sleep(2)
    os.system('clear')


if __name__ == "__main__":
    main()
