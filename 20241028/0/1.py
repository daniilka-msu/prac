def sum_of_squares():
    n = 1
    current_sum = 0
    while True:
        current_sum += 1 / (n ** 2)
        yield current_sum
        n += 1

generator = sum_of_squares()

for _ in range(10):
    print(next(generator))

