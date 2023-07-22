import random
# This line should not change:
number = random.randint(-10000, 10000)
# Print the last digit of the number stored in the variable `number`.
print("Last digit of", number, "is", number % 10, end="")
# Check if the last digit is greater than 5.
if number % 10 > 5:
    print(" and is greater than 5")
# Check if the last digit is equal to 0.
elif number % 10 == 0:
    print(" and is 0")
# Check if the last digit is less than 6 and not equal to 0.
else:
    print(" and is less than 6 and not 0")

