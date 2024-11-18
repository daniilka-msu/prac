class A:
  def __str__(self):
    return "A"

class B(A):
  def __str__(self):
    return f"{super().__str__()}:{self.__class__.__name__}"

class C(B):
  def __str__(self):
    return f"{super().__str__()}:{self.__class__.__name__}"

print(A())  # Выведет: A
print(B())  # Выведет: A:B
print(C())  # Выведет: A:B:C

