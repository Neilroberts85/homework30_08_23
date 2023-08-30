import unittest
from src.drink import Drink 

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Espresso", 3, 5)

    def test_name_same(self):
        self.assertEqual("Espresso", self.drink.name) 

    def test_name_price(self):
        self.assertEqual(3, self.drink.price) 