import unittest
from generator import fib
import time

class fib_test(unittest.TestCase):

    def test_fib_1(self):
        a = [i for i in fib(5)]
        expected = [0, 1, 1, 2, 3]
        self.assertEqual(a, expected)

    def test_fib_2(self):
        a = [i for i in fib(10)]
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(a, expected)

    def test_fib_3(self):
        a = [i for i in fib(0)]
        expected = []
        self.assertEqual(a, expected)
    
    def test_fib_4(self):
        start_time = time.time()
        a = fib(200000) 
        end_time = time.time() - start_time
        self.assertLess(end_time, 1) # if spent time less than a second
        
    def test_fib_5(self):
        start_time = time.time()
        a = [i for i in fib(200000)] 
        end_time = time.time() - start_time
        self.assertLess(1, end_time) 

if __name__ == '__main__':
    unittest.main()