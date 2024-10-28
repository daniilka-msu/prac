from itertools import filterfalse

n = 3
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
non_divisible_by_n = list(filterfalse(lambda x: x % n == 0, sequence))

print(non_divisible_by_n)

