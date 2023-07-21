def fibonacci_sequence(n):
  if n < 0:
    return []
  elif n == 0:
    return [0]
  elif n == 1:
    return [0, 1]
  else:
    fibonacci = [0, 1]
    for i in range(2, n):
      fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
    return fibonacci