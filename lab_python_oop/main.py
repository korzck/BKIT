from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square
import cowsay

if __name__ == "__main__":

    a = Rectangle(6, 6, 'blue', 'pryamougolnik')
    b = Circle(6, 'green', 'krug')
    c = Square(6, 'red', 'kvadrat')

    cowsay.trex(str(a)+'\n'+str(b)+'\n'+str(c))
