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

# def test_add_view_basket_item_added_integration():
#     test_menu = Menu()
#     test_basket = Basket()
#     item1 = Mock()
#     item1.MenuItem_name.return_value = "Pizza1"
#     item1.MenuItem_price.return_value = 14.99
#     item1.MenuItem_quantity.return_value = 0
#     item1.MenuItem_category.return_value = "main"
    
#     test_menu.add_position(item1)

#     test_basket.add_basket("Pizza1")

#     assert test_basket.view_basket() == "YOUR BASKET:\nPizza1 | x 1 | 14.99\n\nTOTAL: 14.99"
#     assert item1.MenuItem_quantity.return_value == 1

# def test_add_view_basket_view_total_double_item_added_integration():
#     item1 = Mock()
#     item1.MenuItem_name.return_value = "Pizza1"
#     item1.MenuItem_price.return_value = 15.00
#     item1.MenuItem_quantity.return_value = 0
#     item1.MenuItem_category.return_value = "main"

#     test_menu = Menu()
#     test_menu.add_position(item1)

#     test_basket = Basket()
#     test_basket.add_basket("Pizza1")
#     test_basket.add_basket("Pizza1")

#     assert test_basket.view_basket() == "YOUR BASKET:\nPizza1 | x 2 | 30.00\nTOTAL: 30.00"
    

# def test_remove_1item_and_empty_basket_error_integration():
#     item1 = Mock()
#     item1.MenuItem_name.return_value = "Pizza1"
#     item1.MenuItem_price.return_value = 15.00
#     item1.MenuItem_quantity.return_value = 0
#     item1.MenuItem_category.return_value = "main"

#     test_menu = Menu()
#     test_menu.add_position(item1)

#     test_basket = Basket()
#     test_basket.add_basket("Pizza1")
#     test_basket.remove_basket("Pizza1")

#     with pytest.raises(Exception) as err:
#         test_basket.view_basket()
    
#     assert  str(err.value) == "Sorry! Your basket is empty!"