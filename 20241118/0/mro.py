class A: pass
class B: pass
class C(A, B): pass
class D(B, A): pass

# Способ 1
try:
  class E1(C, D): pass
  e1 = E1()
except TypeError as e:
  print(f"Ошибка (Способ 1): {e}")
class E1_fixed(D, C): pass; e1_fixed = E1_fixed(); print("Способ 1 исправлен.")

# Способ 2
try:
  class E2(D, C): pass
  e2 = E2()
except TypeError as e:
  print(f"Ошибка (Способ 2): {e}")
class E2_fixed(C, D): pass; e2_fixed = E2_fixed(); print("Способ 2 исправлен.")

# Способ 3
try:
  class E3(A, C, D): pass
  e3 = E3()
except TypeError as e:
  print(f"Ошибка (Способ 3): {e}")
class E3_fixed(C, D, A): pass; e3_fixed = E3_fixed(); print("Способ 3 исправлен.")

