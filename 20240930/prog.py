M, N = map(int, input().split(', '))
print([i for i in range(M, N) if all(i % j for j in range(2, int(i**0.5) + 1))])


