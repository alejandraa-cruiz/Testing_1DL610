import pytest
from unittest.mock import MagicMock
from Assigment_1.online_shopping_cart.user.user_interface import UserInterface
from Assigment_1.online_shopping_cart.checkout.checkout_process import checkout_and_payment, display_products_available_for_purchase

# Stubbed mock data
mock_login_info = {'username': 'Rover', 'wallet': 100}
global_products = [{"Product": "Apple", "Price": "2", "Units": "10"},
    {"Product": "Banana", "Price": "1", "Units": "15"},]

# Fixtures to mock dependencies
@pytest.fixture
def mock_display_products_available_for_purchase():
    mock = MagicMock()
    mock.return_value = 'd'
    return mock

@pytest.fixture
def mock_display_products_available_for_purchase():
    mock = MagicMock()
    return mock

def test_checkout_and_payment_calls_display_products(mock_get_user_input, mock_display_products_available_for_purchase):
    # Arrange: Replace the actual methods with the mock fixtures
    UserInterface.get_user_input = mock_get_user_input
    global display_products_available_for_purchase  # Refer to the global function inside the test
    display_products_available_for_purchase = mock_display_products_available_for_purchase

    # Act: Call the checkout_and_payment function with mocked login info
    checkout_and_payment(mock_login_info)

    # Assert: Ensure that display_products_available_for_purchase was called once
    mock_display_products_available_for_purchase.assert_called_once()

