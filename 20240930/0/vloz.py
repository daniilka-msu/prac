mat = []
while True:
    row = input()
    if row == "":
        break
    mat.append(list(map(int, row.split())))
n = len(mat)

for i in range(n):
    for j in range(i + 1, n):
        mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
for row in mat:
    print(*row)