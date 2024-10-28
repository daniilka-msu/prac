from itertools import repeat

def repeater(seq, n):
    for item in seq:
        yield from repeat(item, n)

sequence = [1, 2, 3]
n_times = 3
result = list(repeater(sequence, n_times))

print(result)

