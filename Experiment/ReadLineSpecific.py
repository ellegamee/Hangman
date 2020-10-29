myfile = open(
    r".\Animation\animation_extreme.txt",
    "rt",
    encoding="utf8",
)

for _ in range(4):
    input("nasta gubbe\n")
    start = 1
    stop = 11

    for i in range(start, stop):
        content = myfile.readline()
        start += 10
        stop += 10
        print(content.strip())

myfile.close