import os
from Modules.ReadFile import RuleRead
from Modules import WrongOption


def rules():

    rulemenu, gameplay, difficultiesrule = RuleRead.ruleread()

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
            WrongOption.wrong()