def search4letters(phrase:str, letters:str) -> set:
    phrase = set(phrase.lower())

    return phrase.intersection(set(letters.lower()))
