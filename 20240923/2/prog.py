s = 0
ln = 0

while True:
  n = int(input())
  ln = n

  if n <= 0:
    print(ln)
    break

  s += n

  if s > 21:
    print(s)
    break
