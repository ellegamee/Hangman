def dictread():

    dict_easy = []
    dict_hard = []

    Dictionary1 = open(
        r"Dictionaries\Easy_Swedish.txt",
        "rt",
        encoding="utf8",
    )

    for _ in range(136211):
        content = Dictionary1.readline()
        dict_easy.append(content)
    Dictionary1.close

    # * Read difficulties rules
    Dictionary2 = open(
        r"Dictionaries\Hard_Swedish.txt",
        "rt",
        encoding="utf8",
    )

    for _ in range(221599):
        content = Dictionary2.readline()
        dict_hard.append(content)
    Dictionary2.close

    return (dict_easy, dict_hard)