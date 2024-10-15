from math import *

def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A

W = 40
H = 20
A, B = -4, 4
for i in range(H):
    x = scale(0, H - 1, A, B, i)
    y = sin(x)
    spc = round(scale(-1, 1, 0, W - 1, y))
    print(" " * spc, '*')
