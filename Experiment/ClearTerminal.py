import os
import time  # ? Makes the running of the code more understanable

# * Print and waits un-till deleating
print("This text will print and will be deleted")
time.sleep(2)

# * this is used to clear the terminal
os.system("cls" if os.name == "nt" else "clear")

print("Hello!")
# Only Hello will be in the terminal
