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

        difficulties_doc = open(
            r"Graphics\Difficulties.txt",
            "rt",
            encoding="utf8",
        )

        # Prints and closes difficulties menu and txt document
        difficulties_menu = difficulties_doc.read()
        difficulties_doc.close()
        os.system("cls" if os.name == "nt" else "clear")

        difficulties_loop = True
        while difficulties_loop:
            # Input and help
            print(difficulties_menu)
            print("For info type help")
            difficulties_choice = input("Choose: ").lower()
            os.system("cls" if os.name == "nt" else "clear")

            if difficulties_choice == "help":
                print(difficultiesrule)
                input("Press Enter to go back... ")
                os.system("cls" if os.name == "nt" else "clear")

            elif (
                difficulties_choice == "easy"
                or difficulties_choice == "medium"
                or difficulties_choice == "hard"
                or difficulties_choice == "extreme"
            ):

                difficulties_loop = False
                difficulties = {
                    "easy": {"life's": 10, "animation": "first"},
                    "medium": {"life's": 8, "animation": "second"},
                    "hard": {"life's": 6, "animation": "third"},
                    "extreme": {"life's": 4, "animation": "fourth"},
                }

                # Open file where all the words are
                myfile = open(
                    r".\Dictionaries\Wordsrandom.txt",
                    "rt",
                    encoding="utf8",
                )

                words = []

                # Reads individually every line and puts in LST "words"
                for i in range(221599):
                    content = myfile.readline()
                    words.append(content)
                myfile.close

                whole_word = random.choice(words)
                characters = list(whole_word.strip())
                print(" _" * len(characters))

                # while True:
                print(
                    "\n You have {} life's left".format(
                        difficulties[difficulties_choice]["life's"]
                    )
                )

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
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")