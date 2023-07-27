def multiply_list_map(my_list=[], number=0):
  """
  Returns a new list:
    Same length as my_list
    Each value should be multiplied by number
    Initial list should not be modified
    You are not allowed to import any module
    You have to use map
  """
  # Check if the input list is valid.
  if not isinstance(my_list, list):
    raise ValueError("my_list must be a list.")
  # Check if the input number is valid.
  if not isinstance(number, int):
    raise ValueError("number must be an integer.")
  # Create a new list with the same length as the input list.
  new_list = list(map(lambda x: x * number, my_list))
  # Return the new list.
  return new_list