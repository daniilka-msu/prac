def average(*args):
 if len(args) == 0:
  return 0
 return sum(args) / len(args)

print(average(1, 2, 3))
print(average(10, 20))
print(average())
