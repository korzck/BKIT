def print_result(f):
    def wrapper(a):
        print(f.__name__)
        res = f(a)
        if type(res) == list:
            for i in res: 
                print(i)
        elif type(res) == dict:
            for k,v in res.items():
                print(k, '=', v)
        return res
    return wrapper 

@print_result
def test123(a):
    return a

test123({'a':1, 'b':2, 'c':3})
newName = test123
newName([5,7,2,9,1,4,3])