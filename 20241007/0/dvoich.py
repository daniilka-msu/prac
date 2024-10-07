def rbin(n, current_list, next_digit):

 if n == 0:
  print(current_list)
 else:
  rbin(n - 1, current_list + [next_digit], 0)
  rbin(n - 1, current_list + [next_digit], 1)

rbin(9, [1], 0)

