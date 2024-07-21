import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def print_list_products(object):
    n = 1
    print("------")
    for product in object.list_of_products:
        print(f"{n}. {product.show()}")
        n += 1
    print("------")
def start(store_object):
    while True:
        print("\n   Store Menu   ")
        print("   -------   ")
        print("1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit")
        option_number = input("Please choose a number: ")
        if option_number == "1":
            print_list_products(store_object)
        elif option_number == "2":
            print(f"Total of {best_buy.get_total_quantity()} items in store")
        elif option_number == "3":
            print_list_products(store_object)
            print("When you want to finish the order, enter empty text")
            keep_order = True
            shopping_list = []
            products = best_buy.get_all_products()
            while keep_order:
                try:
                    option_order = input("Which product # do you want? ")
                    qty_order = int(input("What amount do you want? "))
                except ValueError as e:
                    keep_order = False
                if option_order == "":
                    keep_order = False
                    break
                elif option_order == "1":
                    shopping_list.append((products[0], qty_order))
                    print("Item added to list\n")
                elif option_order == "2":
                    shopping_list.append((products[1], qty_order))
                    print("Item added to list\n")
                elif option_order == "3":
                    shopping_list.append((products[2], qty_order))
                    print("Item added to list\n")
            total_price = best_buy.order(shopping_list)
            print(f"Order made! total payment {total_price}")
        elif option_number == "4":
            break
        else:
            pass
start(best_buy)


