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
            item_quantity = item.get_quantity()
            total_quantity += item_quantity
        return total_quantity

    def get_all_products(self):
        active_products = []
        for item in self.list_of_products:
            if item.active:
                active_products.append(item)
        return active_products


    def order(self, shopping_list):
        total_price = 0
        for product, qty in shopping_list:
            if product.active:
                price = product.buy(qty)
                if isinstance(price, float):
                    total_price += price
                    return total_price
                else:
                    return price
            else:
                return f"{product}is not active"







