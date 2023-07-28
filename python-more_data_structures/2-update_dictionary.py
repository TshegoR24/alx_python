def update_dictionary(a_dictionary, key, value):
  """
  Replaces or adds key/value in a dictionary.
  key argument will be always a string
  value argument will be any type
  If a key exists in the dictionary, the value will be replaced
  If a key doesn't exist in the dictionary, it will be created
  Args:
    a_dictionary: The dictionary to be updated.
    key: The key to be updated or added.
    value: The value to be associated with the key.
  Returns:
    The updated dictionary.
  """
  # Check if the key exists in the dictionary.
  if key in a_dictionary:
    # If the key exists, replace the value.
    a_dictionary[key] = value
  else:
    # If the key doesn't exist, add it with the given value.
    a_dictionary[key] = value
  # Return the updated dictionary.
  return a_dictionary


