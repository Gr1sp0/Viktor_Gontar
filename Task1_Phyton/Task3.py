def digital_root(value: int):
    value_str = str(value)
    sum_of_digits = sum([int(digit) for digit in value_str])
    if(sum_of_digits > 9):
        sum_of_digits = digital_root(sum_of_digits)
    return sum_of_digits