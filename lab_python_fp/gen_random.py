from random import randint
def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield randint(begin, end)
    
if __name__ == '__main__':
    for i in gen_random(10, 100, 200):
        print(i)