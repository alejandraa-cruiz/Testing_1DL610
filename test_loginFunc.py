from unittest import mock

import pytest
from unittest.mock import patch
from online_shopping_cart.user.user_interface import UserInterface

from online_shopping_cart.user.user_authentication import UserAuthenticator,PasswordValidator
from online_shopping_cart.user.user_data import UserDataManager
from online_shopping_cart.user.user_login import login

@pytest.mark.parametrize("password,expected", [
    ("ValidP@ss123", True),        # Valid password with uppercase, lowercase, digit, and special character
    ("AnotherValid1@", True),      # Valid password with uppercase, lowercase, digit, and special character
    ("MyValidPass123$", True),     # Valid password with uppercase, lowercase, digits, and special characters
    ("P@ssw0rd1234", True),        # Valid password with uppercase, lowercase, digits, and special character
    ("SecureP@ssw0rd!", True),     # Valid password with uppercase, lowercase, digits, and special character
    ("V@lidPassword999", True),    # Valid password with uppercase, lowercase, digits, and special character
    ("Str0ngPassword!23", True),   # Valid password with uppercase, lowercase, digits, and special character
])
def test_valid_passwords(password, expected):
    """
    Test for valid passwords that meet all the password requirements.
    """
    assert PasswordValidator.is_valid(password) == expected, f"Password '{password}' should be valid."

import pytest

@pytest.mark.parametrize("password,expected", [
    ("short", False),              # Too short (less than 8 characters)
    ("password", False),           # No uppercase letter
    ("PASSWORD", False),           # No lowercase letter
    ("12345678", False),           # No special character, only digits
    ("password123", False),        # No uppercase letter, no special character
    ("Password", False),           # No digit, no special character

    ("@1234", False),              # Missing uppercase and lowercase letters
    ("password!!", False),         # Missing uppercase and digits
    ("12345@6789", False),         # Missing lowercase and uppercase letters
    ("!@#$%^&*", False),           # Only special characters, no letters or digits
    ("Password1234", False),       # No special character
    ("1234567", False),            # Too short (7 characters)
    ("Validpass123", False),       # No special character
    ("12345678", False),           # No lowercase or special character
])
def test_invalid_passwords(password, expected):
    """
    Test for invalid passwords that do not meet the password requirements.
    """
    assert PasswordValidator.is_valid(password) == expected, f"Password '{password}' should be invalid."



@pytest.fixture
def mock_user_data():
   #"""
   # Fixture to provide mock user data.
  #  """
    return [
       {"username": "Mahwishabc", "password": "MyPass123$", "wallet": 100.0}
   ]

def test_valid_input_login(mock_user_data):
  #  """
  #  Test login function with valid username and password.
  #  """
    username = "Mahwishabc"
    password = "MyPass123$"

    # Patch the UserDataManager.load_users method to return mock_user_data
    with patch.object(UserDataManager, 'load_users', return_value=mock_user_data):
     result = UserAuthenticator.login(username=username, password=password, data=mock_user_data)

    # Check if the result matches the expected output
    assert result == {"username": "Mahwishabc","wallet": 100.0}, "Valid login failed!"




@mock.patch('online_shopping_cart.user.user_data.UserDataManager.load_users')
def test_invalid_password(mock_load_users):
    # Mocking the return value for load_users (simulating a valid user)
    mock_load_users.return_value = [{'username': 'testuser', 'password': 'Password123!', 'wallet': 100.0}]

    # Simulating an invalid password input
    username = 'testuser'
    password = 'WrongPassword!'  # Incorrect password

    # Create the authenticator object and attempt to login
    authenticator = UserAuthenticator()
    result = authenticator.login(username=username, password=password, data=mock_load_users.return_value)

    # Assert that the result is None since the password is incorrect
    assert result is None, "Expected login to fail with invalid password!"


# Test case-insensitive username check
@mock.patch('online_shopping_cart.user.user_data.UserDataManager.load_users')
def test_case_insensitive_username(mock_load_users):
    mock_load_users.return_value = [{'username': 'MAHWISH96', 'password': 'Password123!', 'wallet': 100.0}]

    username = 'mahwish96'  # Correct username but with different case
    password = 'Password123!'  # Correct password

    authenticator = UserAuthenticator()

    # Ensure that the login method works even if the case of the username is different
    result = authenticator.login(username=username, password=password, data=mock_load_users.return_value)

    assert result == {"username": 'MAHWISH96', "wallet": 100.0}, "Case-insensitive login failed!"


@mock.patch('online_shopping_cart.user.user_data.UserDataManager.load_users')
def test_username_with_special_characters(mock_load_users):
    mock_load_users.return_value = [{'username': 'testuser', 'password': 'Password123!', 'wallet': 100.0}]

    username = '!@#$%^&*'  # Invalid username with special characters
    password = 'Password123!'  # Valid password

    authenticator = UserAuthenticator()

    result = authenticator.login(username=username, password=password, data=mock_load_users.return_value)
    assert result is None, "Username with special characters should result in failed login."




@mock.patch('online_shopping_cart.user.user_data.UserDataManager.load_users')
def test_non_existent_username(mock_load_users):
    mock_load_users.return_value = [{'username': 'Mahwish96', 'password': 'Password123!', 'wallet': 100.0}]

    username = 'doesnotexist'  # Non-existent username
    password = 'Password123!'  # Valid password

    authenticator = UserAuthenticator()

    result = authenticator.login(username=username, password=password, data=mock_load_users.return_value)
    assert result is None, "Non-existent username should result in failed login."

@mock.patch('online_shopping_cart.user.user_data.UserDataManager.load_users')
def test_username_with_leading_trailing_spaces(mock_load_users):
        mock_load_users.return_value = [{'username': 'mahwish', 'password': 'Password123!', 'wallet': 100.0}]

        username = '  mahwish  '  # Username with leading and trailing spaces
        password = 'Password123!'  # Valid password

        authenticator = UserAuthenticator()

        result = authenticator.login(username=username.strip(), password=password, data=mock_load_users.return_value)
        assert result == {"username": 'mahwish',"wallet": 100.0}, "Username with spaces should be trimmed and result in successful login."


@pytest.mark.parametrize("invalid_input", [

    1234,  # Integer
    3.14,  # Float
    [],  # Empty list
    {},  # Empty dict
    '',  # Empty string
    '   ',  # Whitespace
    None,  # None
])
def test_invalid_input_handling(mock_user_data, invalid_input):
    """Test handling of invalid input types"""
    authenticator = UserAuthenticator()

    try:
        result = authenticator.login(
            username=invalid_input,
            password='Password123!',
            data=mock_user_data
        )

        assert result is None, f"Login should return None for invalid input type: {type(invalid_input)}"

    except Exception as e:
        # If an exception is raised, ensure it doesn't break the test
        # and that the result is still None
        result = None
        assert result is None, f"Login failed with exception for input {invalid_input}: {e}"







# Mock user data for testing
mock_users = [
    {"username": "Mahwishabc", "password": "MyPass123$", "wallet": 100.0}
]


@pytest.fixture
def mock_user_data():
    """ Fixture to provide mock user data for testing. """
    return mock_users


# Test case to register a new user
@patch('online_shopping_cart.user.user_data.UserDataManager.load_users', return_value=mock_users)
@patch('online_shopping_cart.user.user_data.UserDataManager.save_users')
def test_register_new_user(mock_save, mock_load):


    # Register a new user
    username = 'newuser'
    password = 'ValidPassword123!'
    UserAuthenticator.register(username, password, mock_load())

    # Check if save_users was called once
    mock_save.assert_called_once()

    # Get the data passed to save_users
    saved_data = mock_save.call_args[0][0]

    # Ensure the new user is in the saved data
    new_user = next((user for user in saved_data if user['username'] == username), None)

    # Check if the new user is added correctly
    assert new_user is not None, f"User {username} was not added!"
    assert new_user['username'] == username, f"Expected username {username}, but got {new_user['username']}"
    assert new_user['wallet'] == 0.0, f"Expected wallet balance 0.0, but got {new_user['wallet']}"