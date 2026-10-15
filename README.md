

## Description
A Python-based billing system that accepts product names, quantities, and unit prices, then generates a formatted bill showing the subtotal, discount, tax, and final amount.

## Features
- Accepts multiple products from the user.
- Calculates individual product totals.
- Calculates the subtotal of all products.
- Applies a 10% discount when the subtotal is ₹1,000 or more.
- Calculates 18% tax separately on the original subtotal.
- Displays a neatly formatted bill with amounts rounded to two decimal places.
- Validates user inputs to prevent invalid quantities, prices, and empty product names.

## Technologies Used
- Python 3
- Dictionaries and lists
- Functions
- Loops and conditional statements
- Exception handling
- F-strings for formatted output

## Calculation Rules
- **Subtotal:** Sum of all product totals.
- **Discount:** 10% of the subtotal if it is ₹1,000 or more; otherwise, ₹0.
- **Tax:** 18% of the original subtotal, calculated independently of the discount.
- **Final Amount:** Subtotal − Discount + Tax.

## How to Run
1. Install Python 3.
2. Save the program as `billing_system.py`.
3. Open a terminal in the project directory.
4. Run the command:

   ```bash
   python billing_system.py
   ```

5. Enter the number of products, their names, quantities, and unit prices.
6. View the generated bill.

## Example
For a subtotal of ₹1,200:
- Subtotal: ₹1,200.00
- Discount: ₹120.00
- Tax: ₹216.00
- **Final Amount: ₹1,296.00**

## Learning Outcomes
This project demonstrates how to use Python functions, lists, dictionaries, loops, input validation, exception handling, and arithmetic operations to build a practical billing application.

## Future Improvements
- Allow users to choose discount and tax rates.
- Save bills to a text file or PDF.
- Add product IDs and customer details.
- Generate unique invoice numbers.
- Support editing and removing products before checkout.
