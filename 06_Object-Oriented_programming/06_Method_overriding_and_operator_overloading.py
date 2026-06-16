class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def print_point(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def __add__(self,p):
        return Point(self.x + p.x, self.y + p.y)

p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1.sum(p2)  # Output: <__main__.Point object at 0x...> (a new Point object with x=6, y=8)
p3.print_point()  # Output: Point coordinates: (6, 8)
p4 = p1 + p2  # Output: <__main__.Point object at 0x...> (a new Point object with x=6, y=8)
p4.print_point()  # Output: Point coordinates: (6, 8)