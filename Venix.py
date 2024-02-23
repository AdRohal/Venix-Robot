import datetime

bot_name = 'Venix'

# Get the current year
current_year = datetime.datetime.now().year

print(f"Hello Friend! My name is {bot_name}.")
print(f"I was created in {current_year}.")
print("By 'AdRohal'.")
print("Ready for some Math?")

def calculator_robot():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the calculator robot. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please enter a valid option.")
            continue

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = num1 + num2
            operation = 'Addition'
        elif choice == '2':
            result = num1 - num2
            operation = 'Subtraction'
        elif choice == '3':
            result = num1 * num2
            operation = 'Multiplication'
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                operation = 'Division'
            else:
                print("Error: Cannot divide by zero.")
                continue

        print(f"{operation} result: {result}")

if __name__ == "__main__":
    calculator_robot()
