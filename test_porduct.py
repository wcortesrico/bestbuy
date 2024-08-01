import pytest
import products

def test_create_new_product():
    products.Product("ipod", 150, 200)

def test_create_product_emptyname():
    with pytest.raises(ValueError, match="Name cannot be empty"):
        products.Product("", 130, 100)

def test_product_wrongprice():
    with pytest.raises(ValueError, match="Price cannot be less than cero"):
        products.Product("ipod", -2, 200)

def test_product_inactive():
    ipod = products.Product("ipod", 30, 0)
    assert ipod.is_active() == False

def test_modifies_quantity():
    ipod = products.Product("ipod", 20, 10)
    ipod.buy(2)
    assert ipod.quantity == 8

def test_buy_toomuch():
    ipod = products.Product("ipod", 160, 50)
    with pytest.raises(ValueError, match="There are not enough items to buy"):
        ipod.buy(51)

test_create_new_product()
test_create_product_emptyname()
test_product_wrongprice()
test_buy_toomuch()
