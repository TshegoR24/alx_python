def best_score(a_dictionary):
  """
  Returns a key with the biggest integer value.
  Args:
    a_dictionary: A dictionary.
  Returns:
    A key with the biggest integer value.
  """
  # Check if the input dictionary is valid.
  if not isinstance(a_dictionary, dict):
    raise ValueError("a_dictionary must be a dictionary.")
  # Find the key with the biggest integer value.
  best_key = None
  best_value = -1
  for key, value in a_dictionary.items():
    if isinstance(value, int):
      if value > best_value:
        best_key = key
        best_value = value
  # Return the key with the biggest integer value.
  return best_key