def calculate_subtotal(products):
    return sum(
        product["quantity"] * product["price"]
        for product in products
    )
def calculate_discount(subtotal):
    if subtotal >= 1000:
        return subtotal * 0.10
    return 0.0
def calculate_tax(subtotal, tax_rate=18):
    return subtotal * tax_rate / 100
def calculate_final_amount(subtotal, discount, tax):
    return subtotal - discount + tax
def get_positive_number(prompt, allow_zero=False):
    while True:
        try:
            value = float(input(prompt))

            if value > 0 or (allow_zero and value == 0):
                return value

            print("Please enter a valid positive value.")

        except ValueError:
            print("Invalid input. Please enter a number.")
def main():
    products = []

    print("=" * 50)
    print("                 SHOP BILLING")
    print("=" * 50)

    while True:
        try:
            count = int(input("Enter number of products: "))

            if count > 0:
                break

            print("Enter at least one product.")

        except ValueError:
            print("Please enter a valid whole number.")

    for i in range(count):
        print(f"\nProduct {i + 1}")

        while True:
            name = input("Product name: ").strip()

            if name:
                break

            print("Product name cannot be empty.")

        quantity = get_positive_number("Quantity: ")
        price = get_positive_number(
            "Unit price (₹): ", allow_zero=True
        )

        products.append({
            "name": name,
            "quantity": quantity,
            "price": price
        })

    # Calculate each amount independently
    subtotal = calculate_subtotal(products)
    discount = calculate_discount(subtotal)
    tax = calculate_tax(subtotal)
    final_amount = calculate_final_amount(
        subtotal, discount, tax
    )

    # Print the bill
    print("\n" + "=" * 64)
    print("                         SHOPPING BILL")
    print("=" * 64)
    print(f"{'Product':<20}{'Qty':>8}{'Price':>16}{'Total':>16}")
    print("-" * 64)

    for product in products:
        total = product["quantity"] * product["price"]

        print(
            f"{product['name'][:20]:<20}"
            f"{product['quantity']:>8g}"
            f"{product['price']:>16.2f}"
            f"{total:>16.2f}"
        )

    print("-" * 64)
    print(f"{'Subtotal:':>44} ₹{subtotal:>12.2f}")
    print(f"{'Discount (10% if eligible):':>44} ₹{discount:>12.2f}")
    print(f"{'Tax (18%):':>44} ₹{tax:>12.2f}")
    print("=" * 64)
    print(f"{'FINAL AMOUNT:':>44} ₹{final_amount:>12.2f}")
    print("=" * 64)
    print("              Thank you for shopping!")

if __name__ == "__main__":
    main()
