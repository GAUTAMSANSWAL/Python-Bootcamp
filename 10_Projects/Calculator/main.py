try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation = input("Enter operation (1/2/3/4): ")

    match operation:
        case "1":
            result = a + b
            print(f"Result: {result}")
        case "2":
            result = a - b
            print(f"Result: {result}")
        case "3":
            result = a * b
            print(f"Result: {result}")
        case "4":
            if b != 0:
                result = a / b
                print(f"Result: {result}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation selected.")

except Exception as e:
    print("Invalid input. Please enter valid integers.")
    exit()