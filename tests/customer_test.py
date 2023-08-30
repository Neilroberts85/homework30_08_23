import unittest
from src.customer import Customer 
from src.drink import Drink
class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Neil", 100, 38, 0)
        self.drink = Drink("Espresso", 3, 5)

    def test_name_same(self):
        self.assertEqual("Neil", self.customer.name) 

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(3)
        self.assertEqual(97, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(97, self.customer.wallet)
