numbers = [int(x) for x in input().split()]
sorted_numbers = sorted(numbers, key=lambda x: x**2 % 100)
print(*sorted_numbers)

