import unittest
from RK1_for_RK2 import Street, House, HouseStreet, A1, A2, A3

class RK1_test(unittest.TestCase):
    
    def setUp(self):
        self.streets = [
            # id, name
            Street(1, 'Бауманская'),
            Street(2, 'Рубцовская набережная')
        ]
        self.houses = [
            # id, number, price, name, street_id
            House(1, 2, 25, 'ГЗ', 1), 
            House(2, 5, 43, 'УЛК', 2), 
            House(3, 12, 16, 'Дом', 2)
        ]
            # street_id, house_id
        self.houses_streets = [
            HouseStreet(1, 1),
            HouseStreet(2, 2),
            HouseStreet(2, 3)
        ]
        

    def test_A1(self):
        # expected list of tuples sorted ASC by street name
        expected_result = [
            ('ГЗ', 'Бауманская', 2, 25),
            ('Дом', 'Рубцовская набережная', 12, 16),
            ('УЛК', 'Рубцовская набережная', 5, 43)
        ]

        result = A1(self.streets, self.houses)
        self.assertEqual(result, expected_result)
    
    def test_A2(self):
        # expected tuple of streets sorted ASC by price
        expected_result = [
            ('Бауманская', 25), 
            ('Рубцовская набережная', 59)
        ]
        result = A2(self.streets, self.houses)
        self.assertEqual(result, expected_result)

    def test_A3(self):
        # expected lsit of tuples with street names and houses on it, sorted by name ASC
        expected_result = [
            ('Рубцовская набережная', ['Дом','УЛК'])
        ]
        result = A3(self.streets, self.houses, 'набережная')
        self.assertEqual(result, expected_result) 
    
if __name__ == '__main__':
    unittest.main()