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

    # What menu to open
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

            # Any of the options to continue to play
            elif (
                difficulties_choice == "easy"
                or difficulties_choice == "medium"
                or difficulties_choice == "hard"
                or difficulties_choice == "extreme"
            ):

                # Difficulty data saved
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

                # Entire dictionary will be stored
                words = []

                # Reads individually every line and puts in LIST "words"
                for i in range(221599):
                    content = myfile.readline()
                    words.append(content)
                myfile.close

                # Word preperation
                whole_word = random.choice(words)
                characters = list(whole_word.strip())
                hidden_characters = list("_" * len(characters))
                lifes = difficulties[difficulties_choice]["life's"]

                # TODO: For the future make the hanging man print
                # * Main game loop
                game = True
                while game:

                    # Cheat to develop the program
                    print(whole_word)

                    # Life and characters left with input
                    print(" " + " ".join(hidden_characters) + "\n")
                    print("You have {} life's left".format(lifes))
                    character_guess = input("Guess on character: ")

                    # TODO: Make This better
                    # * First test of character guess
                    correct_guesses = 0
                    wrong_guesses = 0
                    for i in characters:
                        if character_guess == i:
                            correct_guesses += 1
                        else:
                            wrong_guesses += 1

                    # If you get it right
                    if correct_guesses > 0:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("You found {} characters!".format(correct_guesses))

                        for y in range(correct_guesses):
                            position = characters.index(character_guess)
                            hidden_characters[position] = character_guess
                            characters[position] = " "

                        # If you win
                        if "".join(hidden_characters) == whole_word:
                            print("Congrats you won!!!")

                        time.sleep(1.5)
                        os.system("cls" if os.name == "nt" else "clear")

                    # When nothing right and removes 1 life
                    else:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\n You found no characters, you loose one life.")
                        lifes -= 1

                        # Check if you have lost
                        if lifes <= 0:
                            print(" You have lost!")
                            # TODO: Make a menu to play again or exit
                            # TODO: Print the whole word as a tease
                            input("Press Enter to Exit... ")
                            break

                        time.sleep(3)
                        os.system("cls" if os.name == "nt" else "clear")

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

        # prints rule menu, choose menu, clear menu
        while True:
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

    # ? Maybe change or make it public, can find anywhere
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

            else:
                print("Wrong option, try again.")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")

    else:
        print("\n   Error, choose a real option!")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")