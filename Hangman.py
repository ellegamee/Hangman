import random, time, os, sys

# Funtion that is called when splitting word
def split(word):
    return [char for char in word]


loopbool = True
while loopbool:

    # Where all words from dictionary is stored
    words = []

    # ! THIS JUST WORKS ON LAPTOP
    # ! DON'T TRY ON STATIONARY
    # TODO Improve this part so it will automatically guide to the right path
    # ? When fixed in the experimentt or main do the same at the other

    # Open file where all the words are
    Extreme = open(
        r"C:\Users\User\Documents\GitHub\Hangman\Dictionaries\Wordsrandom.txt",
        encoding="utf8",
    )

    # Reads idividually every line and puts in LST "words"
    for i in range(221599):
        content = Extreme.readline()
        words.append(content)
    Extreme.close

    # Chose a random word and remove "/n" in the end
    whole_word = random.choice(words)
    master_word = whole_word[:-1]

    # Splits final word into characters
    characters = split(master_word)

    # TODO Print out the main menu
    # TODO Make the output print (CODE) prettier
    print(
        "This is the main menu, select by typing wich option you want.\n\n"
        "===============================\n"
        "|                             |\n"
        "|   Play    Rules    Exit     |\n"
        "|                             |\n"
        "===============================\n"
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

        # ! Bug in VS code where it does not work, works in cmd
        # ? Trying to find solution
        sys.exit()

    elif menu_choise == "dev":
        # Stop loop and clear terminal
        os.system("cls" if os.name == "nt" else "clear")

        print("Welcome to the dev menu.")
        print("Type: word to see the secret word")
        print("Type: back to come to the main menu again")

        while True:
            devmenu_choise = input("\nCommand: ")
            if devmenu_choise == "word":
                print(master_word)
            elif devmenu_choise == "back":
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print("There are no more options at the moment")

    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("error, choose an real option")
