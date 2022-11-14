from .Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, width=0, color=None, name=''):
        super().__init__(name=name)
        self.width = width
        self.color.value = color
     
    def area(self):
        return self.width*self.width

    def get_name(self):
        return self.name