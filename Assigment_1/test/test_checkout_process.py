import pytest
from pytest import mark
from pytest import fixture
from Assigment_1.online_shopping_cart.checkout.checkout_process import (
    checkout_and_payment,
    display_products_available_for_purchase,
)

# Stubbed mock data
mock_login_info = {"username": "Rover", "wallet": 50}


@fixture
def mock_user_input(mocker):
    def _mock_user_input(inputs):
        return mocker.patch(
            'Assigment_1.online_shopping_cart.user.user_interface.UserInterface.get_user_input',
            side_effect=inputs,
        )
    return _mock_user_input

@fixture
def mock_display_products_available_for_purchase(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.checkout.checkout_process.display_products_available_for_purchase",
        return_value="Products available for purchase",
    )

@fixture
def mock_check_cart(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.checkout.checkout_process.check_cart",
        return_value="Successful checkout",
    )

@fixture
def mock_logout(mocker):
    return mocker.patch(
        "Assigment_1.online_shopping_cart.checkout.checkout_process.logout",
    )

#Test data
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
def test_display_products(
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


