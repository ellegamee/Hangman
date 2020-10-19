import random, time, os, sys

menu_loop = True
while menu_loop:

    # Reads the main menu graphics
    main_doc = open(
        r"Graphics\Main_menu.txt",
        "rt",
        encoding="utf8",
    )
    main_menu = main_doc.read()
    main_doc.close()
    print(main_menu)

    # Reads and closes the difficulties rules
    difficultiesrule_doc = open(
        r"Graphics\Difficultiesrule.txt",
        "rt",
        encoding="utf8",
    )
    difficultiesrule = difficultiesrule_doc.read()
    difficultiesrule_doc.close()

    menu_choice = input("Choose: ").lower()
    os.system("cls" if os.name == "nt" else "clear")

    if menu_choice == "play":
        menu_loop = False

        difficulties_doc = open(
            r"Graphics\Difficulties.txt",
            "rt",
            encoding="utf8",
        )

        # Prints and closes difficulties menu and txt document
        difficulties_menu = difficulties_doc.read()
        difficulties_doc.close()
        os.system("cls" if os.name == "nt" else "clear")

        while True:
            # Input and help
            print(difficulties_menu)
            print("For info type help")
            difficulties_choice = input("Choose: ").lower()
            os.system("cls" if os.name == "nt" else "clear")

            if difficulties_choice == "help":
                print(difficultiesrule)
                input("Press Enter to go back... ")
                os.system("cls" if os.name == "nt" else "clear")

            elif difficulties_choice == "easy" or "medium" or "hard" or "extreme":

                difficulties = {
                    "easy": {"life's": 10, "animation": "first"},
                    "medium": {"life's": 8, "animation": "second"},
                    "hard": {"life's": 6, "animation": "third"},
                    "extreme": {"life's": 4, "animation": "fourth"},
                }

                # * This is a test of how many lives
                # difficulties[difficulties_choice]["life's"]

                # gets the master word from the computer

            else:
                print("\n   Error, choose a real option!")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")

    elif menu_choice == "rules":

        # ! Major text wrong needs to get a look at
        gameplay_doc = open(
            r"Documentation\Gameplay.txt",
            "rt",
            encoding="utf8",
        )
        gameplay = gameplay_doc.read()
        gameplay_doc.close()

        rulemenu_doc = open(
            r"Graphics\Rules_menu.txt",
            "rt",
            encoding="utf8",
        )
        rulemenu = rulemenu_doc.read()
        rulemenu_doc.close()

        while True:
            # prints rule menu, choose menu, clear menu
            print(rulemenu)
            rulemenu_choice = input("Choose: ").lower()
            os.system("cls" if os.name == "nt" else "clear")

            if rulemenu_choice == "gameplay":
                print(gameplay)
                input("Press Enter to go back... ")
                os.system("cls" if os.name == "nt" else "clear")

            elif rulemenu_choice == "difficulties":
                print(difficultiesrule)
                input("Press Enter to go back... ")
                os.system("cls" if os.name == "nt" else "clear")

            elif rulemenu_choice == "back":
                os.system("cls" if os.name == "nt" else "clear")
                break

            else:
                print("\n   Error, choose a real option!")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")

    elif menu_choice == "exit":

        # Goodbye greeting to customer
        print("Good bye, have a great day.")
        sys.exit()

    elif menu_choice == "dev":

        # Reads the dev menu graphics
        devmenu_doc = open(
            r"Graphics\Dev_menu.txt",
            "rt",
            encoding="utf8",
        )

        # Prints and closes dev txt document
        devmenu = devmenu_doc.read()
        devmenu_doc.close()

        while True:

            # Decide option
            devmenu_choice = input("\nCommand: ").lower()
            print(devmenu)

            # Check what to do
            if devmenu_choice == "back":
                os.system("cls" if os.name == "nt" else "clear")
                break

            # TODO When at the right moment fix win and so on
            elif devmenu_choice == "win":
                print("This does not work at the moment right now.")

            elif devmenu_choice == "lose":
                print("This does not work at the moment right now.")

            else:
                print("Wrong option, try again.")

    else:
        print("\n   Error, choose a real option!")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")