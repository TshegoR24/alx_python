def pow(a, b):
  if b == 0:
    return 1
  if b == 1:
    return a
  if b < 0:
    return 1 / pow(a, -b)
  return a * pow(a, b - 1)