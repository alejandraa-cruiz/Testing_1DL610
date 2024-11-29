import pytest
from pytest import mark
from pytest import fixture
from Assigment_1.online_shopping_cart.checkout.checkout_process import (
    checkout_and_payment,
    display_products_available_for_purchase, global_products,
)
from Assigment_1.online_shopping_cart.product.product import Product

# Stubbed mock data
mock_login_info = {"username": "Rover", "wallet": 50}

products = [
    Product("Apple", 2, 10),
    Product("Banana", 1, 15),
    Product("Orange", 1.5, 8),
    Product("Grapes", 3, 5),
    Product("Strawberry", 4, 12),
    Product("Watermelon", 10, 0),
    Product("Carrot", 0.5, 20),
    Product("Broccoli", 1.5, 10),
    Product("Tomato", 1, 15),
    Product("Cucumber", 1, 12),
    Product("Potato", 0.75, 18),
    Product("Onion", 0.8, 20),
    Product("Bell Pepper", 1.2, 8),
    Product("Lettuce", 2, 5),
    Product("Spinach", 2.5, 7),
    Product("Milk", 3, 10),
    Product("Eggs", 2, 24),
    Product("Cheese", 5, 8),
    Product("Chicken Breast", 7, 4),
    Product("Salmon", 10, 2),
    Product("Ground Beef", 6, 5),
    Product("Pasta", 1, 15),
    Product("Rice", 1.5, 10),
    Product("Bread", 2, 8),
    Product("Butter", 3, 6),
    Product("Yogurt", 2, 12),
    Product("Ice Cream", 4, 6),
    Product("Chocolate", 2.5, 8),
    Product("Coffee", 5, 4),
    Product("Tea", 2, 10),
    Product("Soda", 1.5, 12),
    Product("Water", 1, 20),
    Product("Juice", 3, 8),
    Product("Chips", 2.5, 10),
    Product("Cookies", 3, 8),
    Product("Cereal", 2, 12),
    Product("Oatmeal", 1.5, 15),
    Product("Peanut Butter", 3, 6),
    Product("Jelly", 2, 8),
    Product("Toothpaste", 1.5, 10),
    Product("Shampoo", 2, 8),
    Product("Soap", 1, 12),
    Product("Toilet Paper", 0.75, 24),
    Product("Towel", 4, 6),
    Product("Laundry Detergent", 3.5, 8),
    Product("Dish Soap", 1.5, 12),
    Product("Broom", 5, 4),
    Product("Trash Bags", 2, 10),
    Product("Light Bulbs", 1, 15),
    Product("Batteries", 3, 6),
    Product("Phone Charger", 5, 4),
    Product("Laptop", 800, 1),
    Product("Headphones", 50, 1),
    Product("Bluetooth Speaker", 30, 1),
    Product("TV", 500, 1),
    Product("Microwave", 80, 1),
    Product("Coffee Maker", 40, 1),
    Product("Toaster", 20, 1),
    Product("Blender", 30, 1),
    Product("Vacuum Cleaner", 100, 1),
    Product("Dumbbells", 20, 2),
    Product("Yoga Mat", 15, 1),
    Product("Running Shoes", 60, 1),
    Product("Backpack", 25, 1),
    Product("Sunglasses", 10, 1),
    Product("Hat", 8, 1),
    Product("Gloves", 5, 1),
    Product("Umbrella", 7, 1),
    Product("Notebook", 2, 5),
    Product("Pens", 0.5, 10),
    Product("Backpack", 15, 1)
]

# Function fixtures
@fixture
def mock_user_input(mocker):
    def _mock_user_input(inputs):
        return mocker.patch(
            'Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input',
            side_effect = inputs,
        )
    return _mock_user_input

@fixture
def mock_display_products_available_for_purchase(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.checkout.checkout_process.display_products_available_for_purchase",
        return_value = "Products available for purchase",
    )

@fixture
def mock_check_cart(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.checkout.checkout_process.check_cart",
    )

@fixture
def mock_logout(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.checkout.checkout_process.logout",
    )

@fixture
def mock_global_products(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.checkout.checkout_process.get_products",
        return_value = products
    )

#Test data EC1, EC2 and EC3
@mark.parametrize(
    "inputs, should_call_display, should_call_checkout, should_call_logout",
        [
            (["d", "l", "y"], True, False, False),  # TC 1.1.1
            (["d ", "l", "y"], True, False, False), # TC 1.1.2
            (["D", "l", "y"], True, False, False),  # TC 1.1.3
            (["j", "l", "y"], False, False, False), # TC 1.2.1

            (["c", "l", "y"], False, True, False),      # TC 2.1.1
            (["C ", "l", "y"], False, True, False),     # TC 2.1.2
            (["C ", "l", "y"], False, True, False),     # TC 2.1.3
            (["@#$", "l", "y"], False, False, False),   # TC 2.2.1

            (["l","y"], False, False, True),    # TC 3.1.1
            (["L ","y"], False, False, True),   # TC 3.1.2
            (["L", "y"], False, False, True),   # TC 3.1.3
            ([" l", "l", "y"], False, False, False),  # TC 3.2.1
        ],
)

# EC1, EC2 and EC3 User choices from menu
def test_choices_from_menu(
        capsys, mock_user_input, mock_display_products_available_for_purchase, mock_check_cart, mock_logout, inputs, should_call_display, should_call_checkout, should_call_logout
):
    mock_user_input(inputs)
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    if should_call_display: # R1.1
        mock_display_products_available_for_purchase.assert_called_once()
    elif should_call_checkout: # R2.1
        mock_check_cart.assert_called_once()
    elif should_call_logout: # R3.1
        mock_logout.assert_called_once()
    else: # R1.2, R2.2 and R3.2
        out, err = capsys.readouterr()
        assert "Invalid input. Please try again." in out
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

#Test data EC4
@mark.parametrize(
    "inputs, cart_message",
    [
        (["1", "l", "y"], "Apple added to your cart."),             # TC 4.1.1
        (["71", "l", "y"], "Backpack added to your cart."),         # TC 4.1.2
        (["50", "l", "y"], "Batteries added to your cart."),        # TC 4.1.3
        (["1867", "l", "y"], "Invalid input. Please try again."),   # TC 4.2.1
        (["-897", "l", "y"], "Invalid input. Please try again."),   # TC 4.2.2
        (["9%3", "l", "y"], "Invalid input. Please try again."),    # TC 4.2.3
        (["8.9", "l", "y"], "Invalid input. Please try again.")     # TC 4.2.4
    ]
)

#EC 4
def test_selecting_products(
        capsys, mock_user_input, mock_global_products, inputs, cart_message
):
    mock_user_input(inputs)
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    out, err = capsys.readouterr()
    assert cart_message in out # RF 4.1 and 4.2
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

# Test data EC 5
@mark.parametrize(
    "inputs, product_availability_message",
    [
        (["53", "l", "y"], "Headphones added to your cart."),            # TC 5.1.1
        (["61", "l", "y"], "Dumbbells added to your cart."),             # TC 5.1.2
        (["36","l", "y"], "Cereal added to your cart."),                 # TC 5.1.3
        (["6", "6", "l", "y"], "Sorry, Watermelon is out of stock."),    # TC 5.2.1
        (["55", "55", "l", "y"], "Sorry, TV is out of stock.")           # TC 5.2.2
    ]
)

#EC 5
def test_product_availability(
        capsys, mock_user_input, mock_check_cart, mock_logout, mock_global_products,inputs,product_availability_message
):
    mock_user_input(inputs)
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    out, err = capsys.readouterr()
    assert product_availability_message in out # RF 5.1 and 5.2
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0
