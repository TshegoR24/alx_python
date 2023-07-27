def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:>4}".format(matrix[i][j]), end="")
        print()

