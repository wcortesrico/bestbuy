class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        if not type(self.quantity) is int:
            raise TypeError("The given parameter is not a float")
        return self.quantity

    def set_quantity(self, quantity):
        if not type(quantity) is int:
            raise TypeError("The given parameter is not an integer")
        try:
            if self.quantity <= 0:
                self.active = False
            self.quantity = quantity
        except TypeError as e:
            print(e)

    def is_active(self):
        if self.active:
            return True
        else:
            return False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if isinstance(quantity, int):
            if self.quantity >= quantity:
                self.quantity -= quantity
                total_price = self.price * quantity
                if self.quantity <= 0:
                    self.deactivate()
                return total_price
        else:
            print("This is not an int")