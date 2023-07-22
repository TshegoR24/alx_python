# This code prints out the numbers 01,02,03,04,05,06,07,08,09,12,13,14,15,16,17,18,19,23,24,25,26,27,28,29,34,35,36,37,38,39,45,46,47,48,49,56,57,58,59,67,68,69,78,79 and 89.
# First, we create a loop that goes from 1 to 9.
for i in range(1,9):
    # Inside the loop, we create another loop that goes from 2 to 9.
    for j in range(2,9):
        # We then print the number `i` followed by the number `j`.
        print('{}{}'.format(i,j))

