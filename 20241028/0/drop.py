from itertools import dropwhile, islice

sequence = [1.5, 1.2, 1.7, 1.8, 1.9, 1.6, 2.0, 2.1, 2.2, 2.3, 1.4, 1.5, 2.4, 2.5, 2.6]
filtered_iter = dropwhile(lambda x: x <= 1.6, sequence)
result = list(islice(filtered_iter, 10))

print(result)

