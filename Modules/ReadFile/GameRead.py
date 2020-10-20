def gameread():
    difficulties_doc = open(
        r"Graphics\Difficulties.txt",
        "rt",
        encoding="utf8",
    )
    difficulties_menu = difficulties_doc.read()
    difficulties_doc.close()

    # * Read difficulties rules
    difficultiesrule_doc = open(
        r"Graphics\Difficultiesrule.txt",
        "rt",
        encoding="utf8",
    )
    difficultiesrule = difficultiesrule_doc.read()
    difficultiesrule_doc.close()