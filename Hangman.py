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
    content = main_menu.read()
    main_menu.close()
    print(content)

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

        # TODO: Write the rules in the txt documnt
        print("This will print the rules.")
        input("Press Enter to continue...")
        os.system("cls" if os.name == "nt" else "clear")

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
        content = dev_menu.read()
        dev_menu.close()
        print(content)

        while True:

            # Decide option
            devmenu_choise = input("\nCommand: ").lower()

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