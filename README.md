# Discount Calculator Program

## Purpose
This Python program calculates the final price of an item after applying a discount, but only if the discount percentage is 20% or higher. It prompts the user to input the original price and discount percentage, computes the final price using a function, and displays whether a discount was applied or not. The program demonstrates key Python concepts, including:
- Function definition and usage
- Conditional statements (`if-else`)
- User input handling
- Floating-point arithmetic
- Formatted output

It’s designed as an educational tool for learning basic programming logic and is useful for scenarios like retail pricing where minimum discount thresholds apply.

## How to Run
Follow these steps to run the discount calculator program on your computer:

### Prerequisites
- **Python 3.x**: Ensure Python is installed. Download it from [python.org](https://www.python.org/downloads/) if needed, or check your version by running:
  ```bash
  python --version

#### Installation 
Clone the repository using Git:
git clone https://github.com/your-username/discount-calculator.git

##### Running the Program

Run the program using Python:
```bash
python discount_calculator.py (Or python3 discount_calculator.py if python doesn’t work.)

######  Follow the prompts:
Enter the original price (e.g., 50 or 99.99).

Enter the discount percentage (e.g., 25 or 15).

###### View the result:
If the discount is 20% or higher, the program shows the discounted price (e.g., $37.50).

If the discount is less than 20%, the original price is shown with a note that no discount was applied.

##### Example Usage
Example 1: Discount Applied

Enter the original price: 100
Enter the discount percentage: 25
The final price after applying the discount is: $75.00

Example 2: No Discount Applied

Enter the original price: 50
Enter the discount percentage: 10
No discount applied. The original price is: $50.00

##### Notes

The program accepts decimal inputs for both price and discount percentage (e.g., 49.99 or 20.5).

Prices are displayed with two decimal places (e.g., $10.00) for clarity.

If non-numeric inputs (e.g., "abc") are entered, the program will crash. Future improvements could include input validation.

The discount threshold is fixed at 20%, but the code could be modified to make it adjustable.


License
This project is unlicensed and free to use for educational purposes.




