class Customer:
    def __init__(self, input_name, input_wallet, input_age, input_energy):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.energy = input_energy

    def reduce_wallet(self, input_amount):
        self.wallet -= input_amount

    def buy_drink(self, input_drink):
        self.reduce_wallet(input_drink.price)

    