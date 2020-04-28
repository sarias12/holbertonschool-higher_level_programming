#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lint = number % -10
else:
    lint = number % 10
if lint > 5:
    print("Last digit of", number, "is", lint, "and is greater than 5")
elif lint == 0:
    print("Last digit of", number, "is", lint, "and is 0")
else:
    print("Last digit of", number, "is", lint, "and is less than 6 and not 0")
