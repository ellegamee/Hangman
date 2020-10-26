import random, time, os, sys
from Modules import Game, RulesMenu, WrongOption, Main_Menu, Dev_menu

os.system("cls" if os.name == "nt" else "clear")
cheat_word = False
menu_loop = True
while menu_loop:

    Main_Menu.main_menu()

    # What menu to open
    menu_choice = input("Choose: ").lower()
    os.system("cls" if os.name == "nt" else "clear")

    if menu_choice == "play":
        Game.gameplay(cheat_word)

    elif menu_choice == "rules":
        RulesMenu.rules()

    elif menu_choice == "dev":
        cheat_word = Dev_menu.dev(cheat_word)

    elif menu_choice == "exit":
        # Goodbye greeting to customer
        print("Good bye, have a great day.")
        sys.exit()

    else:
        WrongOption.wrong()