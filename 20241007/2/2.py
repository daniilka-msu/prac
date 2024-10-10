def subtract(minuend, subtrahend):
 if type(minuend) == type(subtrahend):
  if isinstance(minuend, (int, float)):
   return minuend - subtrahend
  elif isinstance(minuend, (list, tuple)):
   difference = []
   for element in minuend:
    if element not in subtrahend:
     difference.append(element)
   return difference
  else:
   return None
 else:
  return None

print(subtract(123, 45))
print(subtract((4, 2, 7, 4, 6, 87, 7), (2, 54, 67, 3, 2)))
print(subtract(["Q", "WE", "RTY"], ["WE", "ZZ"]))

