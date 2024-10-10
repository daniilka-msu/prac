from math import *

def Calc(s, t, u):
 def func(x):
  s_x = eval(s.replace("x", str(x)))
  t_x = eval(t.replace("x", str(x)))
  return eval(u.replace("x", str(s_x)).replace("y", str(t_x)))
 return func

formulas = input().split(",")
s = formulas[0].strip('"')
t = formulas[1].strip('"')
u = formulas[2].strip('"')
x = float(input())

F = Calc(s, t, u)
print(F(x))

