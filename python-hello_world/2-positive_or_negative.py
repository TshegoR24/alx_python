# Do not touch this code
from random import randint

number = randint(-10, 10)
# End of code you shouldn't touch

# Your code here
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
