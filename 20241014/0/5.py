from math import *


def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A


def show(screen):
    print('\n'.join(''.join(row) for row in screen))


A, B = -5, 5
W, H = 60, 25
screen = [['.'] * W for _ in range(H)]
for i in range(W):
    x = scale(0, W - 1, A, B, i)
    y = sin(x)
    spc = scale(-1, 1, 0, H - 1, y)
    screen[round(spc)][i] = '@'

show(screen)
