def make_linear_function(a, b):
 def linear_function(x):
  return a * x + b
 return linear_function

f1 = make_linear_function(2, 1)
f2 = make_linear_function(-1, 3)

print(f1(3))
print(f2(5))
