from itertools import product

rows = 'ABCDEFGH'
columns = range(1, 9)
cells = [''.join(cell) for cell in product(rows, map(str, columns))]

print(cells)

