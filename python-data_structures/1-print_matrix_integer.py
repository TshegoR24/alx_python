def print_matrix_integer(matrix=[[]]):
  """Prints a matrix of integers.
  Args:
    matrix: A list of lists of integers.
  """
  # Iterate over the rows of the matrix.
  for row in matrix:
    # Iterate over the columns of the row.
    for column in row:
      # Print the column.
      print(str(column), end=" ")
    # Print a newline.
    print()
