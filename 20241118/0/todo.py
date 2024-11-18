class A:
  def __init__(self):
    self.a_v = 0

  def inc(self):
    self.a_v += 1

class B(A):
  def __init__(self):
    super().__init__()
    self.b_v = 100500

b = B()
print(f"b.a_v: {b.a_v}")
b.inc()
print(f"b.a_v after inc(): {b.a_v}")
print(f"b.b_v: {b.b_v}")

