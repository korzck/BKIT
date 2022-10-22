import json
from operator import concat
from unique import Unique
from field import field
from gen_random import gen_random

def f1(a):
    return Unique([i['job-name'] for i in field(data, 'job-name')], ignore_case=True)
def f2(a):
    return filter(lambda a: a.startswith('программист'), a)
def f3(a):
    return list(map(lambda x: concat(x, ' c опытом Python'), a))
def f4(a):
    return zip(a, gen_random(len(a),137287, 200000))

with open('data_light.json') as f:
    data = json.loads(f.read())
    for i in f4(f3(f2(f1(data)))):
        print(i)
