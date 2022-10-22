import time
from contextlib import contextmanager

class cm_timer_1():
    def __enter__(self):
        self.start_time = time.time()
    def __exit__(self, type, value, traceback):
        print(time.time() - self.start_time)

@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield 
    print(time.time()-start_time)

with cm_timer_1() as c:
    time.sleep(2.6)

with cm_timer_2() as c:
    time.sleep(2.6)    