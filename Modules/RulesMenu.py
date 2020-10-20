import os, time


def rules():
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