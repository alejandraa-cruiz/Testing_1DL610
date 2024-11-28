###############################
# USER AUTHENTICATION CLASSES #
###############################

# TODO: Task 1: validate password for registration
import re

from online_shopping_cart.user.user_data import UserDataManager


class PasswordValidator:
    @staticmethod
    def is_valid(password) -> bool:
        # Ensure the password has at least 8 characters
        if len(password) < 8:
            return False
        # Ensure the password has at least one uppercase letter
        if not any(char.isupper() for char in password):
            return False
        # Ensure the password has at least one special character
        if not any(char in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|" for char in password):
            return False
        # If all checks pass, the password is valid
        return True


class UserAuthenticator:

    @staticmethod
    def login(username, password, data) -> dict[str, str | float] | None:
        is_user_registered: bool = False



        for entry in data:
            #updated

            if entry['username'].lower() == username.lower():
                is_user_registered = True
            if is_user_registered:
                if entry['password'].lower() == password.lower():
                    print('Successfully logged in.')
                    return {
                        'username': entry['username'],
                        'wallet': entry['wallet']
                    }
                break

        if not is_user_registered:
            print('User is not registered.')
        else:
            print('Login failed.')
        return None

#TODO: Task 1: register username and password as new user to file with 0.0 wallet funds
    @staticmethod
    def register(username, password, data) -> None:
        # Validate the password using the PasswordValidator
        if not PasswordValidator.is_valid(password):
            print("Password does not meet the required criteria.")
            return

        # Add the new user to the data and save it
        data.append({'username': username, 'password': password, 'wallet': 0.0})
        UserDataManager.save_users(data)
        print(f"User {username} registered successfully!")

