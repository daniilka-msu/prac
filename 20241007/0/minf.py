def MINF(*args):
 def g(x):
  min_value = float('inf')
  for f in args:
   min_value = min(min_value, f(x))
  return min_value
 return g

def f1(x):
 return x**2

def f2(x):
 return x + 1

def f3(x):
 return -x

g = MINF(f1, f2, f3)
print(g(2))

