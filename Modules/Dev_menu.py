import time, os
from Modules import WrongOption


def dev(cheat_word):
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
        devmenu_choice = input("Command: ").lower()

        # Check what to do
        if devmenu_choice == "back":
            os.system("cls" if os.name == "nt" else "clear")
            return cheat_word
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")

        elif devmenu_choice == "cheat":
            cheat_word = True
            print("You can now see the hidden word!")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")

        # TODO When at the right moment fix win and so on
        elif devmenu_choice == "win":
            print("This does not work at the moment right now.")

        else:
            WrongOption.wrong()
