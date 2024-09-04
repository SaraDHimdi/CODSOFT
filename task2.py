#Working on Task 2 Calculator:
#Usage:

#1. Run the script.
#2. Enter the first number.
#3. Enter the second number (optional for unary operations).
#4. Choose the desired operation from the menu.
#5. The result will be displayed.

#Additional Notes:

#- The code adheres to Python's best practices for readability, maintainability, and efficiency.
#- Comments are included to explain the purpose of different code sections.
#- The calculator can be easily extended to include more advanced mathematical functions.
#  - @codsoftintern SARA DHIMDI


import math

def calculator():
    """
    The main function that controls the calculator's logic.
    """

    print("Welcome to the Comprehensive Calculator!")

    while True:
        # Get user input for the first number
        num1 = float(input("Enter the first number: "))

        # Check if the user wants to perform a unary operation
        if input("Do you want to perform a unary operation? (y/n): ").lower() == 'y':
            # Get the operation choice for unary operations
            print("Choose a unary operation:")
            print("1. Square root")
            print("2. Exponent")
            print("3. Logarithm")
            choice = int(input("Enter your choice (1-3): "))

            # Perform the chosen unary operation
            if choice == 1:
                result = math.sqrt(num1)
                print("Result:", result)
            elif choice == 2:
                exponent = float(input("Enter the exponent: "))
                result = math.pow(num1, exponent)
                print("Result:", result)
            elif choice == 3:
                base = float(input("Enter the base: "))
                result = math.log(num1, base)
                print("Result:", result)
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
            continue

        # Get user input for the second number (for binary operations)
        num2 = float(input("Enter the second number: "))

        # Get the operation choice for binary operations
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Sine")
        print("6. Cosine")
        print("7. Tangent")
        print("8. Exit")

        choice = int(input("Enter your choice (1-8): "))

        # Perform the chosen binary operation
        if choice == 1:
            result = num1 + num2
            print("Result:", result)
        elif choice == 2:
            result = num1 - num2
            print("Result:", result)
        elif choice == 3:
            result = num1 * num2
            print("Result:", result)
        elif choice == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print("Result:", result)
        elif choice == 5:
            result = math.sin(num1)
            print("Result:", result)
        elif choice == 6:
            result = math.cos(num1)
            print("Result:", result)
        elif choice == 7:
            result = math.tan(num1)
            print("Result:", result)
        elif choice == 8:
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    calculator()