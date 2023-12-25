import os

from simple_term_menu import TerminalMenu
from war_maps import starter_map, select_usa


def global_thermonuclear_war():
    # main game
    os.system('clear')
    print(starter_map)
    country = select_country()
    if country == 'USA':
        os.system('clear')
        print(select_usa)


# helper functions
def select_country():
    print('SELECT YOUR COUNTRY')
    print('  Move with Up/Down, Enter to Select\n')
    options = ["USA", "Russia"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    return options[menu_entry_index]
