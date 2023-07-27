def multiple_returns(sentence):
  """Returns a tuple with the length of a string and its first character.
  Args:
    sentence: The string to be processed.
  Returns:
    A tuple with the length of the string and its first character.
  """
  # Check if the sentence is empty.
  if not sentence:
    return (0, None)
  # Get the length of the sentence.
  length = len(sentence)
  # Get the first character of the sentence.
  first_character = sentence[0]
  # Return the tuple with the length and first character.
  return (length, first_character)