import products
class Store:
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        self.list_of_products.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for item in self.list_of_products:
            item_quantity = item.quantity
            total_quantity += item_quantity
        return total_quantity

    def get_all_products(self):
        return self.list_of_products

    """""
    active_products = []
    for item in self.list_of_products:
        if item.active:
            active_products.append(item.name)
    return active_products
    """""

    def order(self, shopping_list):
        total_price = 0
        for product, qty in shopping_list:
            if not type(qty) is int:
                raise TypeError("The second value is not an integer")
            try:
                price = product.price * qty
                total_price += price
            except TypeError as e:
                print(e)
        return total_price








