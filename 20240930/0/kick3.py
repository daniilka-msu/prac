start = int(input(""))
end = int(input(""))

o = []
for n in range(start, end + 1):
    if n % 2 != 0 and '3' not in str(n):
      o.append(n)
print("", o)
