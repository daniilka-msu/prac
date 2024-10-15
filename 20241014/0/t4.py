from math import *

W = 60
H = 20
A, B = -4, 4
for i in range(H):
    x = A + (B - A) * i / 19
    y = sin(x)
    spc = round((1 + y) / 2 * 40)
    print(spc * " ", "*")
