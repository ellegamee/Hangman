import os, sys
from Modules import WrongOption


def endscreen():
    # * Read difficulties rules
    endscreen_doc = open(
        r"Graphics\End_screen.txt",
        "rt",
        encoding="utf8",
    )
    endscreen = endscreen_doc.read()
    endscreen_doc.close()

    print(endscreen)
    decide = input("Choose: ").lower()
    if decide == "retry":
        os.system("cls" if os.name == "nt" else "clear")
        # ! Here is the problem
        break

    elif decide == "exit":
        sys.exit()

    else:
        os.system("cls" if os.name == "nt" else "clear")
        WrongOption.wrong()