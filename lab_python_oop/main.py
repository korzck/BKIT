from lab_python_oop import Circle
from lab_python_oop import Square
from lab_python_oop import Rectangle
import cowsay

if __name__ == "__main__":

    a = Rectangle.Rectangle(6, 6, 'blue', 'pryamougolnik')
    b = Circle.Circle(6, 'green', 'krug')
    c = Square.Square(6, 'red', 'kvadrat')

    cowsay.trex(str(a)+'\n'+str(b)+'\n'+str(c))
