import pytest
from pytest import fixture
from online_shopping_cart.product.product_data import get_products
from online_shopping_cart.checkout.checkout_process import checkout, check_cart
from online_shopping_cart.user.user_interface import UserInterface



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



'''
get_products()
'''
#1.1 invalid file
#IEC1
def test_get_products_invalid_file(mocker,mock_global_products, mock_input, mock_display):
    mocker.patch("online_shopping_cart.product.product_data.get_csv_data", side_effect=FileNotFoundError)

    with pytest.raises(FileNotFoundError):
        get_products(file_name="nonexistent_file.csv")

#1.2 invalid csv content
#IEC2
def test_get_products_invalid_csv(mocker,mock_global_products, mock_input, mock_display):
    mocker.patch("online_shopping_cart.product.product_data.get_csv_data", return_value=[
        {"Name": "Apple", "Cost": "2.5"},
    ])

    with pytest.raises(KeyError):
        get_products()

#1.3 success
#VEC1
def test_get_products_success(replace_data):
    products = get_products()
    print(replace_data)

    expected_products = [
        Product(name="Apple", price=2, units=10),
        Product(name="Banana", price=1, units=15),
    ]

    assert products == expected_products
    # get_csv_data whether be used
    replace_data.assert_called_once()

#1.4 csv file is empty
#VEC2
def test_get_products_empty(replace_data):
    replace_data.return_value = []
    products = get_products()
    print(replace_data)

    assert products == []
    replace_data.assert_called_once()



'''
checkout()
'''
#2.1 success
#EC1
def test_checkout_success(mock_cart,mock_user,capsys):
    checkout(mock_user, mock_cart)

    assert mock_user.wallet == 18
    mock_cart.clear_items.assert_called_once()
    captured = capsys.readouterr()
    mock_cart.clear_items.assert_called_once()
    assert "Thank you for your purchase" in captured.out


#2.2 no item
#EC2
def test_checkout_no_item(mock_user,mock_cart,capsys):
    mock_cart.items = []
    checkout(mock_user, mock_cart)

    assert mock_user.wallet == 20
    mock_cart.clear_items.assert_not_called()

    captured = capsys.readouterr()
    assert "Your basket is empty. Please add items before checking out." in captured.out

#2.3 total_price > user.wallet
#EC3
def test_checkout_overrun(mock_user,mock_cart,capsys):
    mock_cart.get_total_price.return_value = 25.0
    checkout(mock_user, mock_cart)

    assert mock_user.wallet == 20
    mock_cart.clear_items.assert_not_called()

    captured = capsys.readouterr()
    assert "You don't have enough money to complete the purchase." in captured.out

#2.4 item's price is 0
#EC4
def test_checkout_zero_item(mock_user,mock_cart,capsys):
    mock_cart.items = [Product(name="Apple", price=0, units=1)]
    mock_cart.get_total_price.return_value = 0
    checkout(mock_user, mock_cart)

    assert mock_user.wallet == 20
    mock_cart.clear_items.assert_called_once()
    captured = capsys.readouterr()
    assert "Thank you for your purchase" in captured.out



'''
check_cart()
'''
#3.1 invalid input & reach the remove item stage
#IEC1
def test_check_cart_invalid_input_1(mock_user,mock_cart,mock_input,mock_display,capsys):
    result = check_cart(mock_user, mock_cart)

    mock_cart.remove_item.assert_not_called()
    mock_display.assert_called_with(mock_cart)
    assert mock_display.call_count == 2
    assert result is False
    assert mock_input.call_count == 5
    captured = capsys.readouterr()
    assert "Invalid input. Please try again." in captured.out

#3.2 invalid input & doesn't reach the remove item stage
#IEC2
def test_check_cart_invalid_input_2(mock_user,mock_cart,mock_input,mock_display):
    mock_input.side_effect= ["n","n"]
    result = check_cart(mock_user, mock_cart)

    mock_cart.remove_item.assert_not_called()
    mock_display.assert_called_with(mock_cart)
    assert mock_display.call_count == 1
    assert result is False
    assert mock_input.call_count == 2

#3.3 empty input
#IEC3
def test_check_cart_invalid_input_3(mock_user,mock_cart,mock_input,mock_display):
    mock_input.side_effect = ["","",""]
    result = check_cart(mock_user, mock_cart)

    assert result is False
    assert mock_display.call_count == 1
    assert result is False
    mock_cart.remove_item.assert_not_called()


#3.4 jump to check out
#VEC1
def test_check_cart_checkout(mocker,mock_user,mock_cart,mock_input,mock_display):
    mock_input.side_effect = ["y"]
    mock_checkout = mocker.patch("online_shopping_cart.checkout.checkout_process.checkout")
    check_cart(mock_user, mock_cart)
    assert mock_checkout.call_count == 1
    mock_cart.remove_item.assert_not_called()

#3.5 check items list
#VEC2
def test_check_cart_check_items(mock_user,mock_cart,mock_input,mock_display):
    mock_input.side_effect=["n","y","c","n","n"]
    result = check_cart(mock_user, mock_cart)

    mock_cart.remove_item.assert_not_called()
    mock_display.assert_called_with(mock_cart)
    assert mock_display.call_count == 3
    assert result is False
    assert mock_input.call_count == 5

#3.6 remove items successfully
#VEC3
def test_check_cart_remove_items_success(mock_user, mock_cart,mock_global_products,mock_input,mock_display):
    mock_input.side_effect = ["n","y","1"]
    check_cart(mock_user, mock_cart)

    assert mock_display.call_count == 2
    assert mock_input.call_count == 3
    mock_cart.remove_item.assert_called_once()
    mock_display.assert_called_with(mock_cart)
    # stock
    assert mock_global_products[0].units == 11

#3.7 cart is empty
#VEC4
def test_check_cart_empty_cart(mock_user,mock_cart,mock_input,mock_display):
    mock_input.side_effect = ["y"]
    mock_cart.items=[]
    mock_cart.is_empty.return_value = True
    result = check_cart(mock_user, mock_cart)

    assert mock_display.call_count == 1
    assert result is False
    assert mock_input.call_count == 0