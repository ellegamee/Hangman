def main_menu():
    # Reads the main menu graphics
    main_doc = open(
        r"Graphics\Main_menu.txt",
        "rt",
        encoding="utf8",
    )

    # Prints and closes main menu txt document
    main_menu = main_doc.read()
    main_doc.close()
    print(main_menu)

    difficultiesrule_doc = open(
        r"Graphics\Difficultiesrule.txt",
        "rt",
        encoding="utf8",
    )
    difficultiesrule = difficultiesrule_doc.read()
    difficultiesrule_doc.close()