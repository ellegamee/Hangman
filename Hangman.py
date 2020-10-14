import random, time, os

# Funtion that is called when splitting word
def split(word):
    return [char for char in word]


# Where all words from dictionary is stored
words = []

# ! THIS JUST WORKS ON LAPTOP
# ! DON'T TRY ON STATIONARY
# TODO Improve this part so it will automatically guide to the right path
# ? When fixed in the experimentt or main do the same at the other

# Open file where all the words are
Extreme = open(
    r"C:\Users\User\Documents\GitHub\Hangman\Wordsrandom.txt",
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
# print(characters)

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
    print("You will play now.")

elif menu_choise == "rules":
    print("This will print the rules.")

elif menu_choise == "exit":
    print("Good bye, have a great day.")

elif menu_choise == "dev":
    print("Welcome to the dev menu.")
    print("Type: word to see the secret word")

    devmenu_choise = input()
    if devmenu_choise == "word":
        print(master_word)
    else:
        print("There are no more options at the moment")

else:
    print("error, choose an option")