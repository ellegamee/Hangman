import os, time, random, sys
from Modules.ReadFile import GameRead
from Modules import RandomWord, WrongOption, Endscreen, Dev_menu


def gameplay(cheat_word):
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
                "easy": {"life's": 10, "lexicon": "easy"},
                "medium": {"life's": 8, "lexicon": "hard"},
                "hard": {"life's": 6, "lexicon": "hard"},
                "extreme": {"life's": 4, "lexicon": "hard"},
            }

            # * Makes the random word from module
            lexicon = difficulties[difficulties_choice]["lexicon"]
            whole_word, characters = RandomWord.randomword(lexicon)

            # Word preperation
            hidden_characters = list("_" * len(characters))
            lifes = difficulties[difficulties_choice]["life's"]

            # Character preperation
            wrong_characters = []
            all_characters = []

            # TODO: For the future make the hanging man print
            # * Main game loop
            game = True
            while game:

                # Cheat to develop the program
                if cheat_word == True:
                    print("\n " + whole_word.strip())

                # Life and characters left with input
                print("\n " + " ".join(hidden_characters) + "\n")
                print(" Wrong: " + ", ".join(wrong_characters))
                print("\nYou have {} life's left".format(lifes))
                character_guess = input("Guess on character: ")

                if character_guess == "dev":
                    os.system("cls" if os.name == "nt" else "clear")
                    cheat_word = Dev_menu.dev(cheat_word)

                # Cheacks in you type more than one character
                if len(character_guess) >= 2 or len(character_guess.strip()) == 0:
                    if character_guess == "dev":
                        continue
                    else:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\n You can just guess one character!")
                        continue

                # If you already have used a character and save it
                if character_guess in all_characters:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("\n You have already guessed: {}".format(character_guess))
                    continue

                all_characters.append(character_guess.lower())

                # * First test of character guess
                correct_guesses = 0
                for i in characters:
                    if character_guess.lower() == i:
                        correct_guesses += 1

                # If you get it right
                if correct_guesses > 0:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("\n You found {} characters!".format(correct_guesses))

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
                    print("\n You found no characters, you loose one life.")
                    lifes -= 1

                    # Saves wrong character
                    wrong_characters.append(character_guess.lower())

                    # Check if you have lost
                    if lifes <= 0:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\n   Correct word: {}".format(whole_word))

                        game = False
                        Endscreen.endscreen("     You lost, nice try!")

        elif difficulties_choice == "back":
            os.system("cls" if os.name == "nt" else "clear")
            break

        else:
            WrongOption.wrong()