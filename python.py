def calculate_discounted_price(original_price, discount_percentage):
    if original_price < 0 or discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Original price and discount percentage must be positive, and discount percentage must not exceed 100.")
    
    discount_amount = (discount_percentage / 100) * original_price
    discounted_price = original_price - discount_amount
    if original_price < 150:
        return original_price, 0  # No discount applied if price is below 150

    return discounted_price, discount_amount

try:
    original_price = float(input("Enter the original price (R): "))
    discount_percentage = float(input("Enter the discount percentage: "))
    discounted_price, discount_amount = calculate_discounted_price(original_price, discount_percentage)
    if discount_amount == 0:
        print(f"The price of R{original_price:.2f} does not qualify for a discount.")
    else:
        print(f"The original price: R{original_price:.2f}")
        print(f"Discount percentage: {discount_percentage:.2f}%")
        print(f"Amount deducted: R{discount_amount:.2f}")
        print(f"The discounted price is: R{discounted_price:.2f}")
except ValueError as e:
    print(f"Error: {e}")