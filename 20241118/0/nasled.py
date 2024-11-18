class A:
  v = 1

class B(A):
  v = 2

b = B()
b.v = int(input("Введите значение для b.v: "))

print(f"b.v before any deletion: {b.v}")

del b.v
print(f"b.v after deleting b.v: {b.v}")

del B.v
print(f"b.v after deleting B.v: {b.v}")

