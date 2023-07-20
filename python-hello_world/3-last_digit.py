import random

# generate randon number
number =  random.randint(-10000, 10000)
print("orginal number:", number)

# find last number
end = str(number) [-1]
print(end)

# compare end number
end_as_number = int(end)
if end_as_number > 5:
    print("greater than 5")
elif end_as_number < 5 and end_as_number != 0:
    print("smaller than 5")
else:
    print("0")
