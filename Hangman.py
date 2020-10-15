import random, time, os, sys

loopbool = True
while loopbool:

    # TODO Print out the main menu
    # TODO Make the output print (CODE) prettier
    print(
        "This is the main menu, select by typing wich option you want.\n\n"
        "===============================\n"
        "|                             |\n"
        "|   Play    Rules    Exit     |\n"
        "|                             |\n"
        "===============================\n",
    )

    # TODO: Make the menu input all lower case: play = Play
    # TODO: Overall improve the menu structure, loop maybe?
    menu_choise = input()
    if menu_choise == "play":

        # Stop loop and clear terminal
        loopbool = False
        os.system("cls" if os.name == "nt" else "clear")

        # TODO Continue to choose difficultie
        print("Continue with choosing difficultie.")

    elif menu_choise == "rules":

        # Stop loop and clear terminal
        loopbool = False
        os.system("cls" if os.name == "nt" else "clear")

        # TODO: Print out the rules
        print("This will print the rules.")

    elif menu_choise == "exit":

        # Stop loop and clear terminal
        loopbool = False
        os.system("cls" if os.name == "nt" else "clear")

        # Goodbye greeting to coustomer
        print("Good bye, have a great day.")
        sys.exit()

    elif menu_choise == "dev":
        # Stop loop and clear terminal
        os.system("cls" if os.name == "nt" else "clear")

        print("Welcome to the dev menu.")
        print("Type: back to come to the main menu again")

        while True:
            devmenu_choise = input("\nCommand: ")
            if devmenu_choise == "back":
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print("There are no more options at the moment")

    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("error, choose an real option")