from abc import ABC, abstractproperty
import products

class Promotion(ABC):
    def __init__(self, promotion):
        self.promotion = promotion
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, promotion):
        super().__init__(promotion)
        self.promotion = promotion

    def apply_promotion(self, product, quantity):
        total_price = 0
        n = 1
        for i in range(quantity):
            if n % 2 == 1:
                total_price += product.price
            else:
                total_price += product.price / 2
            n += 1
        return total_price


class ThirdOneFree(Promotion):
    def __init__(self, promotion):
        super().__init__(promotion)
        self.promotion = promotion

    def apply_promotion(self, product, quantity):
        total_price = 0
        n = 1
        for i in range(quantity):
            if n % 3 != 0:
                total_price += product.price
            else:
                pass
            n += 1
        return total_price


class PercentDiscount(Promotion):
    def __init__(self, promotion, percent):
        super().__init__(promotion)
        self.percent = percent
        self.promotion = promotion

    def apply_promotion(self, product, quantity):
        total_price = product.price * quantity * (1 - (self.percent / 100))
        return total_price
