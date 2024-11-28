import pytest
from unittest.mock import MagicMock
from Assigment_1.online_shopping_cart.user.user_interface import UserInterface
from Assigment_1.online_shopping_cart.checkout.checkout_process import (
    checkout_and_payment,
    display_products_available_for_purchase,
)

# Stubbed mock data
mock_login_info = {"username": "Rover", "wallet": 50}


# Fixtures to mock dependencies
@pytest.fixture
def mock_1_1_1(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input",
        side_effect=["d", "l", "y"],
    )

@pytest.fixture
def mock_1_1_2(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input",
        side_effect=["d ", "l", "y"],
    )
@pytest.fixture
def mock_1_1_3(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input",
        side_effect=["D", "l", "y"],
    )

@pytest.fixture
def mock_display_products_available_for_purchase(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.checkout.checkout_process.display_products_available_for_purchase",
        return_value="Products available for purchase",
    )

@pytest.fixture
def mock_2_1_1(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input",
        side_effect=["c", "l", "y"],
    )

@pytest.fixture
def mock_2_1_2(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input",
        side_effect=["C", "L ", "y"],
    )

@pytest.fixture
def mock_2_1_3(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input",
        side_effect=["C ", "L", "y"],
    )

@pytest.fixture
def mock_check_cart(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.checkout.checkout_process.check_cart",
        return_value="Successful checkout",
    )


# TC 1.1 Display list of products
def test1_1_1_checkout_and_payment_calls_display_products(
    mock_1_1_1, mock_display_products_available_for_purchase
):
    print("Test: test_checkout_and_payment_calls_display_products")
    # Act: Call the checkout_and_payment function with mocked login info
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)

    # Assert: Ensure that display_products_available_for_purchase was called once
    mock_display_products_available_for_purchase.assert_called_once()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test1_1_2_checkout_and_payment_calls_display_products(
    mock_1_1_2, mock_display_products_available_for_purchase
):
    print("Test: test_checkout_and_payment_calls_display_products")
    # Act: Call the checkout_and_payment function with mocked login info
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)

    # Assert: Ensure that display_products_available_for_purchase was called once
    mock_display_products_available_for_purchase.assert_called_once()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test1_1_3_checkout_and_payment_calls_display_products(
    mock_1_1_3, mock_display_products_available_for_purchase
):
    print("Test: test_checkout_and_payment_calls_display_products")
    # Act: Call the checkout_and_payment function with mocked login info
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)

    # Assert: Ensure that display_products_available_for_purchase was called once
    mock_display_products_available_for_purchase.assert_called_once()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test2_1_1_checkout_and_payment_calls_check_cart(
    mock_2_1_1, mock_check_cart
):
    print("Test: test_checkout_and_payment_calls_display_products")
    # Act: Call the checkout_and_payment function with mocked login info
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)

    # Assert: Ensure that display_products_available_for_purchase was called once
    mock_check_cart.assert_called_once()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

#TC 3.1
def test2_1_2_checkout_and_payment_calls_check_cart(
    mock_2_1_2, mock_check_cart
):
    print("Test: test_checkout_and_payment_calls_display_products")
    # Act: Call the checkout_and_payment function with mocked login info
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)

    # Assert: Ensure that display_products_available_for_purchase was called once
    mock_check_cart.assert_called_once()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test2_1_3_checkout_and_payment_calls_check_cart(
    mock_2_1_3, mock_check_cart
):
    print("Test: test_checkout_and_payment_calls_display_products")
    # Act: Call the checkout_and_payment function with mocked login info
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)

    # Assert: Ensure that display_products_available_for_purchase was called once
    mock_check_cart.assert_called_once()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0