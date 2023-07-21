def fibonacci_sequence(n):
  if n < 0:
    return []
  if n == 0:
    return [0]
  if n == 1:
    return [0, 1]
  fibonacci_sequence = [0, 1]
  for i in range(2, n):
    fibonacci_sequence.append(fibonacci_sequence[i - 2] + fibonacci_sequence[i - 1])
  return fibonacci_sequence