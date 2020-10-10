myfile = open(
    r"C:\Users\User\Documents\Coding\Python\School\Kapitel6\Hangman\Wordsrandom.txt",
    "rt",
    encoding="utf8",
)

for i in range(10000):
    content = myfile.readline()
    print(content)

myfile.close
