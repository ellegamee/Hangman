import os, time
from Modules.ReadFile import RuleRead


def rules():

    RuleRead.ruleread()

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