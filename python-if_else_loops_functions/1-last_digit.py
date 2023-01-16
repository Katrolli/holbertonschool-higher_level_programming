#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    nr = (number * -1 % 10) * -1
    if nr > 5:
        print(f"Last digit of {number} is {nr} and is greater than 5")
    elif nr == 0:
        print(f"Last digit of {number} is {nr} and is 0")
    elif nr < 6 and nr != 0:
        print(f"Last digit of {number} is {nr} and is less than 6 and not 0")
else:
    nr = number % 10
    if nr > 5:
        print(f"Last digit of {number} is {nr} and is greater than 5")
    elif nr == 0:
        print(f"Last digit of {number} is {nr} and is 0")
    elif nr < 6 and nr != 0:
        print(f"Last digit of {number} is {nr} and is less than 6 and not 0")
