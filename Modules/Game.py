import os, time, random, sys
from Modules.ReadFile import GameRead
from Modules import RandomWord, WrongOption, Endscreen


def gameplay():
    os.system("cls" if os.name == "nt" else "clear")
    difficulties_menu, difficultiesrule = GameRead.gameread()

    difficulties_loop = True
    while difficulties_loop:
        # Input and help
        print(difficulties_menu)
        print("For info type help")
        difficulties_choice = input("Choose: ").lower()
        os.system("cls" if os.name == "nt" else "clear")

        if difficulties_choice == "help":
            print(difficultiesrule)
            input("Press Enter to go back... ")
            os.system("cls" if os.name == "nt" else "clear")

        # Any of the options to continue to play
        elif (
            difficulties_choice == "easy"
            or difficulties_choice == "medium"
            or difficulties_choice == "hard"
            or difficulties_choice == "extreme"
        ):

            # Difficulty data saved
            difficulties = {
                "easy": {"life's": 10, "animation": "first"},
                "medium": {"life's": 8, "animation": "second"},
                "hard": {"life's": 6, "animation": "third"},
                "extreme": {"life's": 4, "animation": "fourth"},
            }

            # * Makes the random word from module
            whole_word, characters = RandomWord.randomword()

            # Word preperation
            hidden_characters = list("_" * len(characters))
            lifes = difficulties[difficulties_choice]["life's"]

            # Character preperation
            wrong_characters = []

            # TODO: For the future make the hanging man print
            # * Main game loop
            game = True
            while game:

                # Cheat to develop the program
                # print(whole_word)

                # Life and characters left with input
                print(" " + " ".join(hidden_characters) + "\n")
                print(" " + ", ".join(wrong_characters))
                print("\nYou have {} life's left".format(lifes))
                character_guess = input("Guess on character: ")

                # TODO: Make This better
                # * First test of character guess
                correct_guesses = 0
                for i in characters:
                    if character_guess.lower() == i:
                        correct_guesses += 1

                # If you get it right
                if correct_guesses > 0:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("\n You found {} characters!\n".format(correct_guesses))

                    for y in range(correct_guesses):
                        position = characters.index(character_guess.lower())
                        hidden_characters[position] = character_guess.lower()
                        characters[position] = " "

                    # See if there are any "_" left
                    dash_count = 0
                    for i in hidden_characters:
                        if i == "_":
                            dash_count += 1

                    # If none "_" you win
                    if dash_count == 0:
                        os.system("cls" if os.name == "nt" else "clear")

                        game = False
                        Endscreen.endscreen("\n     Congrats you won!!!")

                # When you found no character
                else:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("\n You found no characters, you loose one life.\n")
                    lifes -= 1

                    # Saves wrong character
                    wrong_characters.append(character_guess.lower())

                    # Check if you have lost
                    if lifes <= 0:
                        os.system("cls" if os.name == "nt" else "clear")
                        print(" You have lost!")
                        print(" The correct word was: {}".format(whole_word))
                        time.sleep(2)
                        os.system("cls" if os.name == "nt" else "clear")

                        game = False
                        Endscreen.endscreen("\n     You lost, nice try!")

        else:
            WrongOption.wrong()