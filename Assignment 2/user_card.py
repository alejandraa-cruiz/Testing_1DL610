from online_shopping_cart.user.user_interface import UserInterface
from online_shopping_cart.user.user_data import UserDataManager


class CreditCardManager:

    @staticmethod
    def modify_credit_card(username, data):
        user_data = None

        # Find user data from the list
        for entry in data:
            if entry['username'] == username:
                user_data = entry
                break

        if user_data is None:
            print("User not found.")
            return

        # Display message if no credit cards are found
        if not user_data['credit_cards']:
            print("No credit cards found.")
            return

        # Ask the user to enter the full card number they want to modify
        card_input = UserInterface.get_user_input(prompt="Enter the full card number you want to modify: ")

        # Find the card matching the full card number
        card_to_modify = None
        for card in user_data['credit_cards']:
            if card['card_number'] == card_input:
                card_to_modify = card
                break

        if not card_to_modify:
            print("Card not found.")
            return

        # Prompt user to modify card details
        new_expiry_date = UserInterface.get_user_input(prompt="Enter new expiry date (MM/YYYY): ")
        new_name_on_card = UserInterface.get_user_input(prompt="Enter new name on card: ")
        new_cvv = UserInterface.get_user_input(prompt="Enter new CVV: ")

        # Update the card details
        card_to_modify['expiry_date'] = new_expiry_date
        card_to_modify['name_on_card'] = new_name_on_card
        card_to_modify['cvv'] = new_cvv

        # Save updated user data
        UserDataManager.save_users(data)
        print("Credit card updated successfully.")
