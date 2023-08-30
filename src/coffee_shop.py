class CoffeeShop:
    def __init__(self, input_name, input_till, input_drinks):
        self.name = input_name
        self.till = input_till
        self.drinks = input_drinks

    def increase_till(self, input_amount):
        self.till += input_amount
    
    def decrease_till(self, input_amount):
        self.till -= input_amount

    def check_age(self, input_customer):
        if input_customer.age >= 16:
             return True
        else:
             return False

    # def check_caffeine_levels(self, )

    def sell_drink(self, input_drink, input_customer):
        if self.check_age(input_customer) == True:
            input_customer.reduce_wallet(input_drink.price)
            self.increase_till(input_drink.price)


        
    


    
    
    
    
    # A `Coffee Shop` should be able to sell a drink to a customer 
    # and increase it's `till` by the price of `Drink`. 
    # Hint: Use a `Customer` method you already have.
