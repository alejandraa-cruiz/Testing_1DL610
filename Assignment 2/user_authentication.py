###############################
# USER AUTHENTICATION CLASSES #
###############################

# TODO: Task 1: validate password for registration
import re

from online_shopping_cart.user.user_card import CreditCardManager
from online_shopping_cart.user.user_data import UserDataManager
from online_shopping_cart.user.user_interface import UserInterface


class PasswordValidator:
    @staticmethod
    def is_valid(password) -> bool:
        if len(password) < 8:
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|" for char in password):
            return False
        return True


class UserAuthenticator:

    @staticmethod
    def login(username, password, data) -> dict[str, str | float | list] | None:
        is_user_registered: bool = False
        user_data = None

        # Check if the user exists in the data
        for entry in data:
            if entry['username'].lower() == username.lower():
                is_user_registered = True
                user_data = entry
                break

        if not is_user_registered:
            print('User is not registered.')
            return None

        # Check if the password is correct
        if user_data['password'].lower() == password.lower():
            print(f"Successfully logged in as {username}.")

            # Ask if the user wants to modify credit card details
            modify_credit_cards = UserInterface.get_user_input(
                prompt="Do you want to modify your credit card details? (yes/no): ")
            if modify_credit_cards.lower().startswith("y"):
                CreditCardManager.modify_credit_card(username, data)  # Modify card details

            # Continue with the regular flow (product selection)
            print("Search for products in inventory (type 'all' for the whole inventory): ")
            return {
                'username': user_data['username'],
                'wallet': user_data['wallet'],
                'credit_cards': user_data['credit_cards']
            }

        print('Login failed.')
        return None

    @staticmethod
    def register(username, password, data) -> None:
        # Validate the password using the PasswordValidator
        if not PasswordValidator.is_valid(password):
            print("Password does not meet the required criteria.")
            return

        # Prompt the user to enter credit card details
        credit_cards = []
        while True:
            add_card = UserInterface.get_user_input(prompt="Do you want to add a credit card? (yes/no): ")
            if add_card.lower().startswith("y"):
                card_number = UserInterface.get_user_input(prompt="Enter card number: ")
                expiry_date = UserInterface.get_user_input(prompt="Enter card expiry date (MM/YYYY): ")
                name_on_card = UserInterface.get_user_input(prompt="Enter name on card: ")
                cvv = UserInterface.get_user_input(prompt="Enter CVV: ")
                credit_cards.append({
                    'card_number': card_number,
                    'expiry_date': expiry_date,
                    'name_on_card': name_on_card,
                    'cvv': cvv
                })
            else:
                break

        # Add the new user to the data with the credit cards and save it
        data.append({
            'username': username,
            'password': password,
            'wallet': 0.0,
            'credit_cards': credit_cards
        })
        UserDataManager.save_users(data)
        print(f"User {username} registered successfully with credit cards!")
