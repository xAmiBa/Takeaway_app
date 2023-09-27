from lib.confirmation import *
from unittest.mock import Mock
import pytest

# TESTING CLASS: Confirmation()
# Available modules:
		# send_txt():

def test_if_number_input_is_formatted():
    test = Confirmation("6666666666")
    assert test.phone_number == "+446666666666"

def test_short_number_error():
    with pytest.raises(Exception) as err:
        test = Confirmation("66666")
    assert str(err.value) == "The number is too short!"

# UNIT TESTING 
#TODO
