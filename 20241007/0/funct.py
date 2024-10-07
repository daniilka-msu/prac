def S(f, g):

 def h(x):
  return f(x) + g(x)
 return h

def f(x):
 return x**2

def g(x):
 return x + 1

h = S(f, g)
print(h(2))

