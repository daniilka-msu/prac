from itertools import islice

def slide(seq, n):
    for i in range(len(seq) - n + 1):
        yield from islice(seq, i, i + n)

    for i in range(1, n):
        yield from seq[-n + i:]

import sys
exec(sys.stdin.read())
