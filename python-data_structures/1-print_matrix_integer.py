def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            # Using str.format() to print integers without converting them to strings
            print("{:d}".format(matrix[i][j]), end=" ")
        print()

# Example usage:
matrix_example = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix_example)

