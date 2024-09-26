n = int(input())

output = "A - B - C -"

if n % 2 == 0 and n % 25 == 0:
  output = output.replace("A -", "A +")

if n % 2 != 0 and n % 25 == 0:
  output = output.replace("B -", "B +")

if n % 8 == 0:
  output = output.replace("C -", "C +")

print(output)
