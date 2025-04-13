# Function to calculate discount
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price: "))  # Convert input to float for price
discount_percent = float(input("Enter the discount percentage: "))  # Convert input to float for discount

# Call the function to calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the result based on whether a discount was applied or not
if final_price != price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${price:.2f}")
# The code above is a simple calculator program that allows the user to perform basic arithmetic operations.
# It prompts the user for two numbers and an operation (+, -, *, /), performs the calculation, and prints the result.
# The code below is a discount calculator that checks if the discount percentage is 20% or higher.