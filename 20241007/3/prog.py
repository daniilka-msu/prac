from math import *

def c(a, b, d):
  f = lambda x: eval(a)
  g = lambda x: eval(b)
  h = lambda x, y: eval(d)

  def r(x):
    return h(f(x), g(x))

  return r

e = input().replace('"', '').split(',')
v = eval(input())
r = c(*e)
print(r(v))

