class Product:
    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError("Name cannot be empty")
        else:
            self.name = name
        if price < 0:
            raise ValueError("Price cannot be less than cero")
        else:
            self.price = price
        if quantity == 0:
            self.active = False
            self.quantity = quantity
        elif quantity < 0:
            raise ValueError("Quantity cannot be negative")
        else:
            self.active = True
            self.quantity = quantity

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
            if self.quantity < quantity:
                raise ValueError("There are not enough items to buy")
            else:
                self.quantity -= quantity
                total_price = self.price * quantity
                if self.quantity <= 0:
                    self.deactivate()
                return total_price
        else:
            print("This is not an int")