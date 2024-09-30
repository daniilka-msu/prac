n = list(map(int, input("").split(", ")))
for number in n:
    if number %2 != 0:
       print("nechet", number)
       break
else:
    print("net nechet", n[0])
