def update_dictionary(a_dictionary, key, value):
  """
  Replaces or adds key/value in a dictionary.
  Args:
    a_dictionary: A dictionary.
    key: A string.
    value: Any type.
  Returns:
    A new dictionary with the updated key/value pair.
  """
  # Check if the input dictionary is valid.
  if not isinstance(a_dictionary, dict):
    raise ValueError("a_dictionary must be a dictionary.")
  # Check if the input key is a string.
  if not isinstance(key, str):
    raise ValueError("key must be a string.")
  # Create a new dictionary with the updated key/value pair.
  new_dictionary = a_dictionary.copy()
  new_dictionary[key] = value
  # Return the new dictionary.
  return new_dictionary