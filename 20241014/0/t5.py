from math import *


def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A

A, B = -5, 5
W, H = 60, 25

screen = [
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.'] ,     
          ]
screen = [['.']*W for i in range(H)]

for i in range(5):
    screen[i][i+10] = '@'

print("\n".join(["".join(s) for s in screen]))
