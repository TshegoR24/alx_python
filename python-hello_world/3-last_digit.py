#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

# Checking if the number is negative or positive
if number < 0:
    sign = "negative"
else:
    sign = "positive"

# Printing the result
print(f"The last digit of {number} is {abs(number) % 10}")

# Checking if the last digit is greater than 5
if abs(number) % 10 > 5:
    print(f"and is greater than 5")

# Checking if the last digit is 0
elif abs(number) % 10 == 0:
    print(f"and is 0")

# Checking if the last digit is less than 6 and not 0
else:
    print(f"and is less than 6 and not 0")

print()
