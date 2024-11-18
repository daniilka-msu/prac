class A:
  v = 1

class B(A):
  v = 2

b = B()
try:
  b.v = int(input())
except ValueError:
  b.v = 0

print(f"b.v before any deletion: {b.v}")

del b.v
print(f"b.v after deleting b.v: {getattr(b, 'v', type(b).v)}")

del B.v
print(f"b.v after deleting B.v: {getattr(b, 'v', type(b).v)}")

