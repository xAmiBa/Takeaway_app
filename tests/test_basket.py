from lib.basket import Basket
from lib.menu import Menu
import pytest
from unittest.mock import Mock

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
    assert test_basket.view_basket() == "YOUR BASKET:\nMargarita | x 1 | 14.99\nChocolate Cake | x 1 | 3.99"

def test_remove_1item():
    pass

def test_view_basket():
    pass

def test_view_total():
    pass
