class Rectangle:
  rectcnt = 0

  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    Rectangle.rectcnt += 1

  def __str__(self):
    return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1}), rectcnt: {Rectangle.rectcnt}"

n = int(input()) # Количество прямоугольников

for i in range(n):
  x1 = int(input())
  y1 = int(input())
  x2 = int(input())
  y2 = int(input())
  rect = Rectangle(x1, y1, x2, y2)
  print(rect) 

