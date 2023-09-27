from lib.basket import Basket
import pytest
from unittest.mock import Mock
from lib.menu import Menu

# TESTING CLASS: Basket()
# Available modules:
		# add_basket():
		# remove_basket():
		# view_basket():
		# view_total():

def test_add_basket_2items_added():
    test_basket = Basket()
    test_basket.add_basket("Margarita")
    test_basket.add_basket("Chocolate cake")
    assert test_basket.view_basket() == "YOUR BASKET:\nMargarita | x 1 | 14.99\nChocolate cake | x 1 | 3.99\n\n\nTOTAL: 18.98"

def test_add_basket_error_no_item():
    test_basket = Basket()
    with pytest.raises(Exception) as err:
        test_basket.add_basket("MarGUrita")
    assert str(err.value) == "No such dish in the menu!"

def test_view_basket_error_empty():
    test_basket = Basket()
    with pytest.raises(Exception) as err:
        test_basket.view_basket()
    assert str(err.value) == "Basket is empty!"

def test_remove_1item():
    test_basket1 = Basket()
    test_basket1.add_basket("Margarita")
    test_basket1.add_basket("Chocolate cake")
    test_basket1.remove_basket("Margarita")
    assert test_basket1.view_basket() == "YOUR BASKET:\nChocolate cake | x 1 | 3.99\n\n\nTOTAL: 3.99"

def test_view_total():
    test_basket = Basket()
    test_basket.add_basket("Margarita")
    assert test_basket.view_total() == 14.99

# UNIT TESTS
def test_add_basket_2items_added_unit():
    fake_menu = Mock()
    fake_menu.menu = [
        {"dish": "New Margarita", "price": 14.99, "category": "main", "quantity": 0},
        {"dish": "Chocolate cake", "price": 3.99, "category": "dessert", "quantity": 0}
                                           ]
    test_basket = Basket(fake_menu)
    test_basket.add_basket("New Margarita")
    test_basket.add_basket("Chocolate cake")
    assert test_basket.view_basket() == "YOUR BASKET:\nNew Margarita | x 1 | 14.99\nChocolate cake | x 1 | 3.99\n\n\nTOTAL: 18.98"

def test_remove_1item_unit():
    fake_menu = Mock()
    fake_menu.menu = [
        {"dish": "New Margarita", "price": 14.99, "category": "main", "quantity": 0},
        {"dish": "Chocolate cake", "price": 3.99, "category": "dessert", "quantity": 0}
                                           ]
    test_basket = Basket(fake_menu)
    test_basket.add_basket("New Margarita")
    test_basket.add_basket("Chocolate cake")
    test_basket.remove_basket("New Margarita")
    assert test_basket.view_basket() == "YOUR BASKET:\nChocolate cake | x 1 | 3.99\n\n\nTOTAL: 3.99"