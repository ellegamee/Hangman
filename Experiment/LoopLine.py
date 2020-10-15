myfile = open(
    r".\Dictionaries\Wordsrandom.txt",
    "rt",
    encoding="utf8",
)

for i in range(10000):
    content = myfile.readline()
    print(content)

myfile.close
