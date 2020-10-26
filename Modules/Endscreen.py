import os, sys
from Modules import WrongOption


def endscreen(whole_word, lost, guess_whole_word):
    while True:
        # * Read difficulties rules
        endscreen_doc = open(
            r"Graphics\End_screen.txt",
            "rt",
            encoding="utf8",
        )
        endscreen = endscreen_doc.read()
        endscreen_doc.close()

        os.system("cls" if os.name == "nt" else "clear")
        if lost == True:
            if guess_whole_word == True:
                print("\n You tried to guess the whole word!")
                print(" You got it wrong!")

            print("\n   Correct word: {}".format(whole_word))
            print("   You lost, nice try!")

        elif lost == False:
            if guess_whole_word == True:
                print("\n You tried to guess the whole word!")
                print(" You got it right!")

            print("\n     Congrats you won!!!")

        print(endscreen)
        decide = input("Choose: ").lower()
        if decide == "retry":
            os.system("cls" if os.name == "nt" else "clear")
            break

        elif decide == "exit":
            sys.exit()

        else:
            os.system("cls" if os.name == "nt" else "clear")
            WrongOption.wrong()