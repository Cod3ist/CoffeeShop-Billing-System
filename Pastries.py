class Pastries: #SUPERCLASS
    def __init__(self, item_name, budget, price, item_pieces):
        self.budget = budget
        self.price = price
        self.item_pieces = item_pieces
        self.item_name = item_name

    def __str__(self): #method to return the item name
        return f'A {self.item_name}'

    def get_change(self, budget): #method to return the balance amount to be given
        return budget - self.price * self.item_pieces

class Doughnuts(Pastries):
    def __init__(self, item_name, budget, price, item_type, item_pieces):
        super().__init__(item_name, budget, price, item_pieces)
        self.item_type = item_type

    def __str__(self): #method to return the details of the item ordered
        return super().__str__() + f' {self.item_type} doughnut'\
                                 + f'\nCost: {self.price}'\
                                 + f'\nPieces: {self.item_pieces}'\
                                 + f'\nTotal: {self.get_total(self.price, self.item_pieces)}'

    def check_type(self): #method to check the type of the item and to add the extra amount accordingly
        item_price = 0
        if self.item_type.lower() == 'cream filled':
            item_price = 5
        return item_price * self.item_pieces

    def get_total(self, price, item_pieces): #method to get the total amount of the item ordered
        price_total = self.price * self.item_pieces
        return price_total + self.check_type()

    def change(self, budget): #method to get the balance amount
        if self.item_type == 'cream filled':
            return self.get_change(budget) - 5 * self.item_pieces
        else:
            return self.get_change(budget)

class Cupcakes(Pastries):
    def __init__(self, item_name, budget, price, item_type, item_pieces):
        super().__init__(item_name, budget, price, item_pieces)
        self.item_type = item_type


    def get_total(self): #method to get the total amount of the item ordered
     return self.price * self.item_pieces

    def __str__(self): #method to return the details of the item ordered
        return super().__str__() + f' {self.item_type} Cupcake' \
               + f'\nCost: {self.price}' \
               + f'\nPieces: {self.item_pieces} '\
               + f'\nTotal: {self.get_total()}'

