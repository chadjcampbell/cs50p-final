import os

from simple_term_menu import TerminalMenu
from war_maps import starter_map, select_usa, select_russia
import random


def global_thermonuclear_war():
    # main game
    os.system('clear')
    print(starter_map)
    country = select_country()
    if country == 'USA':
        os.system('clear')
        print(select_usa)
    if country == 'Russia':
        os.system('clear')
        print(select_russia)
    while len(usa_cities) and len(russia_cities):
        target = select_target(country)
        if target in usa_cities:
            print(f"{target} HAS BEEN DESTOYED")
            usa_cities.remove(target)
            retaliate = random.choice(russia_cities)
            russia_cities.remove(retaliate)
            print(f"RUSSIA HAS DETROYED {retaliate}")
        else:
            print(f"{target} HAS BEEN DESTOYED")
            russia_cities.remove(target)
            retaliate = random.choice(usa_cities)
            russia_cities.remove(retaliate)
            print(f"USA HAS DETROYED {retaliate}")


# helper functions
def select_country():
    print('SELECT YOUR COUNTRY')
    print('  Move with Up/Down, Enter to Select\n')
    options = ["USA", "Russia"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    return options[menu_entry_index]


usa_cities = ["New York", "Washington DC", "Los Angeles"]
russia_cities = ["Moscow", "Leningrad", "Kyev"]


def select_target(country):
    print('SELECT YOUR TARGET')
    print('  Move with Up/Down, Enter to Select\n')
    if country == 'USA':
        options = russia_cities
    if country == 'Russia':
        options = usa_cities
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    return options[menu_entry_index]
