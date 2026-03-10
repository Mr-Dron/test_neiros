class Shape:
    def __init__(self, x, y):
        self._count = 0
        self.x = x
        self.y = y


class Point(Shape):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
    
    def __str__(self):
        return f"Точка ({self.x}, {self.y})"

class Line(Shape):
    def __init__(self, x_end, y_end, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.x_end = x_end
        self.y_end = y_end
    
    def __str__(self):
        return f"Линия (({self.x}, {self.y}) ({self.x_end},{self.y_end}))"


class Circle(Shape):
    def __init__(self, radius, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.radius = radius
    
    def __str__(self):
        return f"Круг ({self.x}, {self.y}, {self.radius})"


class Square(Shape):
    def __init__(self, side, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.side = side

    def __str__(self):
        return f"Квадрат ({self.x}, {self.y}, {self.side})"
        