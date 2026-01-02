# Function to perform calculation
def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator!"

# Welcome message
print("\nWelcome to the Simple Calculator!")
print("You can perform +, -, *, / operations.\n")

# Input numbers from user
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit()

# Input operation
operator = input("Enter the operation (+, -, *, /): ").strip()

# Calculate and display result
result = calculate(number1, number2, operator)
print(f"\nResult: {number1} {operator} {number2} = {result}\n")
