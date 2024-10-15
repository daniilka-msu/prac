M, N = map(int, input().split(', '))
primes = [i for i in range(M, N) if i > 0 and all(i % j for j in range(2, int(i**0.5) + 1))]
print(primes)



