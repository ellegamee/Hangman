import random, time, os, sys
from Modules import Game, RulesMenu, WrongOption, Main_Menu, Dev_menu

menu_loop = True
while menu_loop:

    Main_Menu.main_menu()
    # ! This does not solve it
    cheat_word = False

    # What menu to open
    menu_choice = input("Choose: ").lower()
    os.system("cls" if os.name == "nt" else "clear")

    if menu_choice == "play":
        # ! Does not help the problem
        cheat_word = Game.gameplay()

    elif menu_choice == "rules":
        RulesMenu.rules()

    elif menu_choice == "dev":
        Dev_menu.dev()

    elif menu_choice == "exit":
        # Goodbye greeting to customer
        print("Good bye, have a great day.")
        sys.exit()

    else:
        WrongOption.wrong()