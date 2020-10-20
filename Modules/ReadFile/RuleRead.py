def ruleread():
    # *
    rulemenu_doc = open(
        r"Graphics\Rules_menu.txt",
        "rt",
        encoding="utf8",
    )
    rulemenu = rulemenu_doc.read()
    rulemenu_doc.close()

    # ! Major text wrong needs to get a look at
    gameplay_doc = open(
        r"Documentation\Gameplay.txt",
        "rt",
        encoding="utf8",
    )
    gameplay = gameplay_doc.read()
    gameplay_doc.close()

    # * Read difficulties rules
    difficultiesrule_doc = open(
        r"Graphics\Difficultiesrule.txt",
        "rt",
        encoding="utf8",
    )
    difficultiesrule = difficultiesrule_doc.read()
    difficultiesrule_doc.close()