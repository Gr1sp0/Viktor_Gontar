def first_non_repeating_letter(string: str):
    string_uppercased = string.upper()
    for letter in string:
        if(string_uppercased.count(letter.upper()) <= 1):
            return letter
    return None