import random


def randomword():
    # Open file where all the words are
    myfile = open(
        r".\Dictionaries\Wordsrandom.txt",
        "rt",
        encoding="utf8",
    )

    # Entire dictionary will be stored
    words = []

    # Reads individually every line and puts in LIST "words"
    for i in range(221599):
        content = myfile.readline()
        words.append(content)
    myfile.close

    whole_word = random.choice(words)
    characters = list(whole_word.strip())

    return (whole_word, characters)