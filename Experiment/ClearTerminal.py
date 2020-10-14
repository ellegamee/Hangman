import os
import time

print("This text will print and will be deleted")
time.sleep(2)

os.system('cls' if os.name == 'nt' else 'clear')

print("Hello!")
# Only Hello will be in the terminal
