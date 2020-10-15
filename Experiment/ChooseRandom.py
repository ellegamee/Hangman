import random

words = []

# Open file where all the words are
myfile = open(
    r".\Dictionaries\Wordsrandom.txt",
    "rt",
    encoding="utf8",
)

# Reads idividually every line and puts in LST "words"
for i in range(221599):
    content = myfile.readline()
    words.append(content)
myfile.close

whole_word = random.choice(words)
master_word = whole_word.strip()

print(master_word)