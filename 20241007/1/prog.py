def Pareto(*pairs):

  pareto_front = []
  for i, pair1 in enumerate(pairs):
    is_dominated = False
    for j, pair2 in enumerate(pairs):
      if i != j and pair1[0] <= pair2[0] and pair1[1] <= pair2[1] and (pair1[0] < pair2[0] or pair1[1] < pair2[1]):
        is_dominated = True
        break
    if not is_dominated:
      pareto_front.append(pair1)

  return tuple(pareto_front)

print(Pareto((32, 38), (10, 14), (19, 44), (31, 31), (17, 33), (53, 6), (48, 9), (6, 38), (30, 49), (52, 30), (7, 30), (45, 45), (21, 51), (7, 49), (11, 23)))


print(Pareto((1, 2), (3, 4), (2, 2), (4, 3), (7, 0), (1, 8)))

