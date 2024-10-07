def recursive_function(n):
 if n == 0:
  print("Базовый случай!")
 else:
  print(f"Рекурсивный вызов: n = {n}")
  recursive_function(n - 1)

recursive_function(5)

