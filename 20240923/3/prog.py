N = int(input())

row = N
while row <= N + 2:
    col = N
    while col <= N + 2:
        result = row * col

        d = 0
        while result > 0:
            d += result % 10
            result //= 10

        if d == 6:
            print(":=)", end=" ")
        else:
            print(f"{row} * {col} = {row * col}", end=" ")
        col += 1
    print()
    row += 1

