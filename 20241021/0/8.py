expression = input("")
a, b = map(int, input("").split(","))

# Вычисление с x=a и y=b
result1 = eval(expression, {"x": a, "y": b})
print(result1)

# Вычисление с x=b и y=a
result2 = eval(expression, {"x": b, "y": a})
print(result2)

