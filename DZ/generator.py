import sys
sys.path.append('../lab_python_fp')
from cm_timer import cm_timer_1

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
    
