import products
import store
import promotions

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125, quantity=0),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", 30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = store.Store(product_list)

def print_list_products(object):
    n = 1
    print("------")
    for product in object.get_all_products():
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
            print(f"Total of {store_object.get_total_quantity()} items in store")
        elif option_number == "3":
            print("")
            products = store_object.get_all_products()
            n = 1
            for product in products:
                print(f"{n}. {product.show()}")
                n += 1
            print("When you want to finish the order, enter empty text")
            keep_order = True
            shopping_list = []
            while keep_order:
                try:
                    option_order = input("\nWhich product # do you want? ")
                    qty_order = input("What amount do you want? ")
                except ValueError as e:
                    keep_order = False
                if option_order == "" and qty_order == "":
                    keep_order = False
                    break
                index = int(option_order) - 1
                shopping_list.append((products[index], int(qty_order)))
                print("Item added to list\n")
            total_price = best_buy.order(shopping_list)
            print(total_price)
        elif option_number == "4":
            break
        else:
            pass
start(best_buy)


