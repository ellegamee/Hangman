import random, time, os, sys

menu_loop = True
while menu_loop:

    # Reads the main menu graphics
    main_doc = open(
        r"Graphics\Main_menu.txt",
        "rt",
        encoding="utf8",
    )

    # Prints and closes main menu txt document
    main_menu = main_doc.read()
    main_doc.close()
    print(main_menu)

    menu_choice = input("Choose: ").lower()
    os.system("cls" if os.name == "nt" else "clear")

    if menu_choice == "play":
        menu_loop = False

        # TODO Continue to choose difficulties
        print("Continue with choosing difficultly.")

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

        difficultiesrule_doc = open(
            r"Graphics\Difficultiesrule.txt",
            "rt",
            encoding="utf8",
        )
        difficultiesrule = difficultiesrule_doc.read()
        difficultiesrule_doc.close()

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

        # Reads the main menu graphics
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
            print(devmenu)
            devmenu_choice = input("\nCommand: ").lower()

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
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")

    else:
        print("\n   Error, choose a real option!")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")