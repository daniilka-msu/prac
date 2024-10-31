from itertools import product

n = int(input())
print(",".join(sorted(filter(lambda x: x.count("TOR") == 2, map("".join, product("TOR", repeat=n))))))
