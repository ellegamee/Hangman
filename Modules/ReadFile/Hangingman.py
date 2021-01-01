def animation_lines(difficulties, difficulties_choice):
    file_name = difficulties[difficulties_choice]["animation"]
    animation = open(
        r"Animation\{}".format(file_name),
        "rt",
        encoding="utf8",
    )
    hangingman = animation.readlines()
    animation.close

    return hangingman