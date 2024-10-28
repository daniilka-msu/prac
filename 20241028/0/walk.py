def walk2d():
    x, y = 0, 0
    while True:
        dx, dy = yield (x, y)
        x += dx
        y += dy

generator = walk2d()
next(generator)

for _ in range(10):
    print(generator.send((1, 1)))

