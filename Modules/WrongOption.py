import time, os


def wrong():
    print("\n   Error, choose a real option!")
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")