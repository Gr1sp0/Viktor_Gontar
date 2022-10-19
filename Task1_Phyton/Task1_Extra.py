def next_bigger(value: int):
    if(value > 9):
        list_of_digits = [digit for digit in str(value)]
        list_of_digits[-1], list_of_digits[-2] = list_of_digits[-2], list_of_digits[-1]
        new_value = int(''.join(list_of_digits))
        if(new_value > value):
            return new_value
    return -1