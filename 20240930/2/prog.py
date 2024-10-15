def sortik(numbers):
  n = len(numbers)
  for i in range(n):
    for j in range(0, n - i - 1):
      key_j = (numbers[j] * 2) % 100
      key_jplus1 = (numbers[j + 1] * 2) % 100
      if key_j > key_jplus1:
        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
  return numbers

numbers = list(map(int, input().split(',')))
sorted_numbers = sortik(numbers)
print(sorted_numbers)

