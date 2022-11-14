from .Shape import Shape

class Rectangle(Shape):
    def __init__(self, width=0, height=0, color=None, name=''):
        super().__init__(name=name)
        self.width = width
        self.height = height
        self.color.value = color
        
    def area(self):
        return self.width*self.height

    def get_name(self):
        return self.name