def common_elements(set_1, set_2):
  """
  Returns a set of common elements in two sets.
  Args:
    set_1: A set of elements.
    set_2: A set of elements.
  Returns:
    A set of elements that are in both sets.
  """
  # Check if the input sets are valid.
  if not isinstance(set_1, set):
    raise ValueError("set_1 must be a set.")
  if not isinstance(set_2, set):
    raise ValueError("set_2 must be a set.")
  # Find the intersection of the two sets.
  common_elements = set_1.intersection(set_2)
  # Return the set of common elements.
  return common_elements