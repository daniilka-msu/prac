import re

class InvalidInput(Exception):
    pass

class BadTriangle(Exception):
    pass

def correct_input(inp):
    pattern = r"\(\s*(.+?)\s*,\s*(.+?)\s*\),\s*\(\s*(.+?)\s*,\s*(.+?)\s*\),\s*\(\s*(.+?)\s*,\s*(.+?)\s*\)"
    match = re.fullmatch(pattern, inp)
    if not match:
        raise InvalidInput()
    return list(match.groups())

def is_triangle(x1, y1, x2, y2, x3, y3):
    if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
        raise BadTriangle()
    return True

def to_nums(arr):
    try:
        return [float(el) for el in arr]
    except ValueError:
        raise BadTriangle()

def triangleSquare(s):
    coords = correct_input(s)
    x1, y1, x2, y2, x3, y3 = to_nums(coords)
    if is_triangle(x1, y1, x2, y2, x3, y3):
        area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
        print(f"{area:.1f}")
        exit()

while True:
    try:
        string = input()
        triangleSquare(string)
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
