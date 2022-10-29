from operator import itemgetter
 
class House:
    """Дом"""
    def __init__(self, id, number, price, name, street_id):
        self.id = id
        self.number = number
        self.price = price
        self.name = name
        self.street_id = street_id
 
class Street:
    """Улица"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class HouseStreet:
    def __init__(self, street_id, house_id):
        self.street_id = street_id
        self.house_id = house_id
 
streets = [
    Street(1, 'Бауманская'),
    Street(2, 'Ладожская'),
    Street(3, 'Бригадирный переулок'),
    Street(4, 'Лефортовский переулок'),
    Street(5, 'Рубцовская набережная'),
]

houses = [
    House(1, 1, 2500000000, 'ГЗ', 1), 
    House(2, 5, 4355000000, 'УЛК', 2), 
    House(3, 10, 450000000, 'ГБОУ Карбышева', 3), 
    House(4, 12, 150000000, 'Дом', 4), 
    House(5, 4, 492000000, 'Дом', 5), 
    House(6, 1, 120000000, 'Магазин', 5),
    House(7, 3, 240000000, 'Поликлиника МГТУ', 1)
]
 
houses_streets = [
    HouseStreet(1,1),
    HouseStreet(2,2),
    HouseStreet(3,3),
    HouseStreet(4,4),
    HouseStreet(5,5),
    HouseStreet(5,6),
    HouseStreet(1,7)
]
 
def main():
 
    one_to_many = [(h.name, s.name, h.number, h.price) 
        for s in streets 
        for h in houses 
        if h.street_id==s.id]
    
    many_to_many_temp = [(s.name, hs.street_id, hs.house_id) 
        for s in streets 
        for hs in houses_streets 
        if s.id == hs.street_id]
    
    many_to_many = [(h.id, street_id) 
        for name, street_id, house_id in many_to_many_temp
        for h in houses if h.id==house_id]
 
    print('Задание А1')
    res_31 = sorted(one_to_many, key=itemgetter(1))
    print(list(res_31))
    
    print('Задание А2')
    res32 = []
    for i in streets:
        
        s_houses = [ _ for _ in filter(lambda a: a[1]==i.name ,one_to_many )]
        res32.append((i.name, sum([ _[3] for _ in s_houses])))
    print(res32)
    
    print('Задание Е3')
    res33 = []
    for i in filter(lambda a: "переулок" in streets[a[1]-1].name, many_to_many):
        res33.append((streets[i[1]-1].name, [ _.name for _ in filter(lambda a: a.street_id==i[1], houses)]))
    print(res33)

if __name__ == '__main__':
    main()
