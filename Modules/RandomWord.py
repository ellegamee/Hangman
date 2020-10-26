import random
from Modules.ReadFile import DictionaryRead


def randomword(lexicon):

    dict_easy, dict_hard = DictionaryRead.dictread()

    if lexicon == "easy" or lexicon == "medium":
        whole_word = random.choice(dict_easy)
        characters = list(whole_word.strip())

    elif lexicon == "hard" or lexicon == "extreme":
        whole_word = random.choice(dict_hard)
        characters = list(whole_word.strip())

    return (whole_word, characters)