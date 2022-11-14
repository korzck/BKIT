import math
from .Shape import Shape


class Circle(Shape):
    def __init__(self, radius=0, color=None, name=''):
        super().__init__(name=name)
        self.color.value = color
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2

    def get_name(self):
        return self.name
    