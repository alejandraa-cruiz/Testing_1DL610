import pytest
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
def mock_1_2_1(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input",
        side_effect=["j", "l", "y"],
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
def mock_2_2_1(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input",
        side_effect=["@#$", "l", "y"],
    )

@pytest.fixture
def mock_check_cart(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.checkout.checkout_process.check_cart",
        return_value="Successful checkout",
    )

@pytest.fixture
def mock_3_2_1(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input",
        side_effect=[" l", "l", "y"],
    )

@pytest.fixture
def mock_3_2_1(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input",
        side_effect=[" l", "l", "y"],
    )

@pytest.fixture
def mock_4_2_1(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input",
        side_effect=["1867", "l", "y"],
    )
@pytest.fixture
def mock_4_2_2(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input",
        side_effect=["-897", "l", "y"],
    )
@pytest.fixture
def mock_4_2_3(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input",
        side_effect=["9%3", "l", "y"],
    )

@pytest.fixture
def mock_4_2_4(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input",
        side_effect=["8.9", "l", "y"],
    )
# TC 1.1 Display list of products
def test1_1_1_checkout_and_payment_calls_display_products(
    mock_1_1_1, mock_display_products_available_for_purchase
):
    print("Test: test_checkout_and_payment_calls_display_products")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    mock_display_products_available_for_purchase.assert_called_once()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test1_1_2_checkout_and_payment_calls_display_products(
    mock_1_1_2, mock_display_products_available_for_purchase
):
    print("Test: test_checkout_and_payment_calls_display_products")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    mock_display_products_available_for_purchase.assert_called_once()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test1_1_3_checkout_and_payment_calls_display_products(
    mock_1_1_3, mock_display_products_available_for_purchase
):
    print("Test: test_checkout_and_payment_calls_display_products")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    mock_display_products_available_for_purchase.assert_called_once()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test1_2_1invalid_input(
        capfd, mock_1_2_1
):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    out, err = capfd.readouterr()
    assert "Invalid input. Please try again." in out
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

#TC2.1
def test2_1_1_checkout_and_payment_calls_check_cart(
    mock_2_1_1, mock_check_cart
):
    print("Test: test_checkout_and_payment_calls_display_products")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    mock_check_cart.assert_called_once()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test2_1_2_checkout_and_payment_calls_check_cart(
    mock_2_1_2, mock_check_cart
):
    print("Test: test_checkout_and_payment_calls_display_products")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    mock_check_cart.assert_called_once()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test2_1_3_checkout_and_payment_calls_check_cart(
    mock_2_1_3, mock_check_cart
):
    print("Test: test_checkout_and_payment_calls_display_products")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    mock_check_cart.assert_called_once()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test2_2_1invalid_input(
        capfd, mock_2_2_1
):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    out, err = capfd.readouterr()
    assert "Invalid input. Please try again." in out
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test3_2_1invalid_input(
        capfd, mock_2_2_1
):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    out, err = capfd.readouterr()
    assert "Invalid input. Please try again." in out
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test4_2_1invalid_input(
        capfd, mock_4_2_1
):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    out, err = capfd.readouterr()
    assert "Invalid input. Please try again." in out
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test4_2_2invalid_input(
        capfd, mock_4_2_2
):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    out, err = capfd.readouterr()
    assert "Invalid input. Please try again." in out
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test4_2_3invalid_input(
        capfd, mock_4_2_3
):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    out, err = capfd.readouterr()
    assert "Invalid input. Please try again." in out
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test4_2_4invalid_input(
        capfd, mock_4_2_4
):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        checkout_and_payment(mock_login_info)
    out, err = capfd.readouterr()
    assert "Invalid input. Please try again." in out
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0