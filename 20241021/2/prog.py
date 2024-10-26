from math import *

f = {}
c = 1

while (i := input())[:5] != "quit ":
    if i.startswith(':'):
        d = i[1:].split()
        p = d[1:-1]
        f[d[0]] = (p, d[-1])
        c += 1
    else:
        c += 1
        a = i.split()
        n = a[0]
        r = a[1:]
        res = eval(f[n][1], globals(), {x: eval(y) for x, y in zip(f[n][0], r)})
        print(res)

print(i[6:-1].format(len(f) + 1, c))

