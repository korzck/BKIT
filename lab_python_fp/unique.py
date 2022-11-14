class Unique(object):
    def __init__(self, items, **kwargs):
        self.r = []
    
        for key,value in kwargs.items():
            if key=='ignore_case' and value==True:
                try:
                    items = [i.lower() for i in items]
                finally:
                    break

        for i in items:
            if i not in self.r:
                self.r.append(i)


    def __next__(self):
        try:
            x = self.r[self.begin]
            self.begin += 1
            return x
        except:
            raise StopIteration

    def __iter__(self):
        self.begin = 0
        return self
        
if __name__ == '__main__':
    a = [1,4,87,3,5,7,2,4,6,4,3,6,3,4,2]
    b = ['A', 'a', 'B', 'b']
    for i in Unique(b, ignore_case=True):
        print(i)