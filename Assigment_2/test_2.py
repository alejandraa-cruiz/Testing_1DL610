import pytest
from pytest import fixture
from online_shopping_cart.checkout.checkout_process import checkout, check_cart


PRODUCTS_DATA = [
    {"Product": "Apple", "Price": "2", "Units": "10"},
    {"Product": "Banana", "Price": "1", "Units": "15"},
]

class Product:
    def __init__(self, name, price, units):
        self.name = name
        self.price = price
        self.units = units

    def __eq__(self, other):
        return (self.name == other.name and
                self.price == other.price and
                self.units == other.units)

    def add_product_unit(self):
        self.units += 1



'''
fixtures
'''
@fixture
def replace_data(mocker):
    return mocker.patch("online_shopping_cart.product.product_data.get_csv_data", return_value=PRODUCTS_DATA)

@fixture
def mock_user(mocker):
    user = mocker.Mock()
    user.name = "TestUser"
    user.wallet = 20
    return user

@fixture
def mock_cart(mocker):
    cart = mocker.Mock()
    cart.items = [Product("Apple", 2, 1)]
    cart.get_total_price.return_value = 2.0
    cart.retrieve_items.return_value = [Product("Apple", 2, 1)]
    cart.is_empty.return_value = False
    return cart

@fixture
def mock_global_products(mocker):
    # cart = list[Product]()
    cart = mocker.patch("online_shopping_cart.checkout.checkout_process.global_products",
                 [Product("Apple", 2, 10), Product("Banana", 1, 15)])
    return cart

@fixture
def mock_input(mocker):
    mock_input=mocker.patch("online_shopping_cart.user.user_interface.UserInterface.get_user_input",
                            side_effect=["n","y","x","x","x"])
    return mock_input

@fixture
def mock_display(mocker):
    return mocker.patch("online_shopping_cart.checkout.checkout_process.display_cart_items")


#test case 1
def test_case_1(mock_user,mock_cart,capsys):
    mock_cart.items = []
    checkout(mock_user, mock_cart)

    assert mock_user.wallet == 20
    mock_cart.clear_items.assert_not_called()

    captured = capsys.readouterr()
    assert "Your basket is empty. Please add items before checking out." in captured.out


#test case 2
def test_case_2(mock_cart,mock_user,capsys):
    checkout(mock_user, mock_cart)

    assert mock_user.wallet == 18
    captured = capsys.readouterr()
    mock_cart.clear_items.assert_called_once()
    assert "Thank you for your purchase" in captured.out

#test case 3
def test_case_3(mock_user,mock_cart,capsys):
    mock_cart.get_total_price.return_value = 25.0
    checkout(mock_user, mock_cart)

    assert mock_user.wallet == 20
    mock_cart.clear_items.assert_not_called()

    captured = capsys.readouterr()
    assert "You don't have enough money to complete the purchase." in captured.out


#test case 4
def test_case_4(mock_user,mock_cart,mock_input,mock_display):
    mock_input.side_effect = ["y"]
    mock_cart.items=[]
    mock_cart.is_empty.return_value = True
    result = check_cart(mock_user, mock_cart)

    assert mock_display.call_count == 1
    assert result is False
    assert mock_input.call_count == 0

#test case 5
def test_case_5(mocker,mock_user,mock_cart,mock_input,mock_display):
    mock_input.side_effect = ["y"]
    mock_checkout = mocker.patch("online_shopping_cart.checkout.checkout_process.checkout")
    check_cart(mock_user, mock_cart)
    assert mock_checkout.call_count == 1
    mock_cart.remove_item.assert_not_called()

#test case 6
def test_case_6(mock_user,mock_cart,mock_input,mock_display,capsys):
    result = check_cart(mock_user, mock_cart)

    mock_cart.remove_item.assert_not_called()
    mock_display.assert_called_with(mock_cart)
    assert mock_display.call_count == 2
    assert result is False
    captured = capsys.readouterr()
    assert "Invalid input. Please try again." in captured.out

#test case 7
def test_case_7(mock_user,mock_cart,mock_input,mock_display):
    mock_input.side_effect=["n","y","c","n","n"]
    result = check_cart(mock_user, mock_cart)

    mock_cart.remove_item.assert_not_called()
    mock_display.assert_called_with(mock_cart)
    assert mock_display.call_count == 3
    assert result is False
    assert mock_input.call_count == 5

#test case 8
def test_case_8(mock_user,mock_cart,mock_input,mock_display,capsys):
    result = check_cart(mock_user, mock_cart)

    mock_cart.remove_item.assert_not_called()
    mock_display.assert_called_with(mock_cart)
    assert mock_display.call_count == 2
    assert result is False
    captured = capsys.readouterr()
    assert "Invalid input. Please try again." in captured.out

#test case 9
def test_case_9(mock_user, mock_cart,mock_global_products,mock_input,mock_display):
    mock_input.side_effect = ["n","y","1","n","n"]
    check_cart(mock_user, mock_cart)

    assert mock_display.call_count == 2
    mock_cart.remove_item.assert_called_once()
    mock_display.assert_called_with(mock_cart)
    # stock
    assert mock_global_products[0].units == 11

#test case 10
def test_case_10(mock_user, mock_cart,mock_global_products,mock_input,mock_display,capsys):
    mock_input.side_effect = ["n","y","-1","n","n"]
    result = check_cart(mock_user, mock_cart)

    assert mock_display.call_count == 2
    assert result is False
    captured = capsys.readouterr()
    assert "Invalid input. Please try again." in captured.out

