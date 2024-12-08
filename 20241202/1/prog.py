import sys

data = sys.stdin.buffer.read()
if data:
    N = data[0]
    tail = data[1:]
    L = len(tail)
    parts = [tail[round(i * L / N):round((i + 1) * L / N)] for i in range(N)]
    sorted_parts = sorted(parts)
    result = bytes([N]) + b''.join(sorted_parts)
    sys.stdout.buffer.write(result)
