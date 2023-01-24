#!/usr/bin/python3
def roman_to_int(roman_string):
    d1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    d2 = {"IV": 4, "VII": 7, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    if roman_string is None or type(roman_string) != str:
        return 0
    sum = 0
    i = 0
    while i < len(roman_string):
        sub_str = roman_string[i: i + 2]
        if sub_str in d2:
            sum += d2[sub_str]
            i += 1
        elif roman_string[i] in d1:
            sum += d1[roman_string[i]]
        i += 1
    return sum
