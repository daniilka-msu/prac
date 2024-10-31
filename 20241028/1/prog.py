def fib(m, n):
    if n <= 0:
        return
    if m < 0:
        raise ValueError("Индекс m должен быть неотрицательным")
    x, y = 1, 1
    for _ in range(m):
        x, y = y, x + y
    for _ in range(n):
        yield x
        x, y = y, x + y

import sys
exec(sys.stdin.read())
