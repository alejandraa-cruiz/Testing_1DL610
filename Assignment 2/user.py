################
# USER CLASSES #
################


class User:
    class User:
        """
        User class to represent user information, including credit card details
        """

        def __init__(self, name, wallet, credit_cards=None) -> None:
            self.name: str = name
            self.wallet: float = wallet
            self.credit_cards = credit_cards if credit_cards else []

        def add_credit_card(self, card_number: str, expiry_date: str, name_on_card: str, cvv: str) -> None:
            """
            Adds a new credit card to the user's profile.
            """
            self.credit_cards.append({
                'card_number': card_number,
                'expiry_date': expiry_date,
                'name_on_card': name_on_card,
                'cvv': cvv
            })

        def update_credit_card(self, card_index: int, card_number: str, expiry_date: str, name_on_card: str,
                               cvv: str) -> None:
            """
            Updates an existing credit card in the user's profile.
            """
            if 0 <= card_index < len(self.credit_cards):
                self.credit_cards[card_index] = {
                    'card_number': card_number,
                    'expiry_date': expiry_date,
                    'name_on_card': name_on_card,
                    'cvv': cvv
                }
            else:
                print("Invalid card index.")
