import unittest
from unittest.mock import patch
import pytest
from online_shopping_cart.user.user_interface import UserInterface
from online_shopping_cart.product.product import Product
from online_shopping_cart.checkout.shopping_cart import ShoppingCart
from online_shopping_cart.user.user_logout import logout
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_cart_empty():
    """Fixture for an empty cart."""
    cart = MagicMock()
    cart.is_empty.return_value = True
    cart.retrieve_items.return_value = []
    return cart

@patch('online_shopping_cart.user.user_interface.UserInterface.get_user_input', return_value='y')
def test_logout_empty_cart_with_confirmation(mock_input, mock_cart_empty):
    """Test logout with an empty cart and user confirmation."""
    result = logout(mock_cart_empty)
    assert result is True

@patch('online_shopping_cart.user.user_interface.UserInterface.get_user_input', return_value='n')
def test_logout_empty_cart_with_decline(mock_input, mock_cart_empty):
    """Test logout with an empty cart and user decline."""
    result = logout(mock_cart_empty)
    assert result is False

@pytest.fixture
def mock_cart_non_empty():
    """Fixture for a non-empty cart."""
    cart = MagicMock()
    cart.is_empty.return_value = False
    cart.retrieve_items.return_value = ["Item1", "Item2"]
    return cart
def test_logout_non_empty_cart_with_confirmation():
    cart = MagicMock()
    cart.is_empty.return_value = False
    cart.retrieve_items.return_value = ["Item1"]

    with patch('online_shopping_cart.user.user_interface.UserInterface.get_user_input', return_value='y'):
        assert logout(cart) is True

def test_logout_non_empty_cart_with_decline():
    cart = MagicMock()
    cart.is_empty.return_value = False
    cart.retrieve_items.return_value = ["Item1"]

    with patch('online_shopping_cart.user.user_interface.UserInterface.get_user_input', return_value='n'):
        assert logout(cart) is False