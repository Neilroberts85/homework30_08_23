import unittest
from src.coffee_shop import CoffeeShop 
from src.drink import Drink
from src.customer import Customer
class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.instance_of_our_drink_class = Drink("espresso", 3, 5)
        self.coffee_shop = CoffeeShop("Greggs", 200, [self.instance_of_our_drink_class])
        self.customer = Customer("Neil", 0, 38, 0)
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("Greggs", self.coffee_shop.name)

    def test_increase_till(self):
        self.coffee_shop.sell_drink(self.instance_of_our_drink_class, self.customer)
        self.assertEqual(203, self.coffee_shop.till)

    # def test_age(self):
    #     self.coffee_shop.sell_drink(self.instance_of_our_drink_class, )


