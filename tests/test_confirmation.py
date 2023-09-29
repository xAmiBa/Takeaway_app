from lib.confirmation import *
from unittest.mock import Mock, patch
from lib.restaurant import Restaurant
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

def test_checkout_and_send_txt():
    text_sender = Mock()
    text_sender.phone_number = "7900479648"
    text_sender.message_body.return_value = "Mocked text message!"
    assert text_sender.send_txt == True