def formatting_string(string: str):
    return_string = str()
    set_of_pairs = string.split(";")
    for i in range(len(set_of_pairs)):
        pair_list = set_of_pairs[i].split(":")
        pair_list.reverse()
        pair_list = [pair.upper() for pair in pair_list]
        set_of_pairs[i] = pair_list
    set_of_pairs.sort()
    for surname, name in set_of_pairs:
        return_string += f"({surname}, {name})"
    return return_string