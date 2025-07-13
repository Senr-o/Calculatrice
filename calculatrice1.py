number_1 = 0.0
number_2 = 0.0
result = 0.0
history = []
p_history = "no"
again = "yes"
carry = "no"

print("""Welcome to my simple calculator!
You can perform addition, substraction, multiplication, and division.""")


while again == "yes":

    while True:
        if carry != "yes":
            number_1 = input("Enter first number: ")
            try:
                number_1 = float(number_1)
                break
            except ValueError:
                print("Error: Please enter a valid number for the first number.")
        else:
            number_1 = result
            break

    while True:
        operation_symbol = input("Enter operation symbol (+, -, *, /) : ")
        if operation_symbol in ["+", "-", "*", "/"]:
            break
        else:
            print("Error: Please enter a valide operation symbol (+, -, *, /).")

    while True:
        number_2 = input("Enter second number: ")
        try:
            number_2 = float(number_2)
            break
        except ValueError:
            print("Error: Please enter a valid number for the second number.")

    if operation_symbol == "+":
        result = number_1 + number_2
    elif operation_symbol == "-":
        result = number_1 - number_2
    elif operation_symbol == "*": 
        result = number_1 * number_2
    elif operation_symbol == "/":
        if number_2 !=0:
            result = number_1 / number_2
        else:
            print("Error: Division by zero is not allowed.")


    print(f"{number_1} {operation_symbol} {number_2} = {result}")

    history.append(f"{number_1} {operation_symbol} {number_2} = {result}")

    while True:
        p_history = input("Do you want to print the history of operations? (yes/no): ").strip().lower()
        if p_history in ["yes", "no"]:
            if p_history == "yes":
                print("History of operations:")
                for op in history:
                    print(op)
                break
            else:
                break
        else:
            print("Invalide response.")

    while True:
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again in ["yes", "no"]:
            if again == "no":
                print("Thanks for using the calculator!")
                break
            else:
                break
        else:
            print("Invalid response.")
            
    if again == "no":
        break

    while True:
        carry = input("Do you want to carry the result to the next calculation? (yes/no): ").strip().lower()
        if carry in ["yes", "no"]:
            if carry == "yes":
                break
            else:
                break
        else:
            print("Invalid response.")