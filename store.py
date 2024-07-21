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
            if not type(qty) is int:
                raise TypeError("The second value is not an integer")
            try:
                price = product.buy(qty)
                total_price += price
            except TypeError as e:
                print(e)
        return total_price


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

"""""
store = Store(product_list)
print(store.list_of_products)
for product in store.list_of_products:
    product.show()
products = store.get_all_products()
print(store.get_total_quantity())
print(store.order([(products[0], 1), (products[1], 2)]))
"""""






