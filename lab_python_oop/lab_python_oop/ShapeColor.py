class ShapeColor():
    def __init__(self):
        self.value = None

    @property
    def color(self):
        return self.value

    @color.setter
    def color(self, value):
        self.value = value
    
    @color.deleter
    def color(self):
        del self.value

    def color(self):
        return self.value
