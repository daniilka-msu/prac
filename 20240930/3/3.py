def read_matrix(n):
  matrix = []
  for _ in range(n):
    row = list(map(int, input().split(',')))
    if len(row) != n:
      raise ValueError("Не квадратные")
    matrix.append(row)
  return matrix

def multiply_matrices(m1, m2):
  n = len(m1)
  res = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        res[i][j] += m1[i][k] * m2[k][j]
  return res

try:
  m1 = read_matrix(3)

  m2 = read_matrix(3)

  result = multiply_matrices(m1, m2)
  print()
  for row in result:
    print(*row, sep=',')

except ValueError as e:
  print(e)

