from lib.menu import Menu
import pytest
from unittest.mock import Mock 
import json

# TESTING CLASS: Menu()
# Available modules:
		# menu_view():
		# add_position):

def test_add_position_menu_viev():
    test_menu = Menu()
    assert test_menu.menu_view()[:37] == "*** MENU ***\nMAINS:\nMargarita | 14.99"