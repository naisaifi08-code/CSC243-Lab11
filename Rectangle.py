from Point import Point
class Retangle:
    def __init__(self, p, q):
        assert type(p) == Point and type(q) == Point and p.x <= q.x and p.y <= q.y, "Bad input!"
        self.p = p
        self.q = q
    def __str__(self):
        return "(p =" + str(self.p) + ", q =" + str(self.q) + ")" 
    def width(self):
        return self.q.x - self.p.x
    def height(self):
        return self.q.y - self.p.y
    def perimeter(self):
        return 2 * (self).width() + self.height()
    def area(self):
        return self.width() * self.height()
    def contains(self, pt):
        assert type(pt) == Point, "Bad input!"
        return (self.p.x <= pt.x <= self.q.x and self.p.y <= pt.y <= self.q.y)

