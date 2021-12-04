class Beverages:  # superclass
    def __init__(self, item_name, budget, price, item_qty):  # self represents the object of the class
        self.item_name = item_name
        self.budget = budget
        self.price = price
        self.item_qty = item_qty

    def __str__(self):  #method to return the item name
        return f' {self.item_name} '

    def get_change(self, budget):  # function to return balance
        return budget - self.price * self.item_qty


class Coffee(Beverages):

    def __init__(self, item_name, budget, price, item_type, item_qty):
        super().__init__(item_name, budget, price, item_qty)
        self.item_type = item_type

    def __str__(self):  # method to return the type of the item
        return super().__str__() + f' of {self.item_type} size ' \
                                   f'\nCost: ${self.price} ' \
                                   f'\nQty: {self.item_qty}' \
                                   f'\nTotal: {self.get_total()}'

    def get_total(self):  # method to return the total cost of the item
        return self.price * self.item_qty


class Tea(Beverages):

    def __init__(self, item_name, budget, price, item_type, item_qty):
        super().__init__(item_name, budget, price, item_qty)
        self.item_type = item_type

    def get_total(self):  # method to return the total cost of the item
        return self.price * self.item_qty

    def __str__(self):   # method to return the type of the item
        return super().__str__() + f' of {self.item_type} size ' \
                                   f'\nCost: ${self.price} ' \
                                   f'\nQty: {self.item_qty}' \
                                   f'\nTotal: {self.get_total()}'


class Softdrinks(Beverages):
    def __init__(self, item_name, budget, price, item_type, item_qty):
        super().__init__(item_name, budget, price, item_qty)
        self.item_type = item_type

    def __str__(self):# method to return the type of the item
        return super().__str__() + f' of {self.item_type} size ' \
                                   f'\nCost: ${self.price} ' \
                                   f'\nQty: {self.item_qty}' \
                                   f'\nTotal: {self.get_total()}'

    def get_total(self):  # method to return the total cost of the item
        return self.price * self.item_qty
