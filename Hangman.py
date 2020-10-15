import random, time, os, sys

menu_loop = True
while menu_loop:

    # Reads the main menu graphics
    main_menu = open(
        r"Graphics\Main_menu.txt",
        "rt",
        encoding="utf8",
    )

    # Prints and closes main menu txt document
    # ! Better variable name
    mmc = main_menu.read()
    main_menu.close()
    print(mmc)

    # TODO: Make the menu input all lower case: play = Play
    # TODO: Overall improve the menu structure, loop maybe?
    menu_choise = input("Choose: ").lower()
    if menu_choise == "play":

        # Stop loop and clear terminal
        menu_loop = False
        os.system("cls" if os.name == "nt" else "clear")

        # TODO Continue to choose difficultie
        print("Continue with choosing difficultie.")

    elif menu_choise == "rules":

        # clear terminal
        os.system("cls" if os.name == "nt" else "clear")

        gameplay = open(
            r"Documentation\Gameplay.txt",
            "rt",
            encoding="utf8",
        )

        # ! Better variable name
        gpc = gameplay.read()
        gameplay.close()

        rules_menu = open(
            r"Graphics\Rules_menu.txt",
            "rt",
            encoding="utf8",
        )

        # Prints and closes rules txt document
        # ! Better variable name
        rmc = rules_menu.read()
        rules_menu.close()

        while True:
            print(rmc)
            rulemenu_choise = input("Choose: ").lower()
            os.system("cls" if os.name == "nt" else "clear")

            if rulemenu_choise == "gameplay":
                print(gpc)
                input("Press Enter to go back... ")
                os.system("cls" if os.name == "nt" else "clear")
            elif rulemenu_choise == "difficulties":
                print("Here will the difficulties print")
                input("Press Enter to go back... ")
                os.system("cls" if os.name == "nt" else "clear")
            elif rulemenu_choise == "back":
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print("Error, choose an real option!")

    elif menu_choise == "exit":

        # clear terminal
        os.system("cls" if os.name == "nt" else "clear")

        # Goodbye greeting to coustomer
        print("Good bye, have a great day.")
        sys.exit()

    elif menu_choise == "dev":
        # Stop loop and clear terminal
        os.system("cls" if os.name == "nt" else "clear")

        # Reads the main menu graphics
        dev_menu = open(
            r"Graphics\Dev_menu.txt",
            "rt",
            encoding="utf8",
        )

        # Prints and closes dev txt document
        # ! Better variable name
        dvc = dev_menu.read()
        dev_menu.close()

        while True:

            # Decide option
            devmenu_choise = input("\nCommand: ").lower()
            print(dvc)

            # Check what to do
            if devmenu_choise == "back":
                os.system("cls" if os.name == "nt" else "clear")
                break

            # TODO When at the right moment fix win and so on
            elif devmenu_choise == "win":
                print("This does not work at the moment right now.")
            elif devmenu_choise == "lose":
                print("This does not work at the moment right now.")
            else:
                print("Wrong option, try again.")

    else:
        print("Error, choose an real option!")
        time.sleep(1.5)
        os.system("cls" if os.name == "nt" else "clear")