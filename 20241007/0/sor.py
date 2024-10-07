numbers = [5, 2, 1, 4, 3]

sorted_numbers = sorted(numbers) 
print(sorted_numbers)

sorted_numbers = sorted(numbers, key=lambda x: x % 3)
print(sorted_numbers)

