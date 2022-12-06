import sys
sys.path.append("../lab_python_oop")
from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square

import unittest

class MyTesting(unittest.TestCase):
    def setUp(self):
        self.a = Rectangle(6, 6, 'blue', 'pryamougolnik')
        self.b = Circle(6, 'green', 'krug')
        self.c = Square(3, 'red', 'kvadrat')
    
    def test_area(self):
        import math
        self.assertEqual(self.a.area(), 36)
        self.assertEqual(self.b.area(), math.pi*6**2)
        self.assertEqual(self.c.area(), 9)
    
    def test_color(self):
        self.assertEqual(self.a.color.value, 'blue')
        self.assertEqual(self.b.color.value, 'green')
        self.assertEqual(self.c.color.value, 'red')
    
    def test_get_name(self):
        self.assertEqual(self.a.get_name(), 'pryamougolnik')
        self.assertEqual(self.b.get_name(), 'krug')
        self.assertEqual(self.c.get_name(), 'kvadrat')
        

if __name__ == '__main__':
    unittest.main()
