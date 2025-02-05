# Develop a program to implement a basic calculator supporting addition, subtraction, multiplication, and division
# Function to perform addition
def addition(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtraction(num1, num2):
    return num1 - num2

# Function to perform multiplication
def multiplication(num1, num2):
    return num1 * num2

# Function to perform division
def division(num1, num2):
    try:
        return num1 / num2  # Returns the division result
    except ZeroDivisionError:
        return "Error! Division by zero is not allowed."  # Handles division by zero error

# Main function to drive the calculator
def main():
    while True:
        # Display calculator options
        print("\n" + "*" * 30)
        print("Welcome to Our Calculator :)")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        # Take user choice as input
        choice = input("Enter Your Choice: ")
        
        # If the user selects 5, exit the program
        if choice == "5":
            print("Thank you for using the calculator. Goodbye!")
            break  # Breaks the loop and exits
        
        # Check if the choice is valid (1-4)
        if choice in ("1", "2", "3", "4"):
            # Take user input for numbers
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))

            # Perform the selected operation
            if choice == "1":
                print(f"Result: {num1} + {num2} = {addition(num1, num2)}")
            elif choice == "2":
                print(f"Result: {num1} - {num2} = {subtraction(num1, num2)}")
            elif choice == "3":
                print(f"Result: {num1} × {num2} = {multiplication(num1, num2)}")
            elif choice == "4":
                print(f"Result: {num1} ÷ {num2} = {division(num1, num2)}")
        else:
            # Handle invalid choices
            print("Invalid choice! Please enter a number between 1 and 5.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
