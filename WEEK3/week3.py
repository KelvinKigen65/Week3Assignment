def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

if discount_percent >= 20:
    print(f"The final price after applying the discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price remains: {final_price:.2f}")
