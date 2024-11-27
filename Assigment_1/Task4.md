# Task 4 
The function `checkout_and_payment(login_info)` is the main function in the
`checkout_process.py` file. The function allows the user to:
- Display products available for purchase
- Add them to their cart
- Checkout that cart
- But the items with their wallet
- Logout out

The function has now been updated so the new balance in the wallet is saved after buying the items.

## Input Domain Modeling
As being the main function it interacts with other functions in the `checkout_process.py` file.
That is why for unit testing is important to model all the valid inputs.

The model used for the unit testing is **input domain modeling**. The coverage criterion is **testing at least
two valid inputs for each equivalence class, and one invalid input**.

### What is the space of valid inputs?
Some of the valid inputs connect to external classes like Cart state and Product availability.
ShoppingCart is an external class defined in the file `shopping_cart.py` with the function is_empty(). And 
Product availability is a result of a list generated with objects of the type `Product`. 
Product is a class defined in the external file `product.py`.

| **Input**            | **Type**        | **Detail**                                 |
|----------------------|-----------------|--------------------------------------------|
| Username             | `str`           | Non-empty, valid username in the JSON file |
| Wallet               | `float`         | `wallet >= 0`                              |
| Choice               | `str`           | `"d"`, `"c"`, `"l"`                        |
| Product index        | `int`           | Index existing in the product list         |
| Cart state           | `ShoppingCart`  | Non-empty cart `boolean` state             |
| Product availability | `list[Product]` | `product.units > 0`                        |

### Equivalence classes
Now we turn this valid inputs into equivalence classes. Even when username is an input passed to the function and used
through the execution, the validation of the username is outside the scope of the function. That is why it is not considered
in a equivalence class.

| **Equivalence Class** | **Input**                | **Type**  | **Valid Input**                    |
|-----------------------|--------------------------|-----------|------------------------------------|
| EC1                   | wallet                   | `float`   | Sufficient balance                 |
| EC2                   | choice: display products | `str`     | `"d"`                              |
| EC3                   | choice: check cart       | `str`     | `"c"`                              |
| EC4                   | choice: log out          | `str`     | `"l"`                              |
| EC5                   | choice: product index    | `int`     | Valid product index                |
| EC6                   | cart state               | `boolean` | `non-empty = True`                 |
| EC7                   | product availability     | `product` | `product.units > 0`                |

## Testing Requirements
Now we turn the equivalence classes into testing requirements taking into account the coverage criterion.

**Coverage criterion:** testing at least two valid inputs for each equivalence class, and one invalid input.

| **Equivalence Class** | **Requirement ID**  | **Test Requirement**                                                                                                                |
|-----------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| EC1                   | R1.1                | If input is in EC1, function should return "Thank you for your purchase, `{user.name}`! Your remaining balance is `{user.wallet}`." |
| EC1                   | R1.2                | If input is not in EC1, function should return "You don't have enough money to complete the purchase. Please try again!"            |
| EC2                   | R2.1                | If input is in EC2, function should display list of products                                                                        |
| EC2                   | R2.2                | If input is not in EC2, function should return "Invalid input. Please try again."                                                   |
| EC3 and EC6           | R3.1                | If input is in EC3 and EC6, function should return "Do you want to checkout? - y/n:"                                                |
| EC3                   | R3.2                | If input is not in EC3, function should return "Invalid input. Please try again."                                                   |
| EC4                   | R4.1                | If input is in EC4 and cart is empty, function should return "Do you still want to logout? - y/n:"                                  |
| EC4                   | R4.2                | If input is not in EC4, function should return "Invalid input. Please try again."                                                   |
| EC5 and EC7           | R5.1                | If input is in EC5 and EC7, function should add`{selected_product.name}` to cart.                                                   |
| EC5                   | R5.2                | If input is not in EC5, function should return "Invalid input. Please try again." and cart=[].                                      |
| EC6                   | R6.1                | If input is in EC6, function should return "Do you want to checkout? - y/n:"                                                        |
| EC6                   | R6.2                | If input is not in EC6, function should return "Your basket is empty. Please add items before checking out."                        |
| EC7                   | R7.1                | If input is in EC7, function should return "`{selected_product.name}` added to your cart."                                          |
| EC7                   | R7.2                | If input is not in EC7, function should return "Sorry, `{selected_product.name}` is out of stock."                                  |

## Test Cases 
Once the test requirements are defined we write the test cases to fulfill the coverage criterion.

**Coverage criterion:** testing at least two valid inputs for each equivalence class, and one invalid input.

| **Test Case Id** | **Inputs**                                                         | **Test Case**                                                             |
|------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------|
| TC1.1.1          | login info = [Rover, Dog12@34], cart=[Apple]                       | "Thank you for your purchase, Rover! Your remaining balance is 48.0."     |
| TC1.1.2          | login info = [Cleo, QueenC%at789], cart=[Apple, Banana, Soda]      | "Thank you for your purchase, Cleo! Your remaining balance is 70.5."      |
| TC1.1.3          | login info = [Athena, Wis@eOwl567], cart=[Vacuum Cleaner]          | "Thank you for your purchase, Athena! Your remaining balance is 0."       |
| TC1.2.1          | login info = [Rover, Dog12@34], cart=[Laptop]                      | "You don't have enough money to complete the purchase. Please try again!" |
| TC2.1.1          | login info = [Rover, Dog12@34], choice="d"                         | "Display list of products"                                                |
| TC2.1.2          | login info = [Rover, Dog12@34], choice="d "                        | "Display list of products"                                                |
| TC2.1.3          | login info = [Rover, Dog12@34], choice="D"                         | "Display list of products"                                                |
| TC2.2.1          | login info = [Rover, Dog12@34], choice="j"                         | "Invalid input. Please try again."                                        |
| TC3.1.1          | login info = [Rover, Dog12@34], cart=[Apple, Banana], choice="c"   | "Do you want to checkout? - y/n:"                                         |
| TC3.1.2          | login info = [Rover, Dog12@34], cart=[Apple, Banana], choice="C"   | "Do you want to checkout? - y/n:"                                         |
| TC3.1.3          | login info = [Rover, Dog12@34], cart=[Apple, Banana], choice="C "  | "Do you want to checkout? - y/n:"                                         |
| TC3.2.1          | login info = [Rover, Dog12@34], cart=[Apple, Banana], choice="@#$" | "Invalid input. Please try again."                                        |
| TC4.1.1          | login info = [Rover, Dog12@34], cart=[], choice="l"                | "Do you still want to logout? - y/n:"                                     |
| TC4.1.2          | login info = [Rover, Dog12@34], cart=[], choice="L "               | "Do you still want to logout? - y/n:"                                     |
| TC4.1.3          | login info = [Rover, Dog12@34], cart=[], choice="L"                | "Do you still want to logout? - y/n:"                                     |
| TC4.2.1          | login info = [Rover, Dog12@34], cart=[], choice=" l"               | "Invalid input. Please try again."                                        |
| TC5.1.1          | login info = [Rover, Dog12@34], cart=[], choice="1"                | `cart=[Apple]`                                                            |
| TC5.1.2          | login info = [Rover, Dog12@34], cart=[], choice="71"               | `cart=[Backpack]`                                                         |
| TC5.1.3          | login info = [Luna, Moonlight#456], cart=[Batteries], choice="50"  | `cart=[Batteries, Batteries]`                                             |
| TC5.2.1          | login info = [Rover, Dog12@34], cart=[], choice="1867"             | "Invalid input. Please try again." and `cart=[]`                          |
| TC5.2.2          | login info = [Rover, Dog12@34], cart=[], choice="-897"             | "Invalid input. Please try again." and `cart=[]`                          |
| TC5.2.3          | login info = [Rover, Dog12@34], cart=[], choice="9%3"              | "Invalid input. Please try again." and `cart=[]`                          |
| TC5.2.4          | login info = [Rover, Dog12@34], cart=[], choice="8.9"              | "Invalid input. Please try again." and `cart=[]`                          |
| TC6.1.1          | login info = [Rover, Dog12@34], cart=[Apple], choice="c"           | "Do you want to checkout? - y/n:"                                         |
| TC6.1.2          | login info = [Rover, Dog12@34], cart=[Apple], choice="C"           | "Do you want to checkout? - y/n:"                                         |
| TC6.1.3          | login info = [Rover, Dog12@34], cart=[Apple], choice="c "          | "Do you want to checkout? - y/n:"                                         |
| TC6.2.1          | login info = [Rover, Dog12@34], cart=[], choice="c"                | "Your basket is empty. Please add items before checking out."             |
| TC7.1.1          | login info = [Rover, Dog12@34], cart=[], choice="53"               | "Headphones added to your cart." and `cart=[Headphones]`                  |
| TC7.1.2          | login info = [Rover, Dog12@34], cart=[], choice="61 "              | "Dumbbells added to your cart." and `cart=[Dumbbells]`                    |
| TC7.1.3          | login info = [Luna, Moonlight#456], cart=[Apple], choice="36"      | "Cereal added to your cart." and `cart=[Apple, Cereal]`                   |
| TC7.2.1          | login info = [Rover, Dog12@34], cart=[Watermelon]                  | "Sorry, Watermelon is out of stock."                                      |
| TC7.2.2          | login info = [Rover, Dog12@34], cart=[Backpack]                    | "Sorry, Backpack is out of stock."                                        |
