class Rectangle:
    rectcnt = 0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        Rectangle.rectcnt += 1
        setattr(self, f"rect_{Rectangle.rectcnt}", Rectangle.rectcnt)

    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1}), rectcnt: {Rectangle.rectcnt}"

    def area(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)

    def lt(self, other):
        return self.area() < other.area()

    def eq(self, other):
        return self.area() == other.area()

    def mul(self, k):
        return Rectangle(self.x1 * k, self.y1 * k, self.x2 * k, self.y2 * k)

    def rmul(self, k):
        return Rectangle(self.x1 * k, self.y1 * k, self.x2 * k, self.y2 * k)

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
k = int(input())

myrect = Rectangle(x1, y1, x2, y2)
print(myrect)

newrect = myrect.mul(k)
print(newrect)

newrect2 = k * myrect
print(newrect2)


