def square_matrix_simple(matrix=[]):
  """
  Computes the square value of all integers of a matrix.
  Args:
    matrix: A 2 dimensional array.
  Returns:
    A new matrix:
      Same size as matrix
      Each value should be the square of the value of the input
      Input matrix should not be modified
  Raises:
    ValueError: If the input matrix is not a 2 dimensional array.
  """
  # Check if the input matrix is a 2 dimensional array.
  if not isinstance(matrix, list):
    raise ValueError("Input matrix must be a 2 dimensional array.")
  # Check if the input matrix has the correct dimensions.
  for row in matrix:
    if not isinstance(row, list):
      raise ValueError("Input matrix must be a 2 dimensional array.")
    if len(row) != len(matrix[0]):
      raise ValueError("Input matrix must be a 2 dimensional array.")
  # Compute the square value of each integer in the matrix.
  new_matrix = []
  for row in matrix:
    new_row = []
    for value in row:
      new_row.append(value * value)
    new_matrix.append(new_row)
  # Return the new matrix.
  return new_matrix