def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return (0)
    final = 0
    num = 0
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for rev in reversed(roman_string):
        num = digits[rev]
        final += num if final < num * 5 else -num
    return final
