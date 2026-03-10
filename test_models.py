import pytest
from models import Point, Line, Circle, Square

class TestPoint:
    def test_create_point(self):
        new_point = Point(x=1, y=2)
        assert new_point.x == 1
        assert new_point.y == 2
    
    def test_str_point(self):
        new_point = Point(x=1, y=2)
        assert str(new_point) == "Точка (1, 2)"

class TestLine:
    def test_create_point(self):
        new_line = Line(x=1, y=2, x_end=3, y_end=5)
        assert new_line.x == 1
        assert new_line.y == 2
        assert new_line.x_end == 3
        assert new_line.y_end == 5
    
    def test_str_point(self):
        new_line = Line(x=1, y=2, x_end=3, y_end=5)
        assert str(new_line) == "Линия ((1, 2) (3, 5))"

class TestCircle:
    def test_create_point(self):
        new_circle = Circle(x=1, y=2, radius=3)
        assert new_circle.x == 1
        assert new_circle.y == 2
        assert new_circle.radius == 3
    
    def test_str_point(self):
        new_circle = Circle(x=1, y=2, radius=3)
        assert str(new_circle) == "Круг (1, 2, 3)"

class TestSquare:
    def test_create_point(self):
        new_square = Square(x=1, y=2, side=3)
        assert new_square.x == 1
        assert new_square.y == 2
        assert new_square.side == 3
    
    def test_str_point(self):
        new_square = Square(x=1, y=2, side=3)
        assert str(new_square) == "Квадрат (1, 2, 3)"