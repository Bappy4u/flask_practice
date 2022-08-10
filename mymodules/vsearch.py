def search4letters(phrase:str, letters:str) -> set:
    phrase = set(phrase)

    return phrase.intersection(set(letters))
