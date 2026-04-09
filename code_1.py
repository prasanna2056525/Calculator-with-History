History_file = "history.txt"

def show_history():
    file = open(History_file, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("No history found.")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(History_file, "w")
    file.write("")
    file.close()
    print("History cleared.")

def save_history(equation, result):
    file = open(History_file, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Please enter in the format: number operator number")
        return None

    try:
        num1 = float(parts[0])
        num2 = float(parts[2])
    except ValueError:
        print("Error: Please enter valid numbers.")
        return None

    operator = parts[1]

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return None
        result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return None

    # ✅ Now reachable
    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_history(user_input, result)

def main():
    print('--- Simple Calculator with History ---')
    while True:
        user_input = input("Enter calculation (+ - * /) or command (history / clear / exit): ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break          # ✅ actually exits
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

main()