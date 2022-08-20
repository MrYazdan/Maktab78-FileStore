from os import name as os_name, system as terminal


def clear():
    terminal('cls' if os_name.lower() == 'nt' else 'clear')
