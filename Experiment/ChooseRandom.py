import random

words = []

# Open file where all the words are
# ! THIS JUST WORKS ON LAPTOP
# ! DON'T TRY ON STATIONARY
# TODO Improve this part so it will automatically guide to the right path
# ? When fixed in the experimentt or main do the same at the other

myfile = open(
    r"C:\Users\User\Documents\Coding\Python\School\Kapitel6\Hangman\Wordsrandom.txt",
    "rt",
    encoding="utf8",
)

# Reads idividually every line and puts in LST "words"
for i in range(221599):
    content = myfile.readline()
    words.append(content)
myfile.close

# Chose a random word and remove "/n" in the end
whole_word = random.choice(words)
master_word = whole_word[:-1]

print(master_word)
