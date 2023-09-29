from lib.basket import Basket
from lib.menu import Menu
from unittest.mock import Mock
import pytest

# TESTING CLASS: Basket()
# Available modules:
		# add_basket():
		# remove_basket():
		# view_basket():
		# view_total():

# TESTING CLASS: Menu()
# Available modules:
		# menu_view():
		# add_position):
 
def test_add_view_basket_item_added_integration():
    test_menu = Menu()
    test_basket = Basket()
    test_basket.add_basket("Margarita")

    assert test_basket.view_basket() == "YOUR BASKET:\nMargarita | x 1 | 14.99\n\n\nTOTAL: 14.99"

def test_remove_1item_and_empty_basket_error_integration():
    test_menu = Menu()
    test_basket = Basket()
    test_basket.add_basket("Margarita")
    test_basket.remove_basket("Margarita")
    with pytest.raises(Exception) as err:
        test_basket.view_basket()
    assert  str(err.value) == "Basket is empty!"