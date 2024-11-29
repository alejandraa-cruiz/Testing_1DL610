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
| EC1                   | choice: display products | `str`     | `"d"`                              |
| EC2                   | choice: check cart       | `str`     | `"c"`                              |
| EC3                   | choice: log out          | `str`     | `"l"`                              |
| EC4                   | choice: product index    | `int`     | Valid product index                |
| EC5                   | product availability     | `product` | `product.units > 0`                |

## Testing Requirements
Now we turn the equivalence classes into testing requirements taking into account the coverage criterion.

**Coverage criterion:** testing at least two valid inputs for each equivalence class, and one invalid input.

| **Equivalence Class** | **Requirement ID** | **Test Requirement**                                                                               |
|-----------------------|--------------------|----------------------------------------------------------------------------------------------------|
| EC1                   | R1.1               | If input is in EC1, function should call display_list_of_products function                         |
| EC1                   | R1.2               | If input is not in EC1, function should return "Invalid input. Please try again."                  |
| EC2                   | R2.1               | If input is in EC2, function should call check_cart function                                       |
| EC2                   | R2.2               | If input is in EC2, function should return "Invalid input. Please try again."                      |
| EC3                   | R3.1               | If input is in EC3, function should logout                                                         |
| EC3                   | R3.2               | If input is not in EC3, function should return "Invalid input. Please try again."                  |
| EC4                   | R4.1               | If input is in EC4, function should add`{selected_product.name}` to cart.                          |
| EC4                   | R4.2               | If input is not in EC4, function should return "Invalid input. Please try again."                  |
| EC5                   | R5.1               | If input is in EC5, function should return "`{selected_product.name}` added to your cart."         |
| EC5                   | R5.2               | If input is not in EC5, function should return "Sorry, `{selected_product.name}` is out of stock." |

## Test Cases 
Once the test requirements are defined we write the test cases to fulfill the coverage criterion. TC 3.1.1, 3.1.2, 3.1.3

**Coverage criterion:** testing at least two valid inputs for each equivalence class, and one invalid input.

| **Test Case Id** | **Inputs**                                     | **Test Case**                        |
|------------------|------------------------------------------------|--------------------------------------|
| TC1.1.1          | login info = [Rover, Dog12@34], choice="d"     | calls display_list_of_products()     |
| TC1.1.2          | login info = [Rover, Dog12@34], choice="d "    | calls display_list_of_products()     |
| TC1.1.3          | login info = [Rover, Dog12@34], choice="D"     | calls display_list_of_products()     |
| TC1.2.1          | login info = [Rover, Dog12@34], choice="j"     | "Invalid input. Please try again."   |
| TC2.1.1          | login info = [Rover, Dog12@34],  choice="c"    | calls check_cart()                   |
| TC2.1.2          | login info = [Rover, Dog12@34],  choice="C"    | calls check_cart()                   |
| TC2.1.3          | login info = [Rover, Dog12@34],  choice="C "   | "calls check_cart()                  |
| TC2.2.1          | login info = [Rover, Dog12@34],  choice="@#$"  | "Invalid input. Please try again."   |
| TC3.1.1          | login info = [Rover, Dog12@34],  choice="l"    | exit value code = 0                  |
| TC3.1.2          | login info = [Rover, Dog12@34],  choice="L "   | exit value code = 0                  |
| TC3.1.3          | login info = [Rover, Dog12@34],  choice="L"    | exit value code = 0                  |
| TC3.2.1          | login info = [Rover, Dog12@34],  choice=" l"   | "Invalid input. Please try again."   |
| TC4.1.1          | login info = [Rover, Dog12@34],  choice="1"    | "Apple added to your cart."          |
| TC4.1.2          | login info = [Rover, Dog12@34],  choice="71"   | "Backpack added to your cart."       |
| TC4.1.3          | login info = [Rover, Dog12@34],  choice="50"   | "Batteries added to your cart."      |
| TC4.2.1          | login info = [Rover, Dog12@34],  choice="1867" | "Invalid input. Please try again."   |
| TC4.2.2          | login info = [Rover, Dog12@34],  choice="-897" | "Invalid input. Please try again."   |
| TC4.2.3          | login info = [Rover, Dog12@34], choice="9%3"   | "Invalid input. Please try again."   |
| TC4.2.4          | login info = [Rover, Dog12@34],  choice="8.9"  | "Invalid input. Please try again."   |
| TC5.1.1          | login info = [Rover, Dog12@34],  choice="53"   | "Headphones added to your cart."     |
| TC5.1.2          | login info = [Rover, Dog12@34],  choice="61 "  | "Dumbbells added to your cart."      |
| TC5.1.3          | login info = [Rover, Dog12@34], choice="36"    | "Cereal added to your cart."         |
| TC5.2.1          | login info = [Rover, Dog12@34], choice="6"     | "Sorry, Watermelon is out of stock." |
| TC5.2.2          | login info = [Rover, Dog12@34], choice"55"     | "Sorry, Coffee is out of stock."     |
