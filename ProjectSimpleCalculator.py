print("Welcome to the Simple Calculator!")

while True:
    print("\n=== Calculator Menu ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                result = num1 + num2
                operation = "Addition"
            elif choice == "2":
                result = num1 - num2
                operation = "Subtraction"
            elif choice == "3":
                result = num1 * num2
                operation = "Multiplication"
            elif choice == "4":
                if num2 != 0:
                    result = num1 / num2
                    operation = "Division"
                else:
                    print("Error: Division by zero is not allowed.")
                    continue

            print(f"\n{operation} of {num1} and {num2} is: {result}")
        except ValueError:
            print("Error: Please enter valid numbers.")

    elif choice == "5":  # Exit
        print("Goodbye! Thank you for using the calculator.")
        break

    else:
        print("Invalid choice! Please try again.")