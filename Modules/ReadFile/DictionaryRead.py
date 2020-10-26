def dictread():

    dict_easy = []
    dict_hard = []

    Dictionary1 = open(
        r"Dictionaries\Easy_Swedish.txt",
        "rt",
        encoding="utf8",
    )

    content = Dictionary1.readline()
    while content:
        dict_easy.append(content)
        content = Dictionary1.readline()
    Dictionary1.close

    # * Read difficulties rules
    Dictionary2 = open(
        r"Dictionaries\Hard_Swedish.txt",
        "rt",
        encoding="utf8",
    )

    content = Dictionary2.readline()
    while content:
        dict_hard.append(content)
        content = Dictionary2.readline()
    Dictionary2.close

    return (dict_easy, dict_hard)