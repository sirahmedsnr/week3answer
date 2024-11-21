def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): Original price of the item.
        discount_percent (float): Discount percentage.

    Returns:
        float: Final price after applying the discount.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    # Prompt user for input
    price = float(input("$90"))
    discount_percent = float(input("30%"))

    # Calculate and print the final price
    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f" {discount_percent}%")
        print(f" ${final_price:.2f}")
    else:
        print("No discount applied.")
        print(f"Final price: ${final_price:.2f}")

if __name__ == "__main__":
    main()